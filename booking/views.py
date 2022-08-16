import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm


@login_required
def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        user = request.user
        if form.is_valid():
            new_booking = form.save(commit=False)
            if new_booking.booking_date <= datetime.date.today():
                messages.info(
                    request,
                    'Bookings must be made at least 1 day in advance,' +
                    'please select another date',
                    extra_tags='same_day_booking')
            else:
                new_booking.user = request.user
                new_booking.save()
                return redirect('get_bookings')
        else:
            messages.info(
                request,
                'Time unavailable, please choose another time slot',
                extra_tags='dup_booking')
    form = BookingForm()
    context = {
        'form': form
    }

    return render(request, 'booking/make_booking.html', context)


@login_required
def get_bookings(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    pending_bookings = []
    confirmed_bookings = []
    past_bookings = []
    for booking in bookings:
        if booking.status == 0:
            pending_bookings.append(booking)
        elif booking.status == 1:
            confirmed_bookings.append(booking)
        elif booking.status == 3:
            past_bookings.append(booking)

    context = {
        'upcoming_bookings': pending_bookings + confirmed_bookings,
        'pending_bookings': pending_bookings,
        'confirmed_bookings': confirmed_bookings,
        'past_bookings': past_bookings
    }
    return render(request, 'booking/view_bookings.html', context)


@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        user = request.user
        if form.is_valid():         
                new_booking = form.save(commit=False)
                if new_booking.booking_date <= datetime.date.today():
                    messages.info(
                        request,
                        'Bookings must be made at least 1 day in advance,' +
                        'please select another date',
                        extra_tags='same_day_booking')
                else:
                    new_booking.user = request.user
                    new_booking.status = 0
                    new_booking.save()
                    return redirect('get_bookings')
        else:
            messages.info(
                request,
                'Time unavailable, please choose another time slot',
                extra_tags='dup_booking')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_booking.html', context)


def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('get_bookings')
