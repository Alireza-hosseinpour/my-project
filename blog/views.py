from django.shortcuts import get_object_or_404, render

from blog.models import Post,Category
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def blog(request):
    posts = Post.objects.filter(status=1)
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context = {
        'posts':posts,
        'page_number':page_number
    }
    return render(request,'blog/blog-home.html',context)

def blog_single(request,id):
    posts = Post.objects.filter(status=1)
    post=get_object_or_404(posts,id=id)
    return render(request,'blog/blog-single.html',{'post':post})

def Test(request):
    return render(request,'test.html')

def blog_category(request,pk):

    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__id=pk)
    print(posts)
    context = {
        'posts':posts
    }
    return render(request,'blog/blog-home.html',context)