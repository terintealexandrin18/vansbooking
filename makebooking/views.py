from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import BookingForm

@login_required
def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or render success page
    else:
        form = BookingForm()
    return render(request, 'makebooking/make_booking.html', {'form': form})