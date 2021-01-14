from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I9J9BEGbSY0iiFOlMPrSY8a6fJmB0xZT0JswS4FyRIIhX0Zn74hppfr6lHgpdehdGz1biEu0Xt6ALKwzKUDpVhh00kh8QQjN5',
        'client_secret': 'test cl',
    }

    return render(request, template, context)