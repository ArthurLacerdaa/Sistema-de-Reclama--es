from django.http import JsonResponse
from .models import Reclamacao

def listar_reclamacao(request):
    reclamacao = Reclamacao.objects.all().values()
    return JsonResponse(list(reclamacao), safe=False)


def em_aberto(request):
    reclamacao_aberta = Reclamacao.objects.filter(status='NAO_RESPONDIDA').values()
    return JsonResponse(list(reclamacao_aberta) , safe=False)

def urgente(request):
    reclamacao_urgente = Reclamacao.objects.filter(urgencia='URGENTE').values()
    return JsonResponse(list(reclamacao_urgente) , safe=False)

def nao_urgente(request):
    reclamacao_nao_urgente = Reclamacao.objects.filter(urgencia='NAO_URGENTE').values()
    return JsonResponse(list(reclamacao_nao_urgente) , safe=False)