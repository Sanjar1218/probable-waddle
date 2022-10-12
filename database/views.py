from django.http import JsonResponse
from .models import Mobile

def add(request):
    data = request.POST
    phone = Mobile(
        phone = data.get('phone',''),
        name=data.get('name', ''),
        company = data.get('company', ''),
        color = data.get('color', ''),
        ram = data.get('RAM', ''),
        memory = data.get('price', ''),
        img_url = data.get('img_url', '')
    )
    phone.save()
    return JsonResponse({'status': 'ok'})