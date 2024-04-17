from django.shortcuts import render
from .models import HomePage

# Create your views here.


def home(request):
    """
    View function for the homepage.

    Retrieves all HomePage objects and orders them by 'updated_on'
    field in descending order.

    **Context:**
    - ``home_pages``: QuerySet of all HomePage objects.

    **Template:**
    :template:`homepage/index.html`
    """
    home_pages = HomePage.objects.all().order_by('-updated_on')
    return render(
        request,
        "homepage/index.html",
        {"home_pages": home_pages},
    )
