from django import forms
from .models import Problem, Comment

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['title', 'description', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
