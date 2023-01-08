import unittest
import m_3


class TestFindSeason(unittest.TestCase):
    def testequal(self):
        self.assertEqual(m_3.set_of_products(4),
                         [1, 2, 6, 24])

    def testnotnone(self):
        self.assertIsNotNone(m_3.set_of_products(0))

    def testraises(self):
        with self.assertRaises(TypeError):
            m_3.set_of_products('девять')


if __name__ == '__main__':
    unittest.main()
