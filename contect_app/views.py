from django.shortcuts import render, redirect
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )

        return redirect('/contact/')

    return render(request, 'contact.html')
