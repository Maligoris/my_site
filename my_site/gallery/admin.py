from django.contrib import admin

from .models import Album, Img

class ImgAdmin(admin.StackedInline):
    model=Img

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [ImgAdmin]

    class Meta:
        model = Album

@admin.register(Img)
class AlbumAdmin(admin.ModelAdmin):
    pass
