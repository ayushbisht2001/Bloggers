from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True,blank = True)

class Blog:
    title = "hello world"
    content = "ayush bisht"
