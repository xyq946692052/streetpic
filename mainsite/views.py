
import os
from datetime import datetime
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
    qrcode = request.FILES.get('qrcode', None)
    background = request.POST.get('background', None)
    if qrcode:
        if qrcode.name.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
            return HttpResponse('上传的文件必须是图片')
    params = {
        'title': title,
        'link_url': link_url,
        'link_name': link_name,
        'qrcode': qrcode,
        'background': background
    }
    Strpic.objects.create(**params)
    context = dict()
    context['title'] = title
    context['qrcode'] = qrcode
    context['background'] = background
    context['link_url'] = link_url
    context['link_name'] = link_name
    return render(request, 'result.html', context)