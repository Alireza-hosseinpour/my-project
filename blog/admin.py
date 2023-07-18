from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=('title','created_at','status','published_data')
    list_filter=('created_at',)
    search_fields=('title','status')
    date_hierarchy='created_at'
    
admin.site.register(Post,PostAdmin)