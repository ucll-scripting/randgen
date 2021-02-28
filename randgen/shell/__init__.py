import randgen.shell.csv
from randgen.generator import Generator
import argparse



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, help='seed for RNG', default=None)

    subparsers = parser.add_subparsers(help='subcommands')

    randgen.shell.csv.add_subparser(subparsers)

    args = parser.parse_args()
    generator = _create_generator(args)
    args.function(args, generator)


def _create_generator(args):
    return Generator(args.seed)