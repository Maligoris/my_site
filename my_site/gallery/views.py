from django.shortcuts import render, get_object_or_404

from .models import Album, Img

def album_view(request):
    albums = Album.objects.all()
    return render(request, 'gallery/gallery.html', {'albums': albums})

def open_album(request, title_album=Album.title):
    photos = Img.objects.filter(alb__title=title_album)
    return render(request, 'gallery/details.html', {
        'photos': photos
    })
