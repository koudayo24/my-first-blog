from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
"""
見てのとおり、post_list という名前の ビュー をルートURLに割り当てています。 
このURLパターンは空の文字列に一致します。
Djangoはビューを見つけるとき、
URLのパス(path)の前にくっつくドメイン名（つまり、http://127.0.0.1:8000/ の部分）
を無視します。 
このパターンは誰かがあなたのWebサイトの 'http://127.0.0.1:8000/' というアドレスにアクセスしてきたら
 views.post_list が正しい行き先だということをDjangoに伝えます
 """