from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientDetailsForm

# Create your views here.
def home_page(request):
    return render(request, 'home/index.html')


def client_details_form(request):
    if request.method == 'POST':
        # form = ClientDetailsForm(request.POST)
        # user = request.user
        # if form.is_valid():
        #     new_client = form.save(commit=False)
        #     new_client.user = request.user
        #     new_client.save()
        # name = request.POST.get('client_name')
        phone = request.POST.get('client_phone')
        is_guardian = 'is_guardian' in request.POST
        childs_name = request.POST.get('childs_name')
        already_diagnosed = 'already_diagnosed' in request.POST
        Client.objects.create(user=request.user, phone=phone, is_guardian=is_guardian,
                                    childs_name=childs_name,
                                    already_diagnosed=already_diagnosed)
        
        return redirect('home_page')
    # form = ClientDetailsForm()
    # context = {
    #     'form': form
    # }

    return render(request, 'home/client_details_form.html')