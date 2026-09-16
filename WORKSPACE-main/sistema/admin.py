from django.contrib import admin

from sistema import models

# Register your models here.
@admin.register(models.Paciente)#registrando a classe paciente no portal do python
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email','telefone','ativo',)

@admin.register(models.Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','crm','especialidade','email','telefone','ativo',)

@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id','paciente_id','medico_id','status', )