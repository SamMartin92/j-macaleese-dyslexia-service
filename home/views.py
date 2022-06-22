from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Client

# Create your views here.
def home_page(request):
    return render(request, 'home/index.html')


def client_details_form(request):
    if request.method == 'POST':
        name = request.POST.get('client_name')
        phone = request.POST.get('client_phone')
        is_guardian = 'is_guardian' in request.POST
        childs_name = request.POST.get('childs_name')
        already_diagnosed = 'already_diagnosed' in request.POST
        Client.objects.create(user=request.user, name=name, phone=phone, is_guardian=is_guardian,
                                    childs_name=childs_name,
                                    already_diagnosed=already_diagnosed)
        
        return redirect('home_page')

    return render(request, 'home/client_details_form.html')