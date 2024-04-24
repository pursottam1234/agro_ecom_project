from django.shortcuts import render
from .models import Blogs

# Create your views here.
def handleblog(request):
    posts=Blogs.objects.all() #get all blogs in the database
    context={"posts":posts} # passing as a dictionary
    return render(request,'blogs/handleblog.html',context)