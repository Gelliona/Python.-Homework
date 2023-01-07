import unittest
import m_4


class TestFindMultiplies(unittest.TestCase):
    def testin(self):
        self.assertIn(84, m_4.find_multiples())

    def testbool(self):
        self.assertTrue(type(m_4.find_multiples()) == list)


if __name__ == '__main__':
    unittest.main()
