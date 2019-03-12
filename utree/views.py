from django.shortcuts import render


def index(request):
    namen = 'aaaa'
    value = 'sss'
    context = {
        'namen': namen,
        'value': value,
    }
    return render(request, 'utree_index.html', context)
