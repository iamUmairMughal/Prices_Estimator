from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from .cars import *

@api_view(['POST'])
def car_price(query):
    data = json.loads(query.body)
    result = str(predict_price(data))
    if data == "ERROR":
        return JsonResponse('Error', safe=False)
    else:
        return JsonResponse({'price':result}, safe=False)



