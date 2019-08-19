from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class POST(models.Model):

    title= models.CharField(max_length=100)
    content= models.TextField()

    post_date= models.DateTimeField(default=timezone.now)
    post_update= models.DateTimeField(auto_now=True)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
       ordering=('-post_date', )
class comment(models.Model):
    name=models.CharField(max_length=50,blank=False,verbose_name="الاسم")
    email=models.EmailField(verbose_name="البريد الالكترني")
    body=models.TextField(verbose_name="التعليق")
    comment_date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)
    post=models.ForeignKey(POST,on_delete=models.CASCADE,related_name='comments')

    def __str__(self):
        return ' .{}على{}علق '.format(self.name,self.post)
    class Meta:
       ordering=('-comment_date', )
class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    picture=models.ImageField(default='default.jpg',upload_to="cover")
    website=models.URLField(blank=True,null=True)
    description = models.TextField()
    sample=models.FileField(blank=True,null=True,upload_to="chapters")
    def __str__(self):
        return self.title



