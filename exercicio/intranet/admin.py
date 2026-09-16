from django.contrib import admin
from intranet import models

@admin.register(models.Aluno)
class AlunoAdmin(admin.ModelAdmin):

    list_display = ('id', 'matricula', 'nome', 'idade', 'cpf', 'endereco', 'telefone', 'ativo')

@admin.register(models.Professor)
class ProfessorAdmin(admin.ModelAdmin):

    list_display = ('id', 'disciplina', 'nome', 'idade', 'cpf', 'endereco', 'telefone', 'ativo')

@admin.register(models.Turma)
class TurmaAdmin(admin.ModelAdmin):

    list_display = ('id', 'turma', 'turno', 'professor_fk', 'aluno_fk', 'ativo')

