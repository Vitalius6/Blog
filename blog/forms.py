from . import models
from django.forms import ModelForm
from django.contrib.auth import get_user_model

user = get_user_model()

class AddPostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','context']


class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text', 'post']