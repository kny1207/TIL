from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings 

# Create your models here.
class Profile(models.Model):
    nickname = models.CharField(max_length=20, blank=True)
    image = ProcessedImageField(
                            blank = True, 
                            upload_to='profile/image/', # 이미지 업로드 장소 정해줌
                            processors = [Thumbnail(300,300),],
                            format = 'png',
                            )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
