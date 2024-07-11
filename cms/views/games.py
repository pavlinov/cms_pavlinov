from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ..models import Game
from ..forms import GameForm

def game_list_view(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

@login_required
def add_game_view(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.added_by = request.user
            game.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'add_game.html', {'form': form})

@login_required
def edit_game_view(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)
    return render(request, 'edit_game.html', {'form': form})

@login_required
def remove_game_view(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'confirm_delete.html', {'game': game})
