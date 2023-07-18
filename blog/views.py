from django.shortcuts import get_object_or_404, render

from blog.models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'blog/blog-home.html',context)

def blog_single(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request,'blog/blog-single.html',{'post':post})