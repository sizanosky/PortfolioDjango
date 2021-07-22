from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,
                  'projetos/index.html')


def projetos(request):
    return render(request,
                  'projetos/projetos.html')


def projeto_details(request):
    return render(request,
                  'projetos/projeto_details.html')
