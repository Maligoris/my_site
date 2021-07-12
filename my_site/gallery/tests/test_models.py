from django.test import TestCase

from gallery.models import *
from django.core.files.uploadedfile import SimpleUploadedFile

class GalleryModelTest(TestCase):

    def setUp(self):
        # Создаем объект который будем использовать для тестов
        Album.objects.create(title="Photos")

    def test_title_Album(self):
        album = Album.objects.get(title="Photos")
        # Название альбома совпадает
        self.assertEqual(album.title, 'Photos')

    def test_Img(self):
        album = Album.objects.get(title="Photos")
        new_img = Img() # Создаем объект Img
        new_img.alb = album # Поскольку поле alb - ForeignKey, передаем экземпляр класса Album 
#       new_img.image =  SimpleUploadedFile('test_image.jpg', open('путь/до/test_image', 'rb'), content_type='image/gif') # Создаем фото
        # Проверяем что фото взято из своего альбома
        self.assertEqual(str(new_img.alb), 'Photos')
