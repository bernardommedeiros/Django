from django import forms
from .models import Topic
from .models import Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic;
        fields = ['text']
        labels = {'text': ''}
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry;
        fields = ['text']
        labels = {'text': ''}
        # widgets - altera as formas do formulario padrao, criado automaticamente pelo django
        # attrs={'cols': 80} atributos que seram passados, nesse caso definindo o maximo de colunas em 80
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}