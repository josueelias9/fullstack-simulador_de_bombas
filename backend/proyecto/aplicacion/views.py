from json import loads
from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Geometria

# Create your views here.

class Vista(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        listGet=list(Geometria.objects.values())
        return JsonResponse(listGet,safe=False)

    def post(self,request):
        dictEntrada = loads(request.body)
        Geometria.objects.create(nombre=dictEntrada['nombre'], coordenadas= dictEntrada['coordenadas'])
        respuesta = {
            "mensaje": "Todo bien!"
        }
        return JsonResponse(respuesta)