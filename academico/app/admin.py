from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cidade)
admin.site.register(Pessoa)
admin.site.register(Matricula)
admin.site.register(Turno)
admin.site.register(Ocorrencia)
admin.site.register(AvaliacaoTipo)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(CursoDisciplina)




class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class AlunoInline(admin.TabularInline):
    model = Matricula
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

# Adminsssssssssssss
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [PessoaInline]

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline]

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [CursoInline]

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [CursoDisciplinaInline]

class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [AlunoInline]

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [AlunoInline, AvaliacaoInline, FrequenciaInline]

admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(InstituicaoEnsino, InstituicaoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Turma, TurmaAdmin)





