from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='blog',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)     
    
    def __str__(self):
        return self.title
    
class Problem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image=models.ImageField(upload_to='problem',blank=True,null=True)
    posted_by = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    posted_at = models.DateTimeField(auto_now_add= True)   #time of posting the problem
    

class Comment(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    commented_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)
       