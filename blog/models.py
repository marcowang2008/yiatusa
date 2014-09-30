from django.db import models
from datetime import datetime
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.categoryName


class Post(models.Model):
    title = models.CharField(max_length=60)
    body = HTMLField()
    category = models.ForeignKey(Category)
    viewNum = models.IntegerField(default=0, editable=False)
    tags = models.ManyToManyField('Tag')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=datetime.now())    #for auto publish feature
        
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ('created',)
    

class Tag(models.Model):
    tagName = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.tagName


class Comment(models.Model):
    ip = models.CharField(max_length=20)
    body = models.TextField()
    visitorName = models.CharField(max_length=30)
    post = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now_add=True)


class Statistic(models.Model):
    ip = models.CharField(max_length=20)
    visited = models.DateTimeField(auto_now_add=True)
    
    













