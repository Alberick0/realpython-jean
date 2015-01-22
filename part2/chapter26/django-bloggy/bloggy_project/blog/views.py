from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import Context, loader, RequestContext
from blog.models import Post
from blog.forms import PostForm

# Create your views here.
########################
### helper functions ###
########################
def get_popular_posts():
    return Post.objects.order_by('views')[:5]

######################
### view functions ###
######################
def index(request):
    latest_posts = Post.objects.all().order_by('-created_at')
    t = loader.get_template('blog/index.html')
    context_dict = {'latest_posts': latest_posts, 'popular_posts': get_popular_posts()}
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def post(request, slug):
    single_post = get_object_or_404(Post, slug=slug)
    single_post.views += 1  # used to increment the number of views
    single_post.save()  # saves the increment
    t = loader.get_template('blog/post.html')
    context_dict = {'single_post': single_post, 'popular_posts': get_popular_posts()}
    c = Context(context_dict)
    return HttpResponse(t.render(c))


def add_post(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  # this is going to check if the form values are valid
            form.save(commit=True)  # if valid save to DB
            new_post = Post.objects.filter(title=form.cleaned_data['title']).order_by('-created_at')[:1]
            return post(request, new_post[0].slug)
            # return redirect(index)
        else:
            print form.errors  # displays the errors on the form
    else:
        form = PostForm()
    return render_to_response('blog/add_post.html', {'form':form}, context)