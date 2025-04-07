from django.db import models

# Create your models here.

# manipulação do DB - migra os arquivos para o banco de dados sem precisar digitar SQL

class Topic(models.Model):
    """ Um assunto que o usuário está aprendendo sobre """
    text=models.CharField(max_length=200)
    # registra a data e hora que o assunto foi adicionado
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """ Retorna uma representação em string do modelo """
        return self.text