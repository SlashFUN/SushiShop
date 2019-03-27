from django import forms          #Форма
from .models import *

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        #fields = [''] Поля, которые нужно включить
        exclude = [""] #Поля которые нужно отключить

