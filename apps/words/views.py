from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView

from apps.words.forms import PlayForm
from apps.words.models import GameWord, Room
from apps.words.services.delete_words import delete_words
from apps.words.services.save_word import save_word


# Create your views here.
class GameWordsListView(ListView):
    model = GameWord


def GameWordsPlay_view(request):
    if request.method == "POST":
        form = PlayForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data["word"]
            room = Room.objects.get(id=1)
            save_word(word=word, room=room)

    else:
        form = PlayForm()

    return render(
        request=request,
        template_name="words/gamewords_play.html",
        context=dict(
            gamewords_list=GameWord.objects.all(),
            form=form,
        ),
    )


def delete_words_view(request):
    delete_words()

    return redirect(reverse_lazy("words:gamewords_play"))


def create_room(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        Room.objects.create(name_of_room=room_name)
        return redirect('words:room_list')

    return render(request, 'words/create_room.html')


def room_list_view(request):
    rooms = Room.objects.all()
    return render(
        request,
        'words/room_list.html',
        {'rooms': rooms}
    )


def room_detail_views(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'words/room_detail.html', {'room': room})


def other_rooms_list(request, room_id):
    current_room = get_object_or_404(Room, id=room_id)
    other_rooms = Room.objects.exclude(id=room_id)
    return render(request, 'words/other_rooms_list.html', {'current_room': current_room, 'other_rooms': other_rooms})
