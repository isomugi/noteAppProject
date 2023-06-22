from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.
#使うモデルの名前や変数等を設定する　
#https://itc.tokyo/django/all-about-modelfield/ モデルフィールドについて

class Post(models.Model):
    title = models.CharField(max_length=20, null = True)
    pub_date = models.DateTimeField(auto_now_add = True)
    content = models.TextField(verbose_name = '内容')
    #url = models.URLField(null = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
        
class PostModel(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


""" class Comment(models.Model):
    Post = models.ForeignKey('Post', on_delate = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    content = models.TextField(verbose_name = '内容')
    author = models.ForeignKey(User, on_delate = models.CASCADE)
 """