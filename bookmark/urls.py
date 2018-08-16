from django.urls import path
from .views import *

app_name = 'bookmark'
urlpatterns = [
    # list, write, update, delete
    # 함수형부 : 함수이름만
    # 플래스형뷰 : 클래스이름.as_view()
    path('',BookmarkLV.as_view(), name='index'),
    path('add/', BookmarkCV.as_view(), name='create'),
    #<1:2> : 1. data type, 2. data name
    path('update/<int:pk>', BookmarkUV.as_view(), name='update'),
    path('detail/<int:pk>', BookmarkDetailV.as_view(), name='detail'),
    path('delete/<int:pk>', BookmarkDeleteV.as_view(), name='delete'),
]
