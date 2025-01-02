from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    body = template.render(context)
    return render(request, 'blogging/list.html', context)


def detail_view(request,post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    #render completes template loading, creating context, generating page body, and making HTTP response at once
    return render(request, 'blogging/detail.html', context)