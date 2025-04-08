from django.shortcuts import render

# Create your views here.

# página principal - acionada pela requisição do user
def index(request):
    # caminho para arquivo html da primeira pagina
    return render(request, 'projetos/index.html')