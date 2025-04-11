from django.shortcuts import render
from .models import Topic

# Create your views here.

# página principal - acionada pela requisição do user
def index(request):
    # caminho para arquivo html da primeira pagina
    return render(request, 'projetos/index.html')



def topics(request):
    topics = Topic.objects.order_by('date_added')
    # template da função
    context = {
        'topics': topics
    }
    return render(request, 'projetos/topics.html', context)


# página listando topicos
    
def topic(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic, 'entries': entries
    }
    
    return render(request, 'projetos/topic.html', context)


# adição de um novo assunto

def new_topic(request):
    if 
    context = {
        
    }
    
    return render(request, 'projetos/topic.html', context)
    