from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import render, HttpResponseRedirect
from .forms import CreatePostForm, EditPostForm
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from users import models as um
from .models import *
import datetime



def index(request):
    return render(request, 'diary/index.html')


def profile(request):
    profile = um.Profile.objects.get(user=request.user)
    context = {
        'profile': profile,
    }

    return render(request, 'diary/profile.html', context=context)


def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            rp = request.POST

            post = Post()
            post.title = rp['title']
            post.text = rp['text']
            post.date = datetime.datetime.now()
            post.owner = request.user
            post.save()
            return HttpResponseRedirect('my_posts')
    else:
        form = CreatePostForm()

    return render(request, 'diary/create_post.html', {'form': form})


def my_posts(request):
    posts = Post.objects.filter(owner=request.user).order_by('-date')

    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    is_paginated = 1

    context = {
        'page_obj': page_obj,
        'is_paginated': is_paginated
    }

    return render(request, 'diary/my_posts.html', context=context)


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('my_posts')


class UpdatePost(UpdateView):
    model = Post
    form = EditPostForm(initial={'is_changed': True})
    fields = ['title', 'text', 'is_changed']
    success_url = reverse_lazy('my_posts')
