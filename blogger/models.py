from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='post/')
    posting_time=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title