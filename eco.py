from os import path as os_path
import pandas


ECO_FILE_NAME = 'scid.eco'
ECO_FILE = os_path.join(os_path.realpath(os_path.dirname(__file__)), ECO_FILE_NAME)
KEY_COL = 0
NAME_COL = 1
MOVE_COL = 2
FIRST_ROW = 0


class MoveList:
    def __init__(self, move_list):
        self.level = 1
        self.move_list = move_list.split(' ')

    def next(self):
        moves_string = ' '.join(self.move_list[0:self.level])
        self.level += 1
        return moves_string


class Eco:
    def __init__(self):
        self.rows = pandas.read_csv(ECO_FILE)

    def find(self, move_sequence):
        # strategy is to go from one more to two moves until there is only one match
        move_list = MoveList(move_sequence)
        submoves = move_list.next()
        matches = self.search(submoves)
        if len(matches) == 0:
            return None
        else:
            while len(matches) > 1:
                new_submoves = move_list.next()
                if submoves == new_submoves:
                    break  # We used the whole list of moves, no matches, so go with first match
                else:
                    submoves = new_submoves
                new_matches = self.search(submoves)
                if len(new_matches) > 1:
                    matches = new_matches
                if len(new_matches) < 2:  # Either case, 0 or 1, we are finished!
                    break
        first_match = self.rows.iloc[matches.first_valid_index()]
        return first_match[KEY_COL]

    def search(self, sequence):
        return self.rows[self.rows['move_sequence'].str.contains(sequence, na=False)]
