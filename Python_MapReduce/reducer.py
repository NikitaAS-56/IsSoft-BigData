

import argparse
import sys


def argument_parser() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int,
                        help="Number of top rated movies for each genre")
    return vars(parser.parse_args())



def shuffle():
    dct = {}
    for line in sys.stdin:
        key, value = line.split("\t")
        if key in dct:
             dct[key].append(value)
        else:
             dct[key] = [value]
    return dct


def reduce(key, value, n=None):
    if n:
        for v in value[:n]:
            print(f"{key},{v}")

    else:
        for v in value:
            print(f"{key},{v}")


def main():
    args = argument_parser()
    print('genre,title,year')
    for key, value in shuffle().items():
        reduce(key, value, args['N'])


if __name__ == '__main__':
    main()