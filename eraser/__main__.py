import argparse
import logging
import logging.config

# TODO: fix config file
#logging.config.fileConfig(fname='setup.cfg', disable_existing_loggers=False)
LOGGER = logging.getLogger(__name__)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Eraser target files and directories')

    subparsers = parser.add_subparsers(help='sub-command help')

    parser_targets = subparsers.add_parser('targets', help='targets help')
    parser_targets.add_argument(
        'targets', metavar='targets', type=str, nargs='+',
        help='List of targets files and directories to be erased')

    # TODO: Add more subparsers

    return parser.parse_args()


def main():
    args = parse_arguments()
    LOGGER.debug(args)


if __name__ == '__main__':
    main()
