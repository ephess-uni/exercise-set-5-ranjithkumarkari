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
    print(f"Number of lines in {args.infile}: {line_count_value}")



if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename argument from the command line
    # pass this argument to the main function above
    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    pass
