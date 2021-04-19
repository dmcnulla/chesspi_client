from eco import Eco

def game_splitter(pgn: str):
    eco = Eco()
    games = []
    lines = pgn.split('\n')
    game = []
    moves = []
    for line in lines:
        if '[Event' in line:
            if game:
                game, moves = complete_game(eco, game, games, moves)
            game.append(line.strip())
        elif line.strip() == '':
            skip()
        elif line[0] != '[':  # must be a move!
            moves.append(line.strip())
        else:
            game.append(line.strip())
    complete_game(eco, game, games, moves) # for the last game because there is no next [Event ...]

    return games


def complete_game(eco, game, games, moves):
    all_moves = ' '.join(moves)
    eco_setting = eco.find(all_moves)
    game.append(f"[ECO \"{eco_setting}\"]")
    game.append(all_moves.replace('  ', ' '))
    games.append('\n'.join(game))
    game = []
    moves = []
    return game, moves


def skip():
    pass
