from django.db import models

# Create your models here.

BACKCOLOR = (
    ('red', '红色'),
    ('black', '黑色'),
    ('blue', '蓝色')
)


class Strpic(models.Model):
    title = models.CharField(max_length=1000)
    pic_url = models.ImageField(upload_to='upload')
    background = models.CharField(max_length=50, choices=BACKCOLOR)

    def __str__(self):
        return self.title
