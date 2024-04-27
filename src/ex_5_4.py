import numpy as np
from pathlib import Path

try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root

if __name__ == "__main__":
    # Use these predefined paths
    root_dir = get_repository_root()
    data_dir = root_dir / "data"
    output_dir = root_dir / "outputs"
    input_file = data_dir / "ex_5_4-data.csv"
    output_file = output_dir / "ex_5_4-processed.csv"

    # Load the data from input_file
    data = np.loadtxt(input_file, delimiter=',')

    # Set any negative elements to 0
    processed_data = np.maximum(data, 0)

    # Save the processed data to output_file
    np.savetxt(output_file, processed_data, delimiter=',')