from django.db import models

#Для баз данных   makemigration - изменить модули ( базу данных ), migratiom - результат миграции
class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    def __str__(self): # возвращаем презентабельность записм ( например вместо subscriber oblect будте  id
        return 'ID:{0}; E-mail:{1}; Name:{2}'.format(self.id,self.email,self.name)

    class Meta:  # представление в одиничном числе и в множественном
        verbose_name = 'My subscriber'
        verbose_name_plural = 'A lot of subscribers'