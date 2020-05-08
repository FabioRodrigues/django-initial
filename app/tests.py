from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):
    def test_Add_numbers(self):
        self.assertEqual(add(1, 1), 2)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(1, 1), 0)
