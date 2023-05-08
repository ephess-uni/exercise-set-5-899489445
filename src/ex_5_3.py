""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser
import argparse
def main(infile:str, outfile:str):
    # Load data from input file
    data = np.loadtxt(infile, delimiter=",")

    # Calculate mean and standard deviation of the data
    mean = np.mean(data)
    std = np.std(data)

    # Modify input data to have a mean of 0 and a standard deviation of 1
    processed = (data - mean) / std
    # Save processed data to output file
    np.savetxt(outfile, processed, delimiter=",")

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    parser = argparse.ArgumentParser(description="This program applies a standard scale transform to the data in infile and writes it to outfile.")

    parser.add_argument("infile", type=str, help="input filename for the data file that needs to be processed")
    parser.add_argument("outfile", type=str, help="output filename")

    args = parser.parse_args()

    main(args.infile, args.outfile)
