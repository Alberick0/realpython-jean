from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import Context, loader, RequestContext
from blog.models import Post
from blog.forms import PostForm

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
    c = Context({'single_post': single_post, 'popular_posts': popular_posts})
    return HttpResponse(t.render(c))


def add_post(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  # this is going to check if the form values are valid
            form.save(commit=True)  # if valid save to DB
            return post(request, form.cleaned_data['title'])
        else:
            print form.errors  # displays the errors on the form
    else:
        form = PostForm()
    return render_to_response('blog/add_post.html', {'form':form}, context)