from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact_us(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            messages.success(request, 'Your message has been sent successfully! We will get back to you shortly.')
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'submitted': submitted})