import unittest
import m_1


class TestValueExchange(unittest.TestCase):
    def testevenequal(self):
        self.assertEqual(m_1.value_exchange([1, 3, 5, 7, 9, 11]),
                         [3, 1, 7, 5, 11, 9])

    def testoddequal(self):
        self.assertEqual(m_1.value_exchange([10, 20, 30, 40, 50]),
                         [20, 10, 40, 30, 50])


if __name__ == '__main__':
    unittest.main()
