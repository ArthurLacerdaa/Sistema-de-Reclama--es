from django.urls import path
from .views import listar_reclamacao
from .views import em_aberto
from .views import urgente
from .views import nao_urgente

urlpatterns = [
    path('reclamacoes/' , listar_reclamacao),
    path('reclamacoes/abertas' , em_aberto),
    path('reclamacoes/urgentes' , urgente),
    path('reclamacoes/nao_urgentes' , nao_urgente)    
]