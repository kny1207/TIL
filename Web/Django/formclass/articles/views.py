from django.shortcuts import render, redirect
from .models import Article, Comment # Article class 불러오기
from .forms import ArticleForm, CommentForm # forms.py에 작성한 클래스 import
from django.contrib.auth.decorators import login_required

# Create your views here.

# database에 접근해서 article에 있는 database 가져오기 위한 함수
def index(request):
    articles = Article.objects.all() # Article table에 저장된 모든 data 가져와라
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

# 로그인 검증
# login o -> new 함수 실행
# login x -> login 페이지로 보냄
@login_required # 함수를 인자로 받는 메소드

# data 입력받아서 저장하는 로직 작성
def new(request):

    if request.method == 'POST':

        # Database에 저장

        # 1. 요청에 실려온 data 꺼내오기

        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # image = request.FILES.get('image')

        # django form에서 정의한 class로 data 가져오기
        form = ArticleForm(request.POST, request.FILES)

        # 2-1. data 유효성 검사 - form class 기능
        if form.is_valid():
            # (ModelForm) 2-2. Database에 저장 
            article = form.save(commit=False) # 밑에 2-2 + 2-3 한번에 해결
            article.user = request.user
            # article.user_id = request.user.pk
            article.save()
            # # 2-2. 검증된 data 꺼내오기
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # # 2-3. Database에 저장
            # article = Article(title=title, content=content)
            # article.save() # database에 저장

            # 3. 저장된 data를 확인할 수 있는 곳으로 안내 - index page에서 확인 가능, index주소로 보냄
            return redirect('articles:detail', article.pk)

    else: # GET
        # 작성 양식 보여주기
        form = ArticleForm()
    context = {
        'form' : form,
    } 
    return render(request, 'articles/new.html', context)

def detail(request, pk):
    # Database에서 data 가져오기
    article = Article.objects.get(pk=pk)

    # 댓글 작성 양식 가져오기
    comment_form = CommentForm()

    context = {
        'article':article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def delete(request, pk): # POST
    article = Article.objects.get(pk=pk)


    
    if request.method == 'POST': # 요청방식이 POST일때만
        article.delete()
    return redirect('articles:index')

@login_required
def edit(request, pk):
    # 1. Database에서 data 가져오기
    article = Article.objects.get(pk=pk)

    if request.user != article.user:
        return redirect('articles:detail', article.pk)

    if request.method == 'POST':
        # data 수정!
        # (ModelForm) 2-1. form에 data 집어넣기 + instance와 연결
        form = ArticleForm(request.POST, instance=article)
        # # 2-1. form에 data 집어넣기(검증 목적)
        # form = ArticleForm(request.POST) # 새롭게 넘어온 수정된 data
        # 2-2. form에서 data 유효성 검사
        if form.is_valid():
            # (ModelForm) 2-3. Database에 저장
            article = form.save()
            # # 2-3. 검증된 data를 반영하기(저장)
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            # 3. 저장된 내용을 확인할 수 있는 페이지로 안내
            return redirect('articles:detail', article.pk)

    else: # GET 요청 들어올 때
        # 수정 양식 보여주기!  
        # (ModelForm) 2. Form에 data 채워 넣기
        form = ArticleForm(instance=article) 
        # # 2. Form에 data 채워 넣기
        # form = ArticleForm(initial=article.__dict__) # article의 title:content처럼 초기화
        context = {
            'form': form,
        }
    return render(request, 'articles/edit.html', context)

@login_required
def comments_new(request, article_pk): # POST
    # 1. 요청이 POST인지 점검
    if request.method == 'POST':
        # 2. form에 data를 집어넣기 - 유효성 검사 목적
        # request.POST #=> { 'content': '와 댓글!' }
        form = CommentForm(request.POST)
        # 3. 유효성 검사를 시행
        if form.is_valid():
            # 4. 통과하면 database에 저장(?)
            comment = form.save(commit=False) # database에 일단 기록 X, instance만 만들어오도록
            # 4-1. article 정보 주입
            comment.article_id = article_pk
            # 4-2. user 정보 넣기
            comment.user = request.user
            comment.save()
     # 5. 생성된 댓글을 확인할 수 있는 곳으로 안내
    return redirect('articles:detail', article_pk)

@login_required
def comments_delete(request, article_pk, pk): # POST # urls주소에 정의한 순서대로
    # 0. 요청이 POST인지 점검
    
    # 1. pk를 가지고 삭제하려는 data 꺼내오기
    comment = Comment.objects.get(pk=pk)

    def delete(request, pk): # POST
        article = Article.objects.get(pk=pk)

    if request.user != comment.user:
        return redirect('articles:detail', comment.article.pk)

    if request.method == 'POST':    
        # 2. 삭제!
        comment.delete()

    # 3. 삭제되었는지 확인 가능한 곳으로 안내
    return redirect('articles:detail', article_pk)

@login_required
def comments_edit(request, article_pk, pk): # GET, POST
    # Database에서 수정하려 하는 data 가져오기
    comment = Comment.objects.get(pk=pk)

    if request.user != comment.user:
        return redirect('articles:detail', comment.article.pk)

    # 0. 요청의 종류가 POST인지 GET인지 점검
    if request.method == 'POST':
        # 실제로 수정!
        # 1. form에 '넘어온 data' & '수정하려는 data' 집어넣기
        form = CommentForm(request.POST, instance=comment)
        # 2. 유효성 검사
        if form.is_valid():
            # 3. 검사를 통과했다면, save
            comment = form.save()
            # 4. 변경된 결과 확인하는 곳으로 안내
            return redirect('articles:detail', article_pk)
    else:
        # 수정 양식 보여주기!
        # 1. form class 초기화(생성)
        form = CommentForm(instance=comment)

    context = {
        'form':form,
    }
    return render(request, 'articles/comments_edit.html', context)
