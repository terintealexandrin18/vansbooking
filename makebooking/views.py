from django.shortcuts import render
from .forms import BookingForm
# Create your views here.

def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # Redirect or render success page
    else:
        form = BookingForm(user=request.user)
    return render(request, 'makebooking/make_booking.html', {'form': form})