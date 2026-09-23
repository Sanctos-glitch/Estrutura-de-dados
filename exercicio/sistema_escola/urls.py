
from django.contrib import admin

from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medico/', medico_view),
    path('', home),
]


# MVT (MVC)




# www.vollmed.online/
# www.vollmed.online/login

# MEDICO
# www.vollmed.online/medico/id
# www.vollmed.online/medico/id/alterar -> altera cadastro do médico

# www.vollmed.online/medico/id/consultas

# PACIENTE

# www.vollmed.online/paciente/id -> Perfil do paciente
# www.vollmed.online/paciente/id/alterar -> altera cadastro do paciente

# www.vollmed.online/paciente/id/consultas/cadastrar/
# www.vollmed.online/paciente/id/consultas/id -> ver, alterar, deletar

# SECRETARIO
# www.vollmed.online/secretario/id -> Perfil do secretario
# www.vollmed.online/secretario/id/alterar -> altera cadastro do secretario

# www.vollmed.online/secretario/id/consultas/cadastrar/
# www.vollmed.online/secretario/id/consultas/id -> ver, alterar, deletar


# CONSULTA