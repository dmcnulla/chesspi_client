from eco import Eco
import re


def game_splitter(pgn: str):
    eco = Eco()
    games = []
    lines = pgn.split('\n')
    game = []
    moves = []
    for line in lines:
        line = line.replace('\"', '\'')
        if '[Event' in line:
            # start of new game is detected
            if game:
                # if a previous game already exists, let's close it out and start a new one
                complete_game(eco, game, games, moves)
                game = []
                moves = []
            game.append(line.strip())
        elif line.strip() == '':
            skip()
        elif line[0] != '[':  # must be a move!
            moves.append(line.strip())
        else:
            game.append(line.strip())
    complete_game(eco, game, games, moves)  # for the last game because there is no next [Event ...]

    return games


def complete_game(eco, game, games, moves):
    all_moves = ' '.join(moves)
    eco_setting = eco.find(all_moves)
    game.append(f"[ECO '{eco_setting}']")
    re.sub(' +', ' ', all_moves)  # get rid of extra spaces in the moves list
    game.append(all_moves)
    games.append('|'.join(game))


def skip():
    pass
