from django.urls import path
from .vistas.usuarios import UsuariosView
from .vistas.publicaciones import PublicacionesView
from .vistas.etapaInicial import EstapaInicialView
from .vistas.etapaMedia import EstapaMediaView
from .vistas.etapaFinal import EstapaFinalView
from .views import listar_publicaciones
#PublicacionesView

urlpatterns =[
    path('usuarios/', UsuariosView.as_view(),name='usuarios_listar'),
    path('usuarios/<int:id>', UsuariosView.as_view(),name='usuarios_listar_id'),
    path('publicaciones/', PublicacionesView.as_view(),name='publicaciones_listar'),    
    path('publicaciones/<int:id>', PublicacionesView.as_view(),name='publicaciones_listar_id'),
    path('etapaInicial/', EstapaInicialView.as_view(),name='etapa_inicial_listar'),    
    path('etapaInicial/<int:id>', EstapaInicialView.as_view(),name='etapa_inicial_listar_id'),
    path('etapaMedia/', EstapaMediaView.as_view(),name='etapa_media_listar'),    
    path('etapaMedia/<int:id>', EstapaMediaView.as_view(),name='etapa_media_listar_id'),
    path('etapaFinal/', EstapaFinalView.as_view(),name='etapa_final_listar'),    
    path('etapaFinal/<int:id>', EstapaFinalView.as_view(),name='etapa_final_listar_id'),
    path('publicacionesXusuario/<int:id>/', listar_publicaciones, name='publicaciones_listar_por_usuario'),

]

