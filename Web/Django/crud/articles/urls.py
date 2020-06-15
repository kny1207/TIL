from django.urls import path
from . import views

app_name = 'articles'

# 모든 주소 일괄적으로 여기서 관리 가능
urlpatterns = [
    # 1. GET /articles/ 
    path('', views.index, name='index'), # 게시글 목록
    # 2. GET /articles/new/
    path('new/', views.new, name='new'), # 게시글 작성 양식 (GET)
    # 3. POST /articles/new/
    # path('create/', views.create, name='create'), # 게시글 생성! (POST)
    # 4. GET /articles/1/
    path('<int:pk>/', views.detail, name='detail'), # <int:pk> 는 동적인 부분
    # 5. POST /articles/1/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),
    # 6. GET /articles/1/edit/
    path('<int:pk>/edit/', views.edit, name='edit'), # 게시글 수정 양식 (GET)
    # 7. PUT, PATCH /articles/1/edit
    # path('update/<int:pk>/', views.update, name='update'), # 게시글 수정! (POST)
]