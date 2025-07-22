from django.contrib import admin
from .models import *

# Registro simples
admin.site.register(Funcao)
admin.site.register(Exercicio)
admin.site.register(Alimento)
admin.site.register(DiaSemana)

# Inlines válidos
class HorarioDormirInline(admin.TabularInline):
    model = HorarioDormir
    extra = 1

class MetaInline(admin.TabularInline):
    model = Meta
    extra = 1

class ExercicioFavoritoInline(admin.TabularInline):
    model = ExercicioFavorito
    extra = 1

class FeedbackInline(admin.TabularInline):
    model = Feedback
    extra = 1

class DietaInline(admin.TabularInline):
    model = Dieta
    extra = 1

class AvaliacaoFisicaInline(admin.TabularInline):
    model = AvaliacaoFisica
    extra = 1

# Admins corrigidos
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf')
    search_fields = ('nome', 'email')
    inlines = [HorarioDormirInline, MetaInline, ExercicioFavoritoInline, FeedbackInline, DietaInline, AvaliacaoFisicaInline]

class HorarioDormirAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'tempo')
    search_fields = ('pessoa__nome',)

class MetaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'descricao')
    search_fields = ('pessoa__nome', 'descricao')

class DietaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'alimento', 'dia', 'horario', 'quantidade')
    search_fields = ('pessoa__nome', 'alimento__nome')

class AvaliacaoFisicaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'niv_sedenta')
    search_fields = ('pessoa__nome',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'descricao')
    search_fields = ('pessoa__nome', 'descricao')

class ExercicioFavoritoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'exercicio')
    search_fields = ('pessoa__nome', 'exercicio__nome')

# Registro com Admins
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(HorarioDormir, HorarioDormirAdmin)
admin.site.register(Meta, MetaAdmin)
admin.site.register(Dieta, DietaAdmin)
admin.site.register(AvaliacaoFisica, AvaliacaoFisicaAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ExercicioFavorito, ExercicioFavoritoAdmin)
