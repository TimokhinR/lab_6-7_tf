import unittest
from app import app  # Імпортуємо додаток Flask з файлу app.py

class TestMathAPI(unittest.TestCase):

    def setUp(self):
        # Створюємо тестовий клієнт Flask
        self.client = app.test_client()

    def test_home(self):
        # Перевірка маршруту '/'
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Перевіряємо, чи статус відповіді 200
        self.assertEqual(response.data.decode(), "Welcome to the Math API!")  # Перевіряємо текст відповіді

    def test_add(self):
        # Перевірка маршруту '/add/<float:a>/<float:b>'
        response = self.client.get('/add/3.5/2.5')
        self.assertEqual(response.status_code, 200)  # Перевіряємо, чи статус відповіді 200
        self.assertEqual(response.data.decode(), '6.0')  # Перевіряємо значення відповіді

    def test_subtract(self):
        # Перевірка маршруту '/subtract/<float:a>/<float:b>'
        response = self.client.get('/subtract/10.5/4.5')
        self.assertEqual(response.status_code, 200)  # Перевіряємо, чи статус відповіді 200
        self.assertEqual(response.data.decode(), '6.0')  # Перевіряємо значення відповіді

if __name__ == '__main__':
    unittest.main()

