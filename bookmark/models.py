from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    class Meta:
        #해당 모델에 대한 옵션 값
        #정렬, 출력될 모델 이름
        ordering = ['site_name']

    #print 함수를 사용해서 객체를 출력할 때 출력될 내용을 반환하는 함수
    #장고가 이걸 응용해서 화면에 객체를 html로 출력할 때 내용을 반환하는 함수
    def __str__(self):
        return self.site_name+ " : "+self.url

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bookmark:detail', args=[str(self.id)])
