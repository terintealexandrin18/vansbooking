from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    """
    Render the contact form and handle form submission for sending messages.

    **Context**
    - ``form``: An instance of :form:`contact.ContactForm`.
    - ``submitted``: Boolean indicating if the form has been submitted
     successfully.

    **Template**
    :template:`contact/contact.html`
    """

    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            messages.success(request, 'Your message has been sent '
                                      'successfully! We will get back '
                                      'to you shortly.')
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form,
                                                    'submitted': submitted})
