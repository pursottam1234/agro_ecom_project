from blogs import views
from django.urls import path,include

urlpatterns = [
    path('',views.handleblog,name='handleblog'),
]