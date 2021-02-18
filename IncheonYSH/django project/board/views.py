from django.shortcuts import render
from .forms import WriteArticleForm
from .forms import CommentForm
from board.models import Article
from board.models import Comment
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

# article list
def index(request):
    page = request.GET.get('page', 1)
    article_list = Article.objects.all().order_by('-article_number')
    paginator = Paginator(article_list, 20)
    page_obj = paginator.get_page(page)
    context = {'article_list': page_obj}
    return render(request, 'board/list.html', context)

# Request article, comment
def article(request, article_num):
    try:
        article_objects = Article.objects.get(article_number=article_num)
    except:
        article_objects = None

    try:
        comment_objects = Comment.objects.filter(article_number=article_num).order_by('comment_number')
    except:
        comment_objects = None

    comment_form = CommentForm()
    context = {
        'article_objects': article_objects,
        'comment_objects': comment_objects,
        'comment_form': comment_form,
    }
    return render(request, 'board/article.html', context)

# Create comment
@login_required(login_url='/accounts/login')
def write_comment(request, article_num):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.username = request.user
        comment.article_number = Article(article_number=article_num)
        comment.save()
    return redirect('board:article', article_num=article_num)

# Delete comment
@login_required(login_url='/accounts/login')
def delete_comment(request, comment_num):
    comment = get_object_or_404(Comment, pk=comment_num)
    if request.user != comment.username:
        messages.error(request, '권한없음')
        return redirect('board:article', article_num=comment.article_number)

    else:
        comment.delete()
    return redirect('board:article', article_num=comment.article_number)

# Create article
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

# Update article
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

# Delete article
@login_required(login_url='/accounts/login')
def delete(request, article_num):
    article = get_object_or_404(Article, pk=article_num)
    if request.user != article.username:
        messages.error(request, '권한없음')
        return redirect('board:article', article_num=article.article_number)
    article.delete()
    return redirect('board:index')

