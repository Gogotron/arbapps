import argparse
from .langton import Langton


def check_rate(x):
    try:
        if float(x) > 0:
            return float(x)
    except ValueError:
        pass
    raise argparse.ArgumentTypeError(f'{x!r} is an invalid strictly postive float')


def check_fade(x):
    try:
        if float(x) >= 0:
            return float(x)
    except ValueError:
        pass
    raise argparse.ArgumentTypeError(f'{x!r} is an invalid postive float')


parser = argparse.ArgumentParser(description="Langton's ant simulation")
parser.add_argument('-r', '--rate',
                    default=1/5,
                    type=check_rate,
                    help='Ant steps per second')
parser.add_argument('-fd', '--fade-dur',
                    default=1,
                    type=check_fade,
                    help='Fade duration')

Langton(parser).start()
