from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blogs(models.Model):
    creater = models.ForeignKey(User, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 150)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    likes = models.CharField(max_length = 100, null = True)
    dislikes = models.CharField(max_length = 100, null = True)

class Comments(models.Model):
    commented_on = models.ForeignKey(Blogs, on_delete = models.CASCADE)
    written_by = models.CharField(max_length = 100)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add = True)




