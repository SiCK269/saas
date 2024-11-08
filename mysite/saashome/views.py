import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import *

this_dir = pathlib.Path(__file__).resolve().parent
BASE_DIR = this_dir.parent
print(BASE_DIR)

def home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    context = {
        'page_title': my_title
    }
    html_template = "home.html"

    return render(request, html_template, context)

def about_page_view(request, *args, **kwargs):
    my_title = "About Page"
    context = {
        'page_title': 'about'
    }
    html_template = 'about.html'

    return render(request, html_template, context)