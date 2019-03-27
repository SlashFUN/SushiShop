from django.shortcuts import render
from .forms import SubscriberForm

def landing(request):
    name = 'Sushi-Mushi'
    form = SubscriberForm(request.POST or None)
    if request.method == "POST"and form.is_valid():
        print(request.POST)
        print(form) # <QueryDict: {'csrfmiddlewaretoken': ['5I9e6RNyJ4wlbbE4WPNbzx7utxdw3aJVmqsHc5WjOqCqSChVLsiWaKhXK7YzTQC3'], 'email': ['Olaph@gmail.com'], 'name': ['Hector']}>
        print(form.cleaned_data) #для расчитки полей нужно .is_valid() словарь {'email': 'Olaph@gmail.com', 'name': 'Hector'}
        data = form.cleaned_data['name']
        print(data)

        new_form = form.save()  # form.save() сохранение формы
    return render(request, 'landing/test.html', locals())