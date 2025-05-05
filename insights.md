# Conceitos importantes ao decorrer do curso, para manipulação do ambiente virtual, banco de dados e do projeto em geral.

- Criação do ambiente virtual:
```
python -m venv venv
```

- Ativação do ambiente virtual:
```
venv/Scripts/activate
```

- inicialização de um novo projeto:
```
django-admin startproject
```

- inicialização do banco de dados:
```
python manage.py migrate
```

- RUN:
```
python .\manage.py runserver
```

- conexão DB (migrations):
```
python .\manage.py startapp projetos
python .\manage.py makemigrations projetos 
```

- criação de tabela no DB:

```
python .\manage.py migrate   
````

- painel administrativo:

```
python .\manage.py createsuperuser 
````

- criação de um novo app:

```
python .\manage.py  startapp nome_do_projeto
````



## navegação do projeto pelo Shell

- ativação na venv:
```
python .\manage.py shell
```

- importação dos apps/objetos:
```
from projeto.models import Topic
```

- seleciona todos os topicos e armazena na variavel:
```
topic = Topic.objects.all()
```

- seleciona o topico com um id especifico, podendo manipular seus atributos especificos:
```
 t = Topic.objects.get(id=x)
```

- seleciona todos os topicos:
```
for topic in topics:
    print(topic.id, topic)
```

- utiliza da chave estrangeira para pegar a descrição do topico:
```
t.entry_set.all()
```