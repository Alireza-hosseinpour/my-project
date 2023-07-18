from django.shortcuts import get_object_or_404, render

from blog.models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.filter(status=1)
    context = {
        'posts':posts
    }
    return render(request,'blog/blog-home.html',context)

def blog_single(request,id):
    posts = Post.objects.filter(status=1)
    post=get_object_or_404(posts,id=id)
    return render(request,'blog/blog-single.html',{'post':post})