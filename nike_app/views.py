from django.shortcuts import render, get_object_or_404, redirect
from .models import nikies
from nike_app.models import nikies, HomeProduct  # HomeProduct رو اضافه کن
from contect_app.models import ContactMessage


def nike(request):
    niki = nikies.objects.all()
    return render(request, 'nike_app/nike.html', {'nikies': niki})


def kharid(request, id):
    product = get_object_or_404(nikies, id=id)

    quantity = request.session.get('quantity', 1)

    if request.method == "POST":
        action = request.POST.get('action')

        if action == "plus":
            quantity += 1

        elif action == "minus" and quantity > 1:
            quantity -= 1

        elif action == "delete":
            return redirect('nike')

        request.session['quantity'] = quantity

    total_price = product.ghymat * quantity

    return render(request, 'nike_app/kharid.html', {
        'product': product,
        'quantity': quantity,
        'total_price': total_price,
    })
    


def home_kharid(request, id):
    product = get_object_or_404(HomeProduct, id=id)

    return render(request, 'sabadkharid.html', {
        'product': product,
    })