# Generated by Django 2.0 on 2020-06-13 03:22

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20200607_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strpic',
            name='link_name',
        ),
        migrations.RemoveField(
            model_name='strpic',
            name='link_qrcode',
        ),
        migrations.AlterField(
            model_name='strpic',
            name='qrcode',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='upload_qrcode', verbose_name='上传二维码'),
        ),
    ]