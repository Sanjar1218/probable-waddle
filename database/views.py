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

def get(request):

    phones = Mobile.objects.filter(name__icontains='Apple')
    products_json = []
    for product in phones:
        products_json.append({
            'id': product.id,
            'name': product.name,
            'company': product.company,
            'color': product.color,
            'RAM': product.ram,
            'memory': product.memory,
            'price': product.price,
            'img_url': product.img_url,
            
        })

    return JsonResponse({'products': products_json[:3]})

