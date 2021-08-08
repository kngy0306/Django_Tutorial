from django.urls import path
from . import views

# URLパターンを逆引きできるように名前をつける
app_name = 'photo'

# URLパターンを登録するための変数
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
