import unittest

def suma(number1, number2):
    return abs(number1 + number2)

class BlackboxTest( unittest.TestCase):

    def test_plus_two_positive(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1,num_2)

        self.assertEqual(resultado, 15)

    def test_sum_two_negative(self):
        num_1 = -10
        num_2 = 7

        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -3)


if __name__ == '__main__':
    unittest.main()