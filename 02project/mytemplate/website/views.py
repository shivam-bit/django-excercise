from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name='home.html'
class AboutUsView(TemplateView):
    template_name='aboutus.html'
class ContactUsView(TemplateView):
    template_name='contactUs.html'
    

