from django.shortcuts import render
from .models import Topic
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    if request.method != 'POST': 
        # nenhum dado submetido, cria um formulario em branco
        form = TopicForm()
    else:
        #dados de post submetidos, processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            # redireciona para outra pagina - nesse caso é interessante colocar uma url definida quando fizer deploy do projeto, então utiliza-se o reverse que pega como base o name da url, para direcionar para a pagina indicada no arquivo urls
            return HttpResponseRedirect(reverse('topics'))
        
    context = {'form': form}
    return render(request, 'projetos/new_topic.html', context)
        
        
def new_entry(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST': 
        form = TopicForm()
    else:
        #dados de post submetidos, processa os dados
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            # redireciona para outra pagina - nesse caso é interessante colocar uma url definida quando fizer deploy do projeto, então utiliza-se o reverse que pega como base o name da url, para direcionar para a pagina indicada no arquivo urls
            return HttpResponseRedirect(reverse('topics'))
        
    context = {'form': form}
    return render(request, 'projetos/new_topic.html', context)