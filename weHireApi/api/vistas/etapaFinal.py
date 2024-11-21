import json
from django.http.response import JsonResponse
from django.views import View
from ..models import EtapaFinal
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class EstapaFinalView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, id=0):
        if(id>0):
            etapafinal= list(EtapaFinal.objects.filter(id=id).values())
            if len(etapafinal)>0:
                etapafinal= etapafinal[0]
                datos= {'message': "Success",'publicaciones': etapafinal}
            else:  
                datos={'message': "no hay publicaciones"}
            return JsonResponse(datos)
        else:
            etapasFinales = list(EtapaFinal.objects.values())
            if len(etapasFinales)>0:
                datos= {'message': "Success","publicaciones":etapasFinales}
            else:
                datos= {'message': "publicacion  no encontrado"}
            return JsonResponse(datos)
   
    def post(self,request):
        #print(request.body)
        jd=json.loads(request.body)
       # print(jd)
        EtapaFinal.objects.create(estado=jd['estado'],observaciones=jd['observaciones'],archivo=jd['archivo'],retroalimentacion=jd['retroalimentacion'])
        datos= {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self,request,id):
        jd=json.loads(request.body)
        etapaFinal= list(EtapaFinal.objects.filter(id=id).values())
        if len(etapaFinal)>0:
            etapaFinal =EtapaFinal.objects.get(id=id)
            etapaFinal.estado=jd['estado']
            etapaFinal.observaciones=jd['observaciones']
            etapaFinal.archivo=jd['archivo']
            etapaFinal.retroalimentacion=jd['retroalimentacion']
            etapaFinal.save()
            datos= {'message': "Success"}
        else:
            datos= {'message': "Usuario  no encontrado"}
        return JsonResponse(datos)
        
    def delete(self,request):
        pass