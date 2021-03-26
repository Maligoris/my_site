from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def tictac_prelude(request):
    if request.method == "POST": # Если пользователь ввел данные
        username = request.POST.get('username')
        option  = request.POST.get('option')
        room_code = request.POST.get('room_code')


        if option == '1': # Если пользователь знает номер комнаты
            game = Game.objects.filter(room_code = room_code).first() # Ищем комнату
            print(game)
            print(type(game))

            if game is None:
                messages.success(request, "Комната не найдена")
                return redirect('/')

            if game.is_over:
                messages.success(request, "Игра окончена")
                return redirect('/')

            game.game_opponent = username
            game.save()
            #return redirect('/tictac/' + room_code + '?username=' + username)
        else: # Создаем комнату
            game = Game(game_creator = username, room_code = room_code)
            game.save()
            return redirect('/tictac/' + room_code + '?username=' + username)

    return render(request, 'games/prelude.html')

def tictac(request, room_code):
    username = request.GET.get('username')
    context = {'room_code' : room_code, 'username' : username}
    return render(request, 'games/tictac.html', context)
