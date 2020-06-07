
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
    code_img = request.FILES.get('code_img', None)
    file_name = ''
    if code_img:
        file_name = code_img
        if code_img.name.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
            return HttpResponse('输入文件有误')
    params = {
        'title': title,
        'pic_url': file_name
    }
    Strpic.objects.create(**params)
    context = dict()
    context['title'] = title
    context['code_img'] = code_img
    return render(request, 'result.html', context)