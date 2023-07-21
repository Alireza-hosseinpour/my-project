from django.contrib import admin
from .models import Post,Category
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    list_display=('title','created_at','status','published_data','author')
    list_filter=('created_at',)
    search_fields=('title','status')
    date_hierarchy='created_at'
    summernote_fields= ('content',)
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category)