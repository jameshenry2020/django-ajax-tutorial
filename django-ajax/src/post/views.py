from django.shortcuts import render
from post.models import Article,Like
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Article.objects.all()
    context={
        'posts':posts
    }
    return render(request, 'post/index.html', context)

def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Article.objects.get(id = post_id )
        m = Like(post=likedpost) 
        m.save()
        likedpost.likecount= + 1
        likedpost.save() 
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")