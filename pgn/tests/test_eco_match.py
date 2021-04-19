import unittest
from pgn.eco import Eco

TEST0 = '1. e4 Nf6 2. e5 Nd5 3. d4 d6 4. c4 Nb6 5. f4 dxe5 6. fxe5 Bf5 7. Nc3 e6 8. Nf3 Be7 9. Be2 O-O 10. O-O f6'
MATCH0 = 'B03l'
TEST1 = '1. e4 d5'
MATCH1 = 'B01a'
TEST2 = '1. e4 e5 2. f4 d5 3. exd5 c6 4. dxc6 nxc6 5. h4'
MATCH2 = 'C31'
TEST3 = '1. b2'  # No way this matches anything, it's not even a legal move
MATCH3 = 'A00a'  # Starting Position, no moves at all. Used if there is no match for any moves.


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.eco = Eco()

    def test_eco_match_long_move_list(self):
        self.assertEqual(MATCH0, self.eco.find(TEST0))

    def test_eco_match_short_move_list(self):
        self.assertEqual(MATCH1, self.eco.find(TEST1))

    def test_eco_match_after_multiple_tries(self):
        self.assertEqual(MATCH2, self.eco.find(TEST2))

    def test_eco_no_match(self):
        self.assertEqual(MATCH3, self.eco.find(TEST3))


if __name__ == '__main__':
    unittest.main()
