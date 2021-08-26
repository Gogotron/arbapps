import argparse
from .pong import Pong

parser = argparse.ArgumentParser(description='Pong game')
parser.add_argument('--speed', type=float, default=0.15)

Pong(parser).start()
