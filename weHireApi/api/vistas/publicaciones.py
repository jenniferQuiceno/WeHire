import json
from django.http.response import JsonResponse
from django.views import View
from ..models import Publicaciones
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class PublicacionesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, id=0):
        if(id>0):
            publicaciones= list(Publicaciones.objects.filter(id=id).values())
            if len(publicaciones)>0:
                publicacion= publicaciones[0]
                datos= {'message': "Success",'publicaciones': publicacion}
            else:  
                datos={'message': "no hay publicaciones"}
            return JsonResponse(datos)
        else:
            publicaciones = list(Publicaciones.objects.values())
            if len(publicaciones)>0:
                datos= {'message': "Success","publicaciones":publicaciones}
            else:
                datos= {'message': "publicacion  no encontrado"}
            return JsonResponse(datos)
   
    def post(self,request):
        #print(request.body)
        jd=json.loads(request.body)
       # print(jd)
        Publicaciones.objects.create(titulo=jd['titulo'],descripcion=jd['descripcion'],salario=jd['salario'],requisitos=jd['requisitos'],estado=jd['estado'],reclutador_id=jd['reclutador_id'])
        datos= {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self,request,id):
        jd=json.loads(request.body)
        publicacion= list(Publicaciones.objects.filter(id=id).values())
        if len(publicacion)>0:
            publicacion =Publicaciones.objects.get(id=id)
            publicacion.titulo=jd['titulo']
            publicacion.descripcion=jd['descripcion']
            publicacion.salario=jd['salario']
            publicacion.requisitos=jd['requisitos']
            publicacion.estado=jd['estado']
            publicacion.save()
            datos= {'message': "Success"}
        else:
            datos= {'message': "Usuario  no encontrado"}
        return JsonResponse(datos)
        
    def delete(self,request):
        pass