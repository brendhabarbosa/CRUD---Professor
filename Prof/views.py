from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def index(request):
    professores = Professor.objects.all()
    form = ProfessorForm( request.POST or None )
    if request.method == 'POST':
        form = ProfessorForm(method.POST)
        if form.is_valid():
            form.save()
            form = ProfessorForm()

    return render(request, 'Prof/index.html', {'professores': professores})