from multiprocessing.sharedctypes import Value
from django.shortcuts import render
from home.utils.linkedlist import LinkedList


list_new = LinkedList()

def index(request):
    option = float(request.POST.get('option'))    
    value = float(request.POST.get('number'))


    if option == 1 and value != None:
        list_new.insert(value)

    elif option == 1 and value == None:
        return 

    elif option == 2 and value != None:
        list_new.append(value)

    elif option == 2 and value == None:
        return
    
    elif option == 3 and value != None:
        list_new.removeFirst()

    elif option == 3 and value == None:
        return

    list_template = list_new.toList()

    print(f'\nTemplate: {list_template}')

    return render(request, 'index.html')
