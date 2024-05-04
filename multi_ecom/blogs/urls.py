from blogs import views
from django.urls import path,include

urlpatterns = [
    path('blog',views.handleblog,name='handleblog'),
    path('post-problem/',views.post_problem, name='post_problem'),
    path('problem/<int:pk>/',views.problem_detail, name='problem_detail'),
]