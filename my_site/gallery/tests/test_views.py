from django.test import TestCase


class GalleryPage(TestCase):

    def test_gallery_load_correct(self):
        response = self.client.get('/gallery/')
        # Страница загрузилась корректно
        self.assertEqual(response.status_code, 200)
        # Используеться правильный шаблон
        self.assertTemplateUsed(response, 'gallery/gallery.html')
        # Заголовок корректен (Вкладка браузера)
        self.assertContains(response, 'Галерея')
