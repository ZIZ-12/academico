from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView,
    DietaView,
    ExercicioView,
    DiasSemanaView,
    HorarioDormirView,
    MetaView,
    ExercicioFavoritoView,
    AvaliacaoFisicaView,
    FeedbackView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('dieta.html/', DietaView.as_view(), name='dieta'),
    path('exercicios/', ExercicioView.as_view(), name='exercicios'),
    path('dias-semana/', DiasSemanaView.as_view(), name='dias_semana'),
    path('horarios-dormir/', HorarioDormirView.as_view(), name='horarios_dormir'),
    path('metas/', MetaView.as_view(), name='metas'),
    path('exercicios-favoritos/', ExercicioFavoritoView.as_view(), name='exercicios_favoritos'),
    path('avaliacoes-fisicas/', AvaliacaoFisicaView.as_view(), name='avaliacoes_fisicas'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
]
