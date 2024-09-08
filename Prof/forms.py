from django import forms 
from .models import * 
class ProfessorForm(forms.Form):
    model = Professor
    fields = ['nome', 'cpf', 'data_nascimento', 'email', 'endereco', 'area']
   