from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from payments.models import Payment

def pay(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        Payment.objects.create(
            order=order,
            amount_paid=order.total_price(),
            status="success",
        )
        order.confirmed = True
        order.save()
        order.paid = True
        return redirect("payments:success")
    return render(request, "payments/confirm_payment.html", {"order": order})

def success(request):
    return render(request, "payments/success.html")