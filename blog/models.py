from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    context = models.TextField(max_length=1000)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ['-pub_date',]

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post')
    pub_date = models.DateField(auto_now_add=True)
    text = models.TextField(max_length=1000)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ['-pub_date',]

    def __unicode__(self):
        return 'author: {} - post: {}'.format(self.author.username, self.post.title)

