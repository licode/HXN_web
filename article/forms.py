from django import forms
from models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'algorithm', 'angle_start', 'angle_end', 'angle_step', 'notes', 'upload_file')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'body')


