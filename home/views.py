from django.contrib import messages
from django.shortcuts import render
from home.utils.linkedlist import LinkedList


list_new = LinkedList()

def index(request):
    option = int(request.POST.get('option'))    
    value = request.POST.get('number')

    if option == 1 and value != '':
        list_new.insert(int(value))
        messages.success(request, 'Novo valor inserido no início da Lista!')

    elif option == 1 and value == '':
        messages.error(request, 'Digite um número para ser inserido!') 

    elif option == 2 and value != '':
        list_new.append(int(value))
        messages.success(request, 'Novo valor inserido no final da Lista!')

    elif option == 2 and value == '':
        messages.error(request, 'Digite um número para ser inserido!')
    
    elif option == 3 and len(list_new) > 0:
        list_new.removeFirst()
        messages.success(request, 'Primeiro valor da lista removido!')

    elif option == 3 and len(list_new) == 0:
        messages.error(request, 'Lista vazia, adicione valores para remover!')

    list_template = list_new.toList()

    print(f'\nTemplate: {list_template}')

    return render(request, 'index.html', {
        'list_display': list_template 
    })
