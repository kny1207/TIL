from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 1:N Relation
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 어떤 table(게시글)에 형성되는지 알기 위한
    """
    Article : Comment = 1 : N
    (부모)     (자식)

    on_delete 옵션
    1. CASCADE - 부모가 삭제되면, 자식도 삭제됨 => 미니 프로젝트에서 많이 사용, 편리해서
    2. PROTECT - 자식이 있으면, 부모 삭제 불가
    3. SET_NULL - 부모가 삭제되면, 자식의 FK에 null 할당 => 가장 많이 사용
    4. SET_DEFAULT - 부모가 삭제되면, 자식의 FK에 default 값 할당
    5. DO_NOTHING - 아무것도 하지 않음 => 데이터 무결성 깨질 수 있어 위험!

    1. Create
    article = Article.objects.get(pk=1)
    comment = Comment()
    comment.content = '첫 댓글입니다!'
    comment.article = article
    (comment.article_id = 1 로도 저장 가능)
    comment.save()

    2. Read

    2-1. 부모로부터 자식들 가져오기
    article = Article.objects.get(pk=1)
    comment = article.comment_set.all() - article에 저장된 모든 댓글 가져옴

    2-2. 자식 테이블에서 조건으로 가져오기
    article = Article.objects.get(pk=1)
    comments = Comment.objects.filter(article=article)
                               filter(article_id=1)

    3. 자식이 부모를 부르기 (N에서 1 불러오기)
    comment = Comment.objects.get(pk=1)
    article = comment.article
    article.title => '안녕'
    article.content => '반가워'
    """