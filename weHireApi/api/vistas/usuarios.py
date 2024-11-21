import json
from django.http.response import JsonResponse
from django.views import View
from ..models import Usuarios
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class UsuariosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, id=0):
        if(id>0):
            usuarios= list(Usuarios.objects.filter(id=id).values())
            if len(usuarios)>0:
                usuario = usuarios[0]
                datos= {'message': "Success",'usuarios': usuario}
            else:  
                datos={'message': "no hay usuarios"}
            return JsonResponse(datos)
        else:
            usuarios = list(Usuarios.objects.values())
            if len(usuarios)>0:
                datos= {'message': "Success","usuarios":usuarios}
            else:
                datos= {'message': "Usuario  no encontrado"}
            return JsonResponse(datos)
        
    def post(self,request):
        #print(request.body)
        jd=json.loads(request.body)
       # print(jd)
        Usuarios.objects.create(nombre=jd['nombre'],correo=jd['correo'],clave=jd['clave'])
        datos= {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self,request,id):
        jd=json.loads(request.body)
        usuarios= list(Usuarios.objects.filter(id=id).values())
        if len(usuarios)>0:
            usuario =Usuarios.objects.get(id=id)
            usuario.nombre=jd['nombre']
            usuario.correo=jd['correo']
            usuario.clave=jd['clave']
            usuario.save()
            datos= {'message': "Success"}
        else:
            datos= {'message': "Usuario  no encontrado"}
        return JsonResponse(datos)
        
    def delete(self,request):
        pass