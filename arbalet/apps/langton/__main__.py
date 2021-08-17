import argparse
from .langton import Langton
from arbalet.colors import name_to_rgb


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


def convert_scheme(scheme):
    if len(scheme) > 150:
        raise argparse.ArgumentTypeError(f'{scheme!r} is too long for a scheme (max: 150)')
    if all(map(lambda x: x in 'RL', scheme)):
        return list(map(lambda x: 1 if x == 'R' else -1, scheme))
    else:
        raise argparse.ArgumentTypeError(f'{scheme!r} is an invalid R/L scheme')


def color_name(x):
    try:
        return name_to_rgb(x)
    except KeyError:
        raise argparse.ArgumentTypeError(f'{x!r} is an invalid color')


parser = argparse.ArgumentParser(description="Langton's ant simulation")
parser.add_argument('-r', '--rate',
                    default=1/5,
                    type=check_rate,
                    help='Ant steps per second')
parser.add_argument('-fd', '--fade-dur',
                    default=1,
                    type=check_fade,
                    help='Fade duration')
parser.add_argument('--scheme',
                    default='RL',
                    type=convert_scheme,
                    help='Turning scheme to use')
parser.add_argument('--colors',
                    type=color_name,
                    action='append',
                    help='List of colors to cycle through')

Langton(parser).start()
