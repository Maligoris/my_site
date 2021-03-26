from django.shortcuts import render, get_object_or_404

from .models import Album, Img

def album_view(request):
    albums = Album.objects.all()
    return render(request, 'gallery/gallery.html', {'albums': albums})

def open_album(request, id):
    album = get_object_or_404(Img, id=id) # Н
    photos = Img.objects.all() #filter(album=album)
    print(photos)
    return render(request, 'gallery/details.html', {
        'album': album,
        'photos': photos
    })

def test(request):
    return render(request, 'gallery/details.html')

