from django.forms import ModelForm
from .models import Task

class TodoForms(ModelForm):
    class Meta:
        model = Task
        fields = ['name','priority','date']
