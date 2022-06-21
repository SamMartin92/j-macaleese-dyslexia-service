from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home/index.html')


def client_details_form(request):
    if request.method == 'POST':
        name = request.POST.get('client_name')
        phone = request.POST.get('client_phone')
        is_guardian = 'is_guardian' in request.POST
        childs_name = request.POST.get('childs_namee')
        already_diagnosed = 'already_diagnosed' in request.POST
    return render(request, 'home/client_details_form.html')