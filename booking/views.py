from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.db import IntegrityError
from django.contrib import messages


# Create your views here.
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        user = request.user
        if form.is_valid():
            try:
                new_booking = form.save(commit=False)
                new_booking.user = request.user
                new_booking.save()
                return redirect('get_bookings')
            except IntegrityError:
                messages.info(request, 'Time unavailable, please choose another time slot', extra_tags='dup_booking')
                return redirect('make_booking')
                  
    form = BookingForm()
    context = {
        'form': form
    }

    return render(request, 'booking/make_booking.html', context)


def get_bookings(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/view_bookings.html', context)


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        user = request.user
        if form.is_valid():
            try:
                new_booking = form.save(commit=False)
                new_booking.user = request.user
                new_booking.save()
                return redirect('get_bookings')
            except IntegrityError:
                messages.info(request, 'Time unavailable, please choose another time slot', extra_tags='dup_booking')
                
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_booking.html', context)

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('get_bookings')