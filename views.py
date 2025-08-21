from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import SignUpForm, ProfileForm, BookingForm
from .models import TravelOption, Booking


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created. You are now logged in!')
            login(request, user)
            return redirect('travel_options')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


def travel_options(request):
    # Filters: type, source, destination, date
    q_type = request.GET.get('type')
    q_source = request.GET.get('source')
    q_destination = request.GET.get('destination')
    q_date = request.GET.get('date')  # yyyy-mm-dd

    qs = TravelOption.objects.all()

    if q_type:
        qs = qs.filter(type=q_type)
    if q_source:
        qs = qs.filter(source__icontains=q_source)
    if q_destination:
        qs = qs.filter(destination__icontains=q_destination)
    if q_date:
        qs = qs.filter(departure__date=q_date)

    # Only show future departures
    qs = qs.filter(departure__gte=timezone.now()).order_by('departure')

    return render(request, 'travel_option_list.html', {
        'travel_options': qs,
        'params': {
            'type': q_type or '',
            'source': q_source or '',
            'destination': q_destination or '',
            'date': q_date or '',
        }
    })


@login_required
def book_travel(request, pk):
    travel = get_object_or_404(TravelOption, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST, travel_option=travel)
        if form.is_valid():
   
