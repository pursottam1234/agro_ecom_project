from django.urls import path

from core import views
urlpatterns = [
    path('',views.frontpage,name="frontpage"),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
]