"""ex_5_0.py"""

def line_count(infile):
    try:
        # Open the file in read mode
        with open(infile, 'r') as file:
            # Read all lines into a list and count the number of lines
            lines = file.readlines()
            num_lines = len(lines)
            print(f"Number of lines in {infile}: {num_lines}")
    except FileNotFoundError:
        print(f"Error: File '{infile}' not found.")

if __name__ == "__main__":
    # Get the utility function for path discovery
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

    # Test line_count with a file from the data directory
    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_2-data.csv")
