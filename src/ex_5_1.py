"""ex_5_1.py"""
import argparse
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count


def main():
    parser = argparse.ArgumentParser(description="This program prints the number of lines in the input file.")
    parser.add_argument('infile', help='Input file name')
    args = parser.parse_args()

    line_count_value = line_count(args.infile)
    print(line_count_value)



if __name__ == "__main__":

    pass
