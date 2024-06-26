""" ex_5_2.py
This module contains an entry point that

- loads data from a file ex_5_2-data.csv into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called ex_5_2-processed.csv
"""
import numpy as np
import csv
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

    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    # Complete the data processing steps using numpy here.

    # Save the output to OUTFILE using numpy routines.
    process_data(INFILE, OUTFILE)