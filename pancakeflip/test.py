import solve as s
import unittest

class TestAnalyzer(unittest.TestCase):

    def test_1(self):
        S = '++++'
        self.assertEqual(s.is_positive(S), True, 'Тест 1 не пройден')

        S = '---'
        self.assertEqual(s.is_positive(S), False, 'Тест 2 не пройден')

        S = '+++++'
        self.assertEqual(s.is_negative(S), False, 'Тест 3 не пройден')

        S = '-'
        self.assertEqual(s.is_negative(S), True, 'Тест 4 не пройден')

        S = '---+-++-'
        self.assertEqual(s.lone_minus_cnt(S), 3, 'Тест 5 не пройден')

        S = '---'
        self.assertEqual(s.lone_minus_cnt(S), 1, 'Тест 6 не пройден')

        S = '---+-++-'
        self.assertEqual(s.get_transf_pos(S), (0, 1), 'Тест 8 не пройден')

        S = '+++--+'
        self.assertEqual(s.get_transf_pos(S), (4, -1), 'Тест 9 не пройден')

if __name__ == '__main__':
    unittest.main()