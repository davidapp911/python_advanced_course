import argparse
import logging
import time
from typing import Dict

# basic setup for loging
logger = logging.getLogger('TT_CLI_Tool')
logging.basicConfig(level=logging.INFO)
execution_time: Dict[str, float] = {}

# decorator to measure time of execution of a method
def timelog(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        execution_time[func.__name__] = float(end - start)

        return result
    return wrapper

# argument parser for when the script is execute from the terminal
def arg_parser():
    parser = argparse.ArgumentParser(description='TT CLI Tool')
    parser.add_argument('--infile', required=True, help='input file path')
    parser.add_argument('--outfile', required=True, help='output file path')

    return parser.parse_args()

# sample method that counts the amount of words inside an input file
@timelog
def infile_proc(infile, outfile):
    try:
        with open(infile, 'r') as i:
            data = i.read()
            logger.info(f'File read: {infile}')

        with open(outfile, 'w') as o:
            o.write(f"Words in file: {len(data.split(' '))}")
            logger.info(f'File written: {outfile}')
    except FileNotFoundError:
        logger.error(f'Input file not found: {infile}')

    time.sleep(2)

# run method for when the program is executed on a ide debugger
def run():
    infile = input('Input file path: ')
    outfile = input('Output file path: ')

    infile_proc(infile, outfile)

    print(f"Took {execution_time['infile_proc']:.2f} seconds")

# main method for when the program is executed in the command line
def main():
    args = arg_parser()

    infile_proc(args.infile, args.outfile)

    print(f"Took {execution_time['infile_proc']:.2f} seconds")


if __name__ == '__main__':
    main()