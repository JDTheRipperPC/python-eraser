import argparse
import logging
import logging.config

from eraser.eraser import Eraser

LOGGER = logging.getLogger(__name__)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Eraser target files and directories')
    subparsers = parser.add_subparsers(help='sub-command help')

    # Group: logging
    log_group = parser.add_argument_group('logging')
    log_group.add_argument('--loglevel', default='error', help='Logging ERROR by default',
                           choices=['debug', 'info', 'warning', 'error', 'critical'])
    log_group.add_argument('--logformat', default='%(asctime)s - %(levelname)s - %(message)s')

    # Group: retry
    retry_group = parser.add_argument_group('retry')
    retry_group.add_argument('--sleep', type=int, default=5,
                             help='Time to sleep the thread, 5 by default')
    retry_group.add_argument('--max-retry', type=int, default=100,
                             help='How many times will attempt to erase the files, 100 by default')

    # Subparser: targets
    parser_targets = subparsers.add_parser('targets', help='targets help')
    parser_targets.add_argument(
        'targets', metavar='targets', type=str, nargs='+',
        help='List of targets files and directories to be erased')

    # Subparser: from_file
    parser_from_file = subparsers.add_parser('from_file', help='targets from file help')
    parser_from_file.add_argument('path', nargs=1, help='Path to the input file with the targets')
    parser_from_file.add_argument('format', choices=['plain', 'json', 'xml'],
                                  help='File format of the input file: plain, json, xml')

    return parser.parse_args()


def config_logger(args):
    numeric_level = getattr(logging, args.loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: {}'.format(args.loglevel))

    log_format = args.logformat
    if log_format is None or len(log_format) == 0:
        raise ValueError('Invalid log format: "{}"'.format(log_format))

    logging.basicConfig(level=numeric_level, format=log_format)


def main():
    args = parse_arguments()
    config_logger(args)
    LOGGER.debug(args)

    if args.targets:
        eraser = Eraser()
        eraser.targets(args.targets)
        eraser.erase()


if __name__ == '__main__':
    main()
