from django.shortcuts import render, get_object_or_404

from .models import Projeto


# Create your views here.


def index(request):
    return render(request,
                  'projetos/index.html')


def projetos(request):
    bd_projetos = Projeto.objects.all()  # API Django, Projeto(banco de dados)

    dados_projetos = {
        'projetos': bd_projetos
    }
    return render(request,
                  'projetos/projetos.html', dados_projetos)


def projeto_details(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    dados_projeto = {
        'projeto': projeto
    }
    return render(request, 'projetos/projeto_details.html', dados_projeto)
