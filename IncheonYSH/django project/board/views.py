from django.shortcuts import render
from .forms import WriteArticleForm
from board.models import Article
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

def article(request, article_num):
    article_objects = Article.objects.get(article_number=article_num)
    context = {'article_objects': article_objects}
    return render(request, 'board/article.html', context)

def index(request):
    page = request.GET.get('page', 1)
    article_list = Article.objects.all().order_by('-article_number')
    paginator = Paginator(article_list, 20)
    page_obj = paginator.get_page(page)
    context = {'article_list': page_obj}
    return render(request, 'board/list.html', context)

@login_required(login_url='/accounts/login')
def write(request):
    if request.method == 'POST':
        form = WriteArticleForm(request.POST)
        if form.is_valid():
            article_write = form.save(commit=False)
            article_write.username = request.user
            article_write.save()
            return redirect('/board')
    else:
        form = WriteArticleForm()
    return render(request, 'board/write.html', {"form": form})

@login_required(login_url='/accounts/login')
def modify(request, article_num):
    article = get_object_or_404(Article, pk=article_num)
    if request.user != article.username:
        messages.error(request, '권한없음')
        return redirect('board:article', article_num=article.article_number)

    if request.method == "POST":
        form = WriteArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.username = request.user
            article.save()
            return redirect('board:article', article_num=article.article_number)

    else:
        form = WriteArticleForm(instance=article)
    context = {'form': form}
    return render(request, 'board/modify.html', context)

@login_required(login_url='/accounts/login')
def delete(request, article_num):
    article = get_object_or_404(Article, pk=article_num)
    if request.user != article.username:
        messages.error(request, '권한없음')
        return redirect('board:article', article_num=article.article_number)
    article.delete()
    return redirect('board:index')
