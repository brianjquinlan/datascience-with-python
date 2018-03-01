from django.shortcuts import render
from django.http import Http404, JsonResponse, HttpResponse

from .models import Command, Library, DataFrames
# from .pandas_functions import PandasFunctions

def main_page(request):
    context_dict = {}    
    context_dict['title'] = 'Machine Learning'

    context_dict['libraries'] = Library.objects.all()

    return render(request, 'machine_learning/ml_home.html', context_dict)

def interactive(request, library):
    context_dict = {}

    context_dict['title'] = library

    library = Library.objects.get(library=library)
    command_list = Command.objects.filter(library=library).order_by('section')
        
    if command_list.exists():
        context_dict['command_list'] =  command_list
    else:
        raise Http404

    return render(request, 'machine_learning/interactive.html', context_dict)

def algorithms(request):
    return render(request, 'machine_learning/algorithms.html')

def libraries(request):
    return render(request, 'machine_learning/libraries.html')


# def run_command(request):
#    if request.method == 'POST':
#        pass
    
#    return HttpResponse("/")
