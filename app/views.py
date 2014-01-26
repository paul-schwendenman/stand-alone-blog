from helpers import render_to_template_json, render_to_json
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Post
import datetime

@render_to_template_json('index.html')
def index(request):
    posts = list(Post.objects.all().values('title', 'body', 'slug'))
    if not posts:
        posts = None    

    return {
        'template': 'index.html',
        'posts': posts,
    }

@render_to_template_json('blog.html')
def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return {
        'template': 'blog.html',
        'title': post.title,
        'body': post.body,
        'created_time': post.created.strftime("%I:%M %p"),
        'created_date': post.created.strftime("%b %d, %Y"),
        'slug': post_slug,
    }

