from helpers import render_to_template_json, render_to_json, render_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Post
from forms import PostForm
import datetime
import re

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
def view_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return {
        'template': 'blog.html',
        'title': post.title,
        'body': post.body,
        'created_time': post.created.strftime("%I:%M %p"),
        'created_date': post.created.strftime("%b %d, %Y"),
        'slug': post_slug,
    }

@render_to_template('form.html')
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            body = re.sub('\n', '<br>\n', body)
            Post(body=body, title=title).save()

            return HttpResponseRedirect('/')
    else:
        form = PostForm()

    response_data = {
        'form': form,
    }

    return response_data
