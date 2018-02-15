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
        self.assertEqual(s.transf_pos(S), (0, 1), 'Тест 8 не пройден')

        S = '+++--+'
        self.assertEqual(s.transf_pos(S), (4, -1), 'Тест 9 не пройден')

        S = '---+-++-'
        self.assertEqual(s.transf(S, (0, 1), 3), '++++-++-', 'Тест 10 не пройден')

        S = '---+-++-'
        self.assertEqual(s.transf(S, (7, -1), 3), '---+---+', 'Тест 11 не пройден')

        S = '++++-+++'
        K = 3
        self.assertEqual(s.is_block_minus(S, K), True, 'Тест 12 не пройден')

        S = '++++---+'
        K = 3
        self.assertEqual(s.is_block_minus(S, K), False, 'Тест 13 не пройден')

        S = '++++----'
        K = 3
        self.assertEqual(s.is_block_minus(S, K), True, 'Тест 14 не пройден')

        S = '---+-++-'
        K = 3
        self.assertEqual(s.flips_cnt(S, K), 3, 'Тест 15 не пройден')

        S = '+++++'
        K = 4
        self.assertEqual(s.flips_cnt(S, K), 0, 'Тест 16 не пройден')

        S = '-+-+-'
        K = 4
        self.assertEqual(s.flips_cnt(S, K), -1, 'Тест 17 не пройден')


if __name__ == '__main__':
    unittest.main()