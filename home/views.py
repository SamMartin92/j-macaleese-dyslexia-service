from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientDetailsForm

# Create your views here.
def home_page(request):
    context = {}
    if request.user.is_authenticated:
        clients = Client.objects.all()
        client = clients.filter(user=request.user)      
        if request.method == 'POST':
            form = ClientDetailsForm(request.POST)
            phone = request.POST.get('client_phone')
            is_guardian = 'is_guardian' in request.POST
            childs_name = request.POST.get('childs_name')
            already_diagnosed = 'already_diagnosed' in request.POST
            Client.objects.create(user=request.user, phone=phone, is_guardian=is_guardian,
                                        childs_name=childs_name,
                                        already_diagnosed=already_diagnosed)
            
            return redirect('home_page')
        form = ClientDetailsForm()
        context = {
            'client': client,
            'form': form
        }   
    return render(request, 'home/index.html', context)


def services(request):
    return render(request, 'home/services.html')


def client_details_form(request):
    if request.method == 'POST':
        form = ClientDetailsForm(request.POST)
        phone = request.POST.get('client_phone')
        is_guardian = 'is_guardian' in request.POST
        childs_name = request.POST.get('childs_name')
        already_diagnosed = 'already_diagnosed' in request.POST
        Client.objects.create(user=request.user, phone=phone, is_guardian=is_guardian,
                                    childs_name=childs_name,
                                    already_diagnosed=already_diagnosed)
        
        return redirect('home_page')
    form = ClientDetailsForm()
    context = {
        'form': form
    }

    return render(request, 'home/client_details_form.html')