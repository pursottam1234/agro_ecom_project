from django.shortcuts import render, redirect 
from .forms import ProblemForm, CommentForm
from .models import Blogs, Problem, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def handleblog(request):
    posts=Blogs.objects.all() #get all blogs in the database
    context={"posts":posts} # passing as a dictionary
    return render(request,'blogs/handleblog.html',context)



@login_required
def post_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.posted_by = request.user
            problem.save()
            return redirect('problem_detail', pk=problem.pk)
    else:
        form = ProblemForm()
    return render(request, 'blogs/post_problem.html', {'form': form})


def problem_detail(request, pk):
    problem = Problem.objects.get(pk=pk)
    comments = problem.comments.all()
    
     # Check if the current user is the author of the problem
    is_author = (request.user == problem.posted_by)
    
    if not is_author:  # Only allow non-authors to comment
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.problem = problem
                comment.commented_by = request.user
                comment.save()
                return redirect('problem_detail', pk=pk)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None  # Set comment_form to None if the user is the author
    
    return render(request, 'blogs/problem_detail.html', {'problem': problem, 'comments': comments, 'comment_form': comment_form})

