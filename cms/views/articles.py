from django.shortcuts import get_object_or_404
from ..models import Article
from django.http import HttpResponseRedirect
from ..forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def send_notification(message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            "type": "send_notification",
            "message": message,
        },
    )

@login_required
def add_article_view(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            send_notification(f'New article "{article.title}" has been added.')
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'add_article.html', {'form': form})

@login_required
def edit_article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {'form': form})

def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

def article_list_view(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

@login_required
def remove_article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'confirm_delete.html', {'article': article})
