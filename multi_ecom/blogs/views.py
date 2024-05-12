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
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.posted_by = request.user
            problem = form.save()
            return redirect('problem_detail', pk=problem.pk)
    else:
        form = ProblemForm()
    problems = Problem.objects.all()
    return render(request, 'blogs/post_problem.html', {'form': form, 'problems': problems})


def problem_detail(request, pk):
    problem = Problem.objects.get(pk=pk)
    comments = Comment.objects.filter(problem=problem)
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
    return render(request, 'blogs/problem_detail.html', {'problem': problem, 'comments': comments, 'comment_form': comment_form})
