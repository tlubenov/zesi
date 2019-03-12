from django.shortcuts import render


def index(request):

    return render(request, 'index.html', {'informs': infos})


class Info:

    def __init__(self, namen, value):
        self.namen = namen
        self.value = value

infos = [
    Info('test', 500),
    Info('ttt', 250)
]
