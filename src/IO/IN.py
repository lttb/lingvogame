import argparse


def IN():
    parser = argparse.ArgumentParser('LingvoGame')

    parser.add_argument(
        '-f',
        '--file',
        help='path to input file',
        required=True
    )

    parser.add_argument(
        '--min',
        help='coefficient for minimum rate',
        default=0.02,
        type=float
    )

    parser.add_argument(
        '--max',
        help='coefficient for maximum rate',
        default=0.15,
        type=float
    )

    return parser.parse_args()
