from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse, HttpResponse

from .models import Command, Library, DataFrame, Algorithm, PythonLibrary
# from .pandas_functions import PandasFunctions

import pandas as pd

def main_page(request):
    context_dict = {}    
    context_dict['title'] = 'Machine Learning'

    context_dict['libraries'] = Library.objects.all()

    context_dict['algorithms'] = Algorithm.objects.all()
    context_dict['python_libs'] = PythonLibrary.objects.all()

    return render(request, 'machine_learning/ml_home.html', context_dict)

def interactive(request, library):
    context_dict = {}

    data = DataFrame.objects.get(name='boston_airbnb')
    context_dict['data'] = data
    
    # frame = "```python\n%s```"

    library = Library.objects.get(slug=library)
    command_list = Command.objects.filter(library=library).order_by('section').order_by('id')
       
    context_dict['title'] = library.library

    if command_list.exists():
        context_dict['command_list'] =  command_list
    else:
        raise Http404

    return render(request, 'machine_learning/interactive.html', context_dict)

def algorithms(request, algorithm):
    context_dict = {}

    alg = get_object_or_404(Algorithm, slug=algorithm)
    context_dict['alg'] = alg

    return render(request, 'machine_learning/algorithms.html', context_dict)

def libraries(request, pylibrary):
    context_dict = {}

    lib = get_object_or_404(PythonLibrary, slug=pylibrary)
    context_dict['lib'] = lib

    return render(request, 'machine_learning/libraries.html', context_dict)


# def run_command(request):
#    if request.method == 'POST':
#        pass
    
#    return HttpResponse("/")
