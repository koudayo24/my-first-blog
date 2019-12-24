from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #models.ForeignKeyは他のモデルへのリンク
    title = models.CharField(max_length=200) #models.ChartFieldは文字数が制限されたテキストを定義する
    text = models.TextField() #models.TextFieldは文字数制限なし
    created_data = models.DateTimeField(default=timezone.now)
    published_data = models.DateTimeField(blank=True, null=True)

#ブログを投稿するメソッド
    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title
