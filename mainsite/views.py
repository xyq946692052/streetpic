
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
    upload_qrcode = request.FILES.get('qrcode', None)
    background = request.POST.get('background', None)

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    if link_url:
        gen_qrcode_img = qrcode.make(link_url)
        gen_qrcode_name = os.path.join(settings.MEDIA_ROOT, 'generate_qrcode', link_name+"_"+now).replace('\\', '/')
        with open('%s.png' % gen_qrcode_name, 'wb') as f:
            gen_qrcode_img.save(f)

    if upload_qrcode:
        if upload_qrcode.name.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
            return HttpResponse('上传的文件必须是图片')
    params = {
        'title': title,
        'link_url': link_url,
        'link_name': link_name,
        'qrcode': qrcode,
        'background': background
    }
    #Strpic.objects.create(**params)
    context = dict()
    context['title'] = title
    context['qrcode'] = qrcode
    context['background'] = background
    context['link_url'] = link_url
    context['link_name'] = link_name
    if link_url:
        context['qrcode'] = '/media/generate_qrcode/'+link_name+"_"+now+'.png'
    return render(request, 'result.html', context)