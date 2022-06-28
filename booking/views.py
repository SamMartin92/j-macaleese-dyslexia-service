from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib.auth.models import User

# Create your views here.
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        user = request.user
        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.user = request.user
            new_booking.save()
            return redirect('home_page')
    form = BookingForm()
    context = {
        'form': form
    }

    return render(request, 'booking/make_booking.html', context)


def get_bookings(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    #user_bookings = bookings.
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/view_bookings.html', context)
