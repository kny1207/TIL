from django.db import models

# Create your models here.
# 데이터베이스 테이블 생성
class Article(models.Model): 
    # models.Model는 Django가 만들어놓은 기능으로 DB와 연동 가능하게 해줌
    # id = models.AutoField(primary_key=True) - Model에서 알아서 생성해줘서 생략
    title = models.CharField(max_length=100) # CharField는 길이제한 가지는 필드
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 날짜, 시간 저장하는 필드
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self): # f-string: 문자열 합쳐주는 기능
        return f'{self.id}번 글 - {self.title} : {self.content}'

# 1. models.py 작성 및 변경(생성 및 수정)
# 2. python manage.py makemigrations
#    -> migration(설계도) 파일 생성
# 3. python manage.py migrate
#    -> 실제 Database에 적용 (테이블 생성)
