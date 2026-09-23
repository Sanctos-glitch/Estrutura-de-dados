from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#VIWES -> Retornam algo, são funções request -> response
# view responsavel pela tela inicial do médico
def medico_view(Request):
    print('Página funcionou')
    return HttpResponse('Pagina inicial do Médico')

# view responsavel pela tela inicial da home
def home(Request):
    print('Página funcionou')
    return HttpResponse('Pagina Home')