from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Strpic(models.Model):
    title = models.CharField(max_length=200, verbose_name="海报内容", null=False)
    link_url = models.CharField(max_length=100, verbose_name="链接", null=True)
    qrcode = ThumbnailerImageField(upload_to='upload_qrcode', verbose_name="上传二维码", null=True)
    background = models.CharField(max_length=50, verbose_name="背景色", default="#1E90FF")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        ordering = ('-id', )

    def __str__(self):
        return self.title
