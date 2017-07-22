from django.shortcuts import render

def main_page(request):
    context_dict = {}

    context_dict['title'] = 'Machine Learning'

    return render(request, 'machine_learning/ml_home.html', context_dict)

def numpy(request):
    context_dict = {}
    
    context_dict['title'] = 'Numpy'

    return render(request, 'machine_learning/numpy.html',  context_dict)

def pandas(request):
    context_dict = {}

    context_dict['title'] = 'Pandas'

    return render(request, 'machine_learning/pandas.html', context_dict)

def scikitlearn(request):
    context_dict = {}

    context_dict['title'] = 'ScikitLearn'

    return render(request, 'machine_learning/scikitlearn.html', context_dict)

