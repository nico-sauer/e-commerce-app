from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import SearchForm
from .recommender import Recommender
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


def home(request):
    products = Product.objects.filter(available=True).order_by('-created')[:8]
    return render(request, "shop/index.html", {'products': products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    object_list = Product.objects.filter(available=True)
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        if category_slug:
            language = request.LANGUAGE_CODE
            category = get_object_or_404(Category,
                                         translations__language_code=language,
                                         translations__slug=category_slug)
            object_list = object_list.filter(category=category)
            paginator = Paginator(object_list, 6)
            page = request.GET.get('page')
            products = paginator.page(page)
        else:
            products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    return render(request, "shop/product-list.html",
                  {"category": category, "categories": categories,
                   "products": products, "page": page},
                  )


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product,
                                id=id,
                                translations__language_code=language,
                                translations__slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(
        request,
        "shop/product-detail.html",
        {"product": product,
         "cart_product_form": cart_product_form,
         "recommended_products": recommended_products})


def product_search(request):
    language = request.LANGUAGE_CODE
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector(
                'translations__name', 'specification',
                'brand', 'category')
            search_query = SearchQuery(query)
            results = Product.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(
                search=search_query, available=True,
                translations__language_code=language
            ).order_by('-rank').distinct()
    return render(request, 'shop/search.html',
                  {'form': form, 'query': query,
                   'results': results})
