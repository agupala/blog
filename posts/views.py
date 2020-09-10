from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    # posts = Post.objects.all()
    posts = Post.objects.order_by('-created').filter(is_published=True)
    post_number = Post.objects.all().count()
    print(f"Cantidad de posts: {post_number}")
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts': paged_posts,
    }
    return render(request, "posts/home.html", context)

def get_prev(post):
    qs = Post.objects.filter(id__lt=post.id, is_published=True).order_by('-created')
    if qs.exists():
        return qs.first()
    return None

def get_next(post):
    qs = Post.objects.filter(id__gt=post.id, is_published=True).order_by('created')
    if qs.exists():
        return qs.first()
    return None

def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    posts = Post.objects.filter(is_published=True).order_by('-created')
    
    next = get_next(post)
    prev = get_prev(post)

    print(f"Actual: {post}")
    print(f"Prev: {prev}")
    print(f"Next: {next}")

    context = {
        'post': post,
        'previous': prev,
        'next': next,
    }

    return render(request, "posts/post.html", context)
