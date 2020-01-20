from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('about/',views.AboutUsView.as_view(),name='about us'),
    path('contact/',views.ContactUsView.as_view(),name='contact us'),

]
