import argparse
from requests import post
from encoder import game_splitter

LOCAL_CHESSPI_SERVER = 'http://localhost:5000'
GAME_JSON = {
    "delimiter": "|",
    "data": {}
}


def setup_argparse(server=None):
    """
    Parse the args.
    :return: argparse object
    """
    parser = argparse.ArgumentParser(description="### add_trusted_key.py ###")
    parser.add_argument('--server', default=LOCAL_CHESSPI_SERVER, help='ChessPI Server', required=False)
    parser.add_argument('--file', help='File to send to database server.', required=True)

    parsed_args = parser.parse_args()

    return parsed_args


class ChessPiClient:
    def send_pgn(self, server, pgn):
        job = GAME_JSON
        job['data'] = self.encode(pgn)
        post(url=f"{server}/games", json=job)

    def encode(self, pgn):
        games = game_splitter(pgn)
        return "||".join(games)


if __name__ == '__main__':
    args = setup_argparse()
    with open(args.file, 'r') as f:
        ChessPiClient().send_pgn(server=args.server, pgn=f.read())
