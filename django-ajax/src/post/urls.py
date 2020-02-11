from django.urls import path
from post.views import index, like


urlpatterns = [
   path('', index, name='article-list'),
path('like/',like, name='like'),
  
]