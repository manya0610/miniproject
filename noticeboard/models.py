from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse



# Create your models here.

class Notice(models.Model):
    title=models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('notice_detail', args=[str(self.id)])
class Comment(models.Model):
    notice= models.ForeignKey(Notice,on_delete=models.CASCADE,related_name='comments')
    comment= models.CharField(max_length=255)
    author=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='author')

    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('notice_list')
