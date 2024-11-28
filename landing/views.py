import requests

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from landing.models import SubmittedOrder


def index(request):
    return render(request, 'landing/index.html')


@csrf_exempt
def submit_order(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")

        if SubmittedOrder.objects.filter(phone=phone).exists() or SubmittedOrder.objects.filter(name=name).exists():
            return JsonResponse(
                {"error": "Вы уже отправляли заявку с этим номером телефона или именем"},
                status=400,
                json_dumps_params={'ensure_ascii': False}
            )

        payload = {
            "stream_code": settings.STREAM_CODE,
            "client": {
                "phone": phone,
                "name": name,
            },
        }

        response = requests.post(settings.API_URL, json=payload, headers=settings.HEADERS)

        if response.status_code == 200:
            SubmittedOrder.objects.create(name=name, phone=phone)
            return redirect('landing:thank_you')
        else:
            return JsonResponse({"error": "Ошибка отправки данных"}, status=500)

    return JsonResponse({"error": "Неверный метод запроса"}, status=405)


def thank_you(request):
    return render(request, 'landing/thank_you.html')
