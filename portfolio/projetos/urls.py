from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("projetos", views.projetos, name='projetos'),
    path("projeto_details", views.projeto_details, name='projeto_details')
]
