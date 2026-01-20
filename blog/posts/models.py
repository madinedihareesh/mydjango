from django.db import models

# Create your models here.
class Post(models.Model):
    post_title=models.CharField(max_length=60)
    post_dis=models.TextField()
    post_Cdate=models.DateTimeField(auto_now=True)
