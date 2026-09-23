from django.contrib import admin
from django.urls import path

from sistema.views import medico_view



urlpatterns = [
    path('medico/', medico_view),
]
