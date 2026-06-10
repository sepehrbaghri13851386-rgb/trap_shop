from .models import formi, CartItem
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    formies = formi.objects.all()

    return render(
        request,
        'products.html',
        {'formies': formies}
    )


def product_detail(request, id):
    product = get_object_or_404(formi, id=id)
    

    return render(
        request,
        'kala_app/product_detail.html',
        {'product': product}
    )



