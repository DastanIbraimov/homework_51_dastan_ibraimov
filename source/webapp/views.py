from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.kitty import Kitty

kitty = Kitty()


def index(request):
    return render(request, 'index.html')


def show_info(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            kitty.name = request.POST.get('name')

    if not kitty.name:
        return HttpResponseRedirect('/')

    return render(request, 'kitty.html', context={
        'name': kitty.name,
        'age': kitty.age,
        'fullness': kitty.fullness,
        'mood': kitty.mood,
        'image': kitty.image})


def update(request):
    if request.method == 'POST':
        match request.POST.get('action'):
            case 'play':
                kitty.play()
                kitty.validate_params()
            case 'feed':
                kitty.feed()
                kitty.validate_params()
            case 'sleep':
                kitty.sleep()
    return HttpResponseRedirect('/kitty')
