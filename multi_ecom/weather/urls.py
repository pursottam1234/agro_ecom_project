from django.urls import path
from .views import weather_view
from weather import views 
urlpatterns = [
    path('weatherview', views.weather_view, name='weatherview'),

]
