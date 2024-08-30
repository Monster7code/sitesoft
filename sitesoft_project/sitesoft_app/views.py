from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json


def get_habr(request):
    habrs = Resource.objects.all()

    habrs_list = list(habrs.values())
    return JsonResponse({
            "name_habr": habrs_list
    })


@csrf_exempt
def check_link(request):
    data = json.loads(request.body)
    link = data.get('link')
    try:
        link = Articles.objects.get(article_link=link)

        return JsonResponse({
            "status": False
        })
    except ObjectDoesNotExist:
        return JsonResponse({
            "status": True
        })


@csrf_exempt
def set_article_on_db(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            name_habr = data.get("resource")
            habr = Resource.objects.get(resource_link=name_habr)

            data["resource"] = habr
            # Создание или обновление записи в базе данных
            resource = Articles(**data)  # Распаковка словаря в модель
            resource.save()  # Сохранение в базе данных
            return JsonResponse({'status': True})
        except:
            return JsonResponse({'status': False})