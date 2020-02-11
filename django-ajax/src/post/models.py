from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    post =models.TextField()
    author=models.CharField(max_length=60)
    likecount=models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Article, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.post.title