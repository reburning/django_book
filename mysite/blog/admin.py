__author__ = 'root'
from django.contrib import admin
from mysite.blog.models import BlogPost, BlogPostAdmin

admin.site.register(BlogPost, BlogPostAdmin)