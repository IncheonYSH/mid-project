from django.shortcuts import render
from .forms import WriteArticleForm
from board.models import Article
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def article(request, article_num):
    article_objects = Article.objects.get(article_number=article_num)
    context = {'article_objects': article_objects}
    return render(request, 'board/article.html', context)

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
