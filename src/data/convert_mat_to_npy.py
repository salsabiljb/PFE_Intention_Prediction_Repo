import scipy.io
import numpy as np
import os

# Define paths
raw_data_dir = "data/raw"
output_dir = "data/processed/npy"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate through .mat files
for file in os.listdir(raw_data_dir):
    if file.endswith(".mat"):
        file_path = os.path.join(raw_data_dir, file)
        mat_data = scipy.io.loadmat(file_path)

        # Extract data and save in .npy format
        for key in mat_data:
            if isinstance(mat_data[key], (list, tuple, dict)):
                continue  # Skip metadata

            np_data = np.array(mat_data[key])
            output_file = os.path.join(output_dir, file.replace(".mat", f"_{key}.npy"))
            np.save(output_file, np_data)

print("✅ Conversion to NPY completed!")
