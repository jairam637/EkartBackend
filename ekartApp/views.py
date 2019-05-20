from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import csv
import reverse_geocoder as rg 
import pprint 
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def items(request):
    
    # with open('Ekart.xlsx','r', encoding="ascii", errors="surrogateescape")as f:
    #     data = csv.reader(f)
    #     for row in data:
    #             print(row)
    reader = csv.DictReader(open("Ekart.csv"))
    data = []
    if reader:
        for raw in reader:
            data.append(raw)
    return JsonResponse({'data': data})

@csrf_exempt
def location(request):
        lattitude = json.loads(request.body.decode("utf-8"))['lat']
        longitude = json.loads(request.body.decode("utf-8"))['lon']
        result = rg.search((lattitude, longitude)) 
      
    # result is a list containing ordered dictionary. 
        pprint.pprint(result)
        return JsonResponse({'data': result})