from django import template

from blog.models import Post,Category

register = template.Library()

@register.simple_tag
def hello():
    return 'hello'

@register.inclusion_tag('blog/popular-posts.html')
def popularposts():
    posts = Post.objects.filter(status=1).order_by('published_data')
    return ({'posts':posts})
@register.inclusion_tag('blog/post-category.html')
def postcategories():
    cat_dict={}
    posts = Post.objects.all()
    categories = Category.objects.all()
    
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return ({'categories':cat_dict})  
    
    