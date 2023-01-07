import unittest
import m_2


class TestFindSeason(unittest.TestCase):
    def testequaldict(self):
        self.assertEqual(m_2.find_season_dict(8),
                         '8-й месяц - это лето')

    def testequallist(self):
        self.assertEqual(m_2.find_season_list(1),
                         '1-й месяц - это зима')

    def testin(self):
        self.assertNotIn("лето", m_2.find_season_dict(2))

    def testvaluedict(self):
        with self.assertRaises(KeyError):
            m_2.find_season_dict(13)

    def testvaluelist(self):
        with self.assertRaises(TypeError):
            m_2.find_season_list('пять')


if __name__ == '__main__':
    unittest.main()
