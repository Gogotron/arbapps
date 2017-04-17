import argparse
from .spectrum import SpectrumAnalyser
from arbalet.application import get_application_parser

parser = argparse.ArgumentParser(description='Musical spectrum display for the default system audio input')
parser.add_argument('-v', '--vertical',
                    action='store_const',
                    const=True,
                    default=False,
                    help='The spectrum must be vertical (less bands, more bins)')

parser = get_application_parser(parser)
args = parser.parse_args(parser)

SpectrumAnalyser(**args.__dict__).start()

