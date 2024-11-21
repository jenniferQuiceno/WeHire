import json
from django.http.response import JsonResponse
from django.views import View
from ..models import EtapaInicial,Usuarios,Publicaciones
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


class EstapaInicialView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, id=0):
        if(id>0):
            etapaInicial= list(EtapaInicial.objects.filter(id=id).values())
            if len(etapaInicial)>0:
                etapaInicial= etapaInicial[0]
                datos= {'message': "Success",'estapá inicial': etapaInicial}
            else:  
                datos={'message': "no hay estapá inicial"}
            return JsonResponse(datos)
        else:
            etapasIniciales = list(EtapaInicial.objects.values())
            if len(etapasIniciales)>0:
                datos= {'message': "Success","estapá inicial":etapasIniciales}
            else:
                datos= {'message': "publicacion  no encontrado"}
            return JsonResponse(datos)
   
    def post(self, request):
            jd = json.loads(request.body)
            
            usuario = None
            publicacion = None
          
            usuario = Usuarios.objects.get(id=jd['usuario_id']) 
            publicacion = Publicaciones.objects.get(id=jd['publicacion_id'])  # Asume que 'publicacion_id' está en el JSON
         
            EtapaInicial.objects.create(
                estado=jd['estado'],  
                observaciones=jd['observaciones'],
                usuario=usuario,
                publicacion=publicacion
            )
            
            return JsonResponse({'message': 'Success'}, status=201)
        
    def put(self,request,id):
        jd=json.loads(request.body)
        etapaInicial= list(EtapaInicial.objects.filter(id=id).values())
        if len(etapaInicial)>0:
            etapaInicial =EtapaInicial.objects.get(id=id)
            etapaInicial.estado=jd['estado']
            etapaInicial.observaciones=jd['observaciones']
            etapaInicial.save()
            datos= {'message': "Success"}
        else:
            datos= {'message': "Etapa  no encontrada"}
        return JsonResponse(datos)
        
    def delete(self,request):
        pass