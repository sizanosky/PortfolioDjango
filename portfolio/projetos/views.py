from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,
                  'projetos/index.html')


def projetos(request):
    dic_projetos = {
        'proj_1': 'Weather Around World - usando API',
        'proj_2': "Buscando noticias com API's",
        'proj_3': 'Logando no Facebook - usando Selenium'
    }
    dados_projetos = {
        'nome_projetos': dic_projetos
    }
    return render(request,
                  'projetos/projetos.html', dados_projetos)


def projeto_details(request):
    return render(request,
                  'projetos/projeto_details.html')
