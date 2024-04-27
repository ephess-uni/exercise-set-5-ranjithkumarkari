import argparse
import numpy as np
from pathlib import Path

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

def process_data(infile, outfile):
    # Load data from infile into a numpy array
    data = np.loadtxt(infile, delimiter=',')

    # Shift and scale the data to have mean 0 and standard deviation 1
    processed = (data - np.mean(data, axis=0)) / np.std(data, axis=0)

    # Save the processed data to outfile
    np.savetxt(outfile, processed, delimiter=',')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile.")
    parser.add_argument('infile', nargs='?', default='ex_5_2-data.csv', help='Input file name')
    parser.add_argument('outfile', nargs='?', default='ex_5_2-processed.csv', help='Output file name')
    args = parser.parse_args()

    # Use these predefined input / output files
    root_dir = get_repository_root()
    infile = Path(root_dir, "data", args.infile)
    outfile = Path(root_dir, "outputs", args.outfile)

    process_data(infile, outfile)