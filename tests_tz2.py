from unittest import TestCase, main
from tz2 import _max, _min, _mult, _sum, _fca


class Test1(TestCase):
    def test_max(self):
        self.assertEqual(_max([1, 0, -1, 3, -1, 44, 413, 43, -23424, -24, 0]), 413)

    def test_min(self):
        self.assertEqual(_min([1, 0, -1, 3, -1, 44, 413, 43, -23424, -24, 0]), -23424)

    def test_mult(self):
        self.assertEqual(_mult([1, 0, -1, 3, -1, 44, 413, 43, -23424, -24, 0]), 0)

    def test_sum(self):
        self.assertEqual(_sum([1, 0, -1, 3, -1, 44, 413, 43, -23424, -24, 0]), -22946)

    # Тест на свое усмотрение:

    def test_fca1(self):
        self.assertEqual(_fca('5'), 'Такой функции нет, перезапустите программу')

    def test_fca2(self):
        self.assertEqual(_fca('ж'), 'Такой функции нет, перезапустите программу')

    def test_fca3(self):
        self.assertEqual(_fca(';'), 'Такой функции нет, перезапустите программу')


if __name__ == '__main__':
    main()
