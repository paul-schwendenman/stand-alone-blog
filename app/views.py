from helpers import render_to_template_json, render_to_json
from django.shortcuts import get_object_or_404
from models import Post

#@render_to_json
@render_to_template_json('index.html')
def index(request):
    posts = list(Post.objects.all().values('title', 'body', 'slug'))
    if not posts:
        posts = None    

    return {
        'body': 'index',
        'posts': posts,
    }

@render_to_json
def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return {
        'title': post.title,
        'body': post.body,
        'created': str(post.created),
        'slug': post_slug,
    }

