import json
from django.http.response import JsonResponse
from django.views import View
from ..models import EtapaMedia,Usuarios,Publicaciones
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class EstapaMediaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, id=0):
        if(id>0):
            etapaMedia= list(EtapaMedia.objects.filter(id=id).values())
            if len(etapaMedia)>0:
                etapaMedia= etapaMedia[0]
                datos= {'message': "Success",'etapa media': etapaMedia}
            else:  
                datos={'message': "no hay etapas"}
            return JsonResponse(datos)
        else:
            etapasMedias = list(EtapaMedia.objects.values())
            if len(etapasMedias)>0:
                datos= {'message': "Success","etapa media":etapasMedias}
            else:
                datos= {'message': "etapas  no encontradas"}
            return JsonResponse(datos)
   
    def post(self, request):
            jd = json.loads(request.body)
            
            usuario = None
            publicacion = None
          
            usuario = Usuarios.objects.get(id=jd['usuario_id']) 
            publicacion = Publicaciones.objects.get(id=jd['publicacion_id'])
         
            EtapaMedia.objects.create(
                estado=jd['estado'],  
                observaciones=jd['observaciones'],
                usuario=usuario,
                publicacion=publicacion
            )
            
            return JsonResponse({'message': 'Success'}, status=201)
        
    def put(self,request,id):
        jd=json.loads(request.body)
        etapaMedia= list(EtapaMedia.objects.filter(id=id).values())
        if len(etapaMedia)>0:
            etapaMedia =EtapaMedia.objects.get(id=id)
            etapaMedia.estado=jd['estado']
            etapaMedia.observaciones=jd['observaciones']
            etapaMedia.archivo=jd['archivo']
            etapaMedia.save()
            datos= {'message': "Success"}
        else:
            datos= {'message': "Etapa  no encontrada"}
        return JsonResponse(datos)
        
    def delete(self,request):
        pass
