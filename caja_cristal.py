import unittest


def isOldMayor(yearsOld):
    return yearsOld >= 18

class TestCristalBox(unittest.TestCase):

    def test_be_old_mayor(self):
        yearsOld = 24
        result = isOldMayor(yearsOld)
        self.assertEqual(result, True)

    def test_not_be_old_mayor(self):
        yearsOld = 12
        result = isOldMayor(yearsOld)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
