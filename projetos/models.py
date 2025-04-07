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
    
    # texto de entrada, anotação dentro do topico
class Entry(models.Model):
    """Algo específico aprendido sobre o assunto do topico"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    # on delete -> obrigatório
    # para cada entrada de um topico
    
    class Meta:
        verbose_name_plural = 'entries'
        # automaticamente o django adiciona apenas um S no final para plural
        
    def __str__ (self):
        """retorna uma presentação en string do modelo"""
        return self.text[:50] + '....'
        # limita a 50 char 