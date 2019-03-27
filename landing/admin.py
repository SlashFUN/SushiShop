from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    #list_display = ['name','email'] # Поля, которые выводятся
    list_display = [field.name for field in Subscriber._meta.fields] # итератор всех полей для вывода
    #exclude = [''] # исключение поля
    #fields = ['']#Добавление поля
    list_filter = ('name','email') #появление блока фильтр на страние админки
    search_fields = ['name','email']#поиск/фильтрация по значению
    class Meta:

        model = Subscriber #Берет данные с Subscriber / модель на основе


admin.site.register(Subscriber, SubscriberAdmin)