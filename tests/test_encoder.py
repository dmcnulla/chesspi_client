import unittest
from os import path as os_path

from encoder import game_splitter

RESOURCE_DIR = os_path.join(os_path.realpath(os_path.dirname(__file__)), 'resources')


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.pgn = self.get_file_pgn_data('test1.pgn')
        self.pgn_a = self.get_file_pgn_data('test1a.pgn').strip()
        self.pgn_b = self.get_file_pgn_data('test1b.pgn').strip()

    def get_file_pgn_data(self, file_name):
        with open(os_path.join(RESOURCE_DIR, file_name)) as f:
            return f.read()

    def test_game_splitter(self):
        games = game_splitter(self.pgn)
        self.assertEqual(self.pgn_a, games[0])
        self.assertEqual(self.pgn_b, games[1])


if __name__ == '__main__':
    unittest.main()
