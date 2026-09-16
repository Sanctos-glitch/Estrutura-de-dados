from django.db import models #ORM do Django para declarar modelos no banco de dados.
from django.utils import timezone # util para data/hora atual no projeto.
# Modelo que representa um Paciente.
#atributos => nome, sobrenome, email, telefone, data de cadastro, mensagem, ativo (True ou False)

# Modelo que representa um Paciente.
class Paciente(models.Model):
    nome = models.CharField(max_length=25)# Nome do paciente
    sobrenome = models.CharField(max_length=50)# Sobrenome do paciente.
    email = models.EmailField() #Email de contato com paciente
    telefone = models.CharField(max_length=20)# telefone de contado
    criacao_data = models.DateTimeField(default=timezone.now)# data hora de cadastro
    mensagem = models.TextField(blank=True)# campo opcional livre para mensagem.
    ativo =  models.BooleanField(default=True) # campo de exclusão logica, caso o paciente seja desativado, não será excluido do banco de dados, apenas marcado como inativo.

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
# Modelo que representa um Médico
class Medico(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    criacao_data = models.DateTimeField(default=timezone.now)
    mensagem = models.TextField(blank=True)
    ativo =  models.BooleanField(default=True)
    crm = models.CharField(max_length=100, default="") # campo para armazenar o CRM do médico
    especialidade = models.CharField(max_length=100, default="")

    def __str__(self):
            return f'{self.nome} {self.sobrenome}' #retorna uma string com o nome, sobrenome e email do paciente.


# Modelo que representa uma Consulta.
class Consulta(models.Model):
     paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE) # chave estrangeira para o paciente
     medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE) # chave estrangeira para o médico
     data_consulta = models.DateTimeField(default=timezone.now) # data e hora da consulta
     ativa = models.BooleanField(default=True) # campo de exclusão logica, caso a consulta seja desativada, não será excluida do banco de dados, apenas marcada como inativa.
     observacao = models.TextField(blank=True) # campo opcional livre para observação da consulta.
     status = models.CharField(
          default='A',
          max_length=1,
          choices=[
                ('A', 'Agendada'),
                ('x', 'Cancelada'),
                ('C', 'Confirmada'),
                ('R', 'Realizada'),
          ]
     ) # campo para armazenar o status da consulta (Agendada, Realizada, Cancelada, etc.)