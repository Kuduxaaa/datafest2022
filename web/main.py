# -*- coding: utf-8 -*-

import argparse
from app import app

parser = argparse.ArgumentParser(
    prog = 'Data Visualisation',
    description = 'Data visualisation framework',
    epilog = 'Good lucky ;D'
)

parser.add_argument('-ho', '--host', type=str, help='Host to run the server', default='127.0.0.1')
parser.add_argument('-p', '--port', type=str, help='Port to run the server', default=8080)
parser.add_argument('-d', '--debug', action='store_true', help='Debug mode', default=False)

if __name__ == '__main__':
    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)
