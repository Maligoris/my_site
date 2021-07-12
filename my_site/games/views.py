from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def tictac_prelude(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        option  = request.POST.get('option')
        room_code = request.POST.get('room_code')

        if option == '0': # Если пользователь знает номер комнаты
            game = Game.objects.filter(room_code = room_code).first() # Ищем комнату
            if game is None:
                messages.error(request, 'Комната не найдена')
                return redirect('http://localhost:8000/games/')

            if game.is_over:
                messages.error(request, 'Игра уже закончена')
                return redirect('http://localhost:8000/games/')

            game.game_opponent = username
            game.save()
            return redirect('/tictac/' + room_code + '?username=' + username)
        elif option == '1': # Создаем комнату
            game = Game(game_creator = username, room_code = room_code)
            game.save()
            return redirect('/tictac/' + room_code + '?username=' + username)

    return render(request, 'games/prelude.html')

def tictac(request, room_code):
    game = Game.objects.filter(room_code = room_code).first()
    username = request.POST.get('username')

    creator = game.game_creator
    opponent = game.game_opponent

    username = request.GET.get('username')
    context = { 'room_code' : room_code,
                 'username' : username,
                  'creator' : creator,
                 'opponent' : opponent }

    return render(request, 'games/tictac.html', context)

