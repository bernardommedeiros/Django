from django.shortcuts import render
from .models import Topic

# Create your views here.

# página principal - acionada pela requisição do user
def index(request):
    # caminho para arquivo html da primeira pagina
    return render(request, 'projetos/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {
        'topics': topics
    }
    return render(request, 'projetos/topics.html', context)