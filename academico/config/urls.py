"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.views import View
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('cidades/', CidadesView.as_view(), name='cidades'),
    path('ocupacao/', OcupacaoView.as_view(), name='ocupacao'),
    path('instituicao/', InstituicaoView.as_view(), name='instituicao'),
    path('areas-do-saber/', AreaSaberView.as_view(), name='area'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('turmas/', TurmasView.as_view(), name='turmas'),
    path('disciplinas/', DisciplinasView.as_view(), name='disciplinas'),
    path('matriculas/', MatriculasView.as_view(), name='matriculas'),
    path('avaliacoes/', AvaliacoesView.as_view(), name='avaliacoes'),
    path('disciplinas-curso/', CursosDisciplinasView.as_view(), name='disciplinasCurso'),
    path('frequencias/', FrequenciasView.as_view(), name='frequencia'),
    path('ocorrencias/', OcorrenciasView.as_view(), name='ocorrencia'),
    path('turnos/', TurnosView.as_view(), name='turno'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),


]
