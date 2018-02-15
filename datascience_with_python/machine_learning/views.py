from django.shortcuts import render
from django.http import Http404, JsonResponse, HttpResponse

from .models import Command, DataFrames
# from .pandas_functions import PandasFunctions

def main_page(request):
    context_dict = {}    
    context_dict['title'] = 'Machine Learning'

    context_dict['libraries'] = Command.objects.values_list('library', flat=True).distinct()
    

    return render(request, 'machine_learning/ml_home.html', context_dict)

def interactive(request, library):
    context_dict = {}

    context_dict['title'] = library
    command_list = Command.objects.filter(library=library).order_by('section')
        
    if command_list.exists():
        context_dict['command_list'] =  command_list
    else:
        raise Http404

    return render(request, 'machine_learning/interactive.html', context_dict)

# def run_command(request):
#    if request.method == 'POST':
#        pass
    
#    return HttpResponse("/")
