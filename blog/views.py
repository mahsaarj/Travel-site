from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        posts = posts.filter(author__username = kwargs['author_username'])
    context={'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def test(request):
    return render(request, 'test.html')

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == "GET":
        #print(request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains= s)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)