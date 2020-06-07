from django.db import models


class Strpic(models.Model):
    title = models.CharField(max_length=200, verbose_name="海报内容", null=False)
    link_url = models.CharField(max_length=100, verbose_name="链接", null=True)
    link_name = models.CharField(max_length=100, verbose_name="链接名", null=True)
    qrcode = models.ImageField(upload_to='upload', verbose_name="二维码")
    background = models.CharField(max_length=50, verbose_name="背景色", default="#1E90FF")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.title
