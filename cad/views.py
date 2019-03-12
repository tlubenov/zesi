from django.shortcuts import render

def index(request):
    namen = 'CAD'
    value = 'Razgrad'
    context = {
        'namen': namen,
        'value': value,
    }
    return render(request, 'cad_index.html', context)
