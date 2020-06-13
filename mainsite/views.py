
import os
import qrcode
from easy_thumbnails.files import get_thumbnailer
from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse,reverse
from .models import Strpic

def index(request):
    context = {}
    return render(request, 'index.html', context)


def generate_pic(request):

    title = request.POST.get('title', None)
    link_url = request.POST.get('link_url', None)
    upload_qrcode = request.FILES.get('upload_qrcode', None)
    background = request.POST.get('background', None)

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    if link_url:
        gen_qrcode_img = qrcode.make(link_url)
        gen_qrcode_name = os.path.join(settings.MEDIA_ROOT, 'generate_qrcode', title[:5]+ "_"+now).replace('\\', '/')
        with open('%s.png' % gen_qrcode_name, 'wb') as f:
            gen_qrcode_img.save(f)

    if upload_qrcode:
        upload_qrcode_name = now+"_"+upload_qrcode.name
        upload_path = 'media/upload_qrcode/' +upload_qrcode_name
        with open(upload_path, 'wb') as f:
            for line in upload_qrcode.chunks():
                f.write(line)
        if upload_qrcode.name.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
            return HttpResponse('上传的文件必须是图片')

    params = {
        'title': title,
        'link_url': link_url,
        'qrcode': upload_qrcode,
        'background': background
    }
    Strpic.objects.create(**params)

    obj = Strpic.objects.all().first()



    context = dict()
    context['title'] = obj.title[:45] if obj.title else None
    context['background'] = obj.background

    if upload_qrcode:
        path = get_thumbnailer(obj.qrcode)['avatar'].url
        context['prompt'] = '长按或扫一扫进行付款'
        context['qrcode'] = path

    if link_url:
        context['link_url'] = obj.link_url[:50]
        context['prompt'] = '长按识别二维码打开链接'
        context['qrcode'] = '/media/generate_qrcode/'+obj.title[:5]+"_"+now+'.png'
    print('--------------',now, context['qrcode'])
    return render(request, 'result.html', context)