from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

# Create your views here.
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        client=request.client
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.client = request.client
            new_booking.save()
            return redirect('home_page')
    form = BookingForm()
    context = {
        'form': form
    }

    return render(request, 'booking/make_booking.html', context)