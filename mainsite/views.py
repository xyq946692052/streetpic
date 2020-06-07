
import os
import qrcode
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
    link_name = request.POST.get('link_name', None)
    upload_qrcode = request.FILES.get('upload_qrcode', None)
    background = request.POST.get('background', None)

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    if link_url:
        gen_qrcode_img = qrcode.make(link_url)
        gen_qrcode_name = os.path.join(settings.MEDIA_ROOT, 'generate_qrcode', link_name+"_"+now).replace('\\', '/')
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

    context = dict()
    context['title'] = title[:26] if title else None
    context['background'] = background

    if upload_qrcode:
        context['prompt'] = '长按或扫一扫进行付款'
        context['qrcode'] = '/media/upload_qrcode/' + upload_qrcode_name

    if link_url:
        context['link_url'] = link_url[:50]
        context['link_name'] = link_name
        context['prompt'] = '长按识别二维码打开链接'
        context['qrcode'] = '/media/generate_qrcode/'+link_name+"_"+now+'.png'
    return render(request, 'result.html', context)