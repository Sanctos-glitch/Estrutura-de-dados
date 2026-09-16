# COMANDOS DO DJANGO

1. `pip install django` -> Instala o Django no projeto
2. ``django-admin startproject nome_do_projeto`` . -> Criando um novo projeto em django.
3. ``python manage.py runserver`` -> subindo o servidor.
4. ``python manege.py startapp nome_do_app`` -> Criando um novo app
5. ``python manage.py migrate`` -> realiza as migrações do projeto. 
6. ``python manage.py createsuperuser`` -> criar um novo super usuario
7. ``python manage.py changepassword nomedousuario`` -> Altera a senha, caso vc esqueça.
8. ``python manage.py makemigrations`` -> Crie/gera um novo pacote de migração (Util para novo app e alteração no banco de dados);

# ATIVIDADE 
' criar um model para o médico com as informações:
-nome
-sobrenome
-E-mail
- data de criação
- telefone 
- crm
- especialidade 
- mensagem
- ativo = true