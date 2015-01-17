from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.template import Context, loader
from blog.models import Post

# Create your views here.
def encode_url(posts):
    for post in posts:
        post.url = post.title.replace(' ', '_')
    return posts

def index(request):
    latest_posts = encode_url(Post.objects.all().order_by('-created_at'))
    popular_posts = encode_url(Post.objects.all().order_by('-views')[:5])
    t = loader.get_template('blog/index.html')
    context_dict = {'latest_posts': latest_posts, 'popular_posts': popular_posts}
    c = Context(context_dict)
    return HttpResponse(t.render(c))

def post(request, slug):
    single_post = get_object_or_404(Post, title=slug.replace('_', ' '))
    popular_posts = encode_url(Post.objects.all().order_by('-views')[:5])
    single_post.views += 1  # used to increment the number of views
    single_post.save()  # saves the increment
    t = loader.get_template('blog/post.html')
    c = Context({'single_post': single_post, 'popular_posts': popular_posts })
    return HttpResponse(t.render(c))
