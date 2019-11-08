from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, Http404
import json
import daemon.transformar.transformar_glc as transformar_glc
import daemon.analisador.analiser as analiser


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

        objetos_tratados = transform.tratar_objeto(object_from_view)
        analisador = analiser.Analiser()
        first_list = analisador.create_first(objetos_tratados)
        follow_list = analisador.create_follow(objetos_tratados)
        acoes = analisador.criar_acoes(objetos_tratados, first_list, follow_list)
        tabela = analisador.preencher_tabela(acoes)
        response_data.update({"tabela": tabela, "first": first_list, "follow": follow_list, "acoes": acoes})
        print(response_data)
        return HttpResponse(
            json.dumps(response_data)
        )
    else:
        raise Http404

