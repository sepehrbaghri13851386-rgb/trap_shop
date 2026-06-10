from django.shortcuts import render
from kala_app.models import formi
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from contect_app.models import ContactMessage
from nike_app.models import nikies,HomeProduct
def index(request):
    about_data = formi.objects.all()

    context = {
        'formies': about_data,
    }
    return render(request, 'products.html', context)





def contact (request):
    return render(request,'contact.html')
def shopp(request):
    comments = ContactMessage.objects.filter(is_approved=True)
    products = nikies.objects.all()  # اضافه کن
    return render(request, 'index.html', {
        'comments': comments,
        'products': products,  # اضافه کن
    })

def prod (request):
    return render(request,'products.html')
def sliad3 (request):
    return render(request,'aslad3.html')
def about (request):
    return render(request,'blog_app/about.html')


def login (request):
    return render(request,'login.html')



def shopp(request):
    comments = ContactMessage.objects.filter(is_approved=True)

    men_products = HomeProduct.objects.filter(category='men')
    women_products = HomeProduct.objects.filter(category='women')
    kids_products = HomeProduct.objects.filter(category='kids')

    return render(request, 'index.html', {
        'comments': comments,
        'men_products': men_products,
        'women_products': women_products,
        'kids_products': kids_products,
    })


