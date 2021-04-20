import argparse
from requests import post
from encoder import game_splitter
from json import dumps as json_dumps

LOCAL_CHESSPI_SERVER = 'http://localhost:5000'
GAME_JSON = {
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
        job['data']['pgn'] = self.encode(pgn)
        body = json_dumps(job)
        headers = {"Content-Type": "application/json"}
        post(url=f"{server}/games", data=body, headers=headers)

    def encode(self, pgn):
        games = game_splitter(pgn)
        return "\n\n".join(games)


if __name__ == '__main__':
    args = setup_argparse()
    with open(args.file, 'r') as f:
        ChessPiClient().send_pgn(server=args.server, pgn=f.read())
