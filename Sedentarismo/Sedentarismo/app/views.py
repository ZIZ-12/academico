from django.shortcuts import render
from django.views import View
from .models import Dieta, Alimento, Exercicio, DiaSemana, Pessoa, HorarioDormir, Meta, ExercicioFavorito, Feedback, AvaliacaoFisica

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class DietaView(View):
    def get(self, request, *args, **kwargs):
        # Busca todas as dietas com alimento e dia já carregados (otimização)
        dietas = Dieta.objects.select_related('alimento', 'dia').all()
        # Busca os dias da semana do banco, ordenados pelo id para manter a ordem correta
        dias = DiaSemana.objects.order_by('id').values_list('nome', flat=True)

        context = {
            'dietas': dietas,
            'dias': dias,
        }
        return render(request, 'dieta.html', context)

class ExercicioView(View):
    def get(self, request, *args, **kwargs):
        exercicios = Exercicio.objects.all()
        return render(request, 'exercicios.html', {'exercicios': exercicios})

class DiasSemanaView(View):
    def get(self, request, *args, **kwargs):
        dias = DiaSemana.objects.all()
        return render(request, 'dias_semana.html', {'dias': dias})

class HorarioDormirView(View):
    def get(self, request, *args, **kwargs):
        horarios = HorarioDormir.objects.all()
        return render(request, 'horarios_dormir.html', {'horarios': horarios})

class MetaView(View):
    def get(self, request, *args, **kwargs):
        metas = Meta.objects.all()
        return render(request, 'metas.html', {'metas': metas})

class ExercicioFavoritoView(View):
    def get(self, request, *args, **kwargs):
        favoritos = ExercicioFavorito.objects.select_related('exercicio').all()
        return render(request, 'exercicios_favoritos.html', {'favoritos': favoritos})

class AvaliacaoFisicaView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = AvaliacaoFisica.objects.all()
        return render(request, 'avaliacoes_fisicas.html', {'avaliacoes': avaliacoes})

class FeedbackView(View):
    def get(self, request, *args, **kwargs):
        feedbacks = Feedback.objects.all()
        return render(request, 'feedback.html', {'feedbacks': feedbacks})
