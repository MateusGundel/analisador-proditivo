from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, Http404
import json
import daemon.reconhecedor.gramatica as gramatica
import daemon.reconhecedor.consistencia as consistencia
import daemon.reconhecedor.sentencas as sentencas
import daemon.transformar.transformar_glc as transformar_glc


# Create your views here.
def home_view(request):
    return render(request, 'web/home.html')


@csrf_exempt
def analisar(request):
    if request.method == 'POST':
        object_from_view = json.loads(request.body)
        response_data = {}
        print(object_from_view)
        transform = transformar_glc.transformation()
        print(transform.recursao_a_esquerda(transform.tratar_objeto(object_from_view)))
        print(response_data)
        return HttpResponse(
            json.dumps(response_data)
        )
    else:
        raise Http404

