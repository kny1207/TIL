from django import forms
from .models import Article

# model과 연계하기 쉬운 form 생성
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)

# 장고에서 정하고 있는 forms로 form tag 만들어주기 
# => views.py의 new함수에서 양식보여주기
# class ArticleForm(forms.Form):
#     title = forms.CharField(
#                     max_length = 10,
#                     label = '제목',
#                     widget = forms.TextInput(
#                         attrs={
#                             'class': 'title',
#                             'placeholder': '제목을 입력하세요.'
#                         }
#                     )
#                     )
#     content = forms.CharField(
#                     label = '내용',
#                     widget = forms.Textarea(
#                         attrs={
#                             'class':'content',
#                             'rows': 5,
#                             'cols': 20,
#                         }
#                     )        
#                 )   
    