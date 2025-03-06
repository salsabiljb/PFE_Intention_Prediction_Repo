import scipy.io
import pandas as pd
import os

# Define paths
raw_data_dir = "data/raw"
output_dir = "data/processed/csv"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate through .mat files
for file in os.listdir(raw_data_dir):
    if file.endswith(".mat"):
        file_path = os.path.join(raw_data_dir, file)
        mat_data = scipy.io.loadmat(file_path)

        # Extract signal data (adjust keys based on .mat structure)
        for key in mat_data:
            if isinstance(mat_data[key], (list, tuple, dict)):
                continue  # Skip metadata

            df = pd.DataFrame(mat_data[key])
            output_file = os.path.join(output_dir, file.replace(".mat", f"_{key}.csv"))
            df.to_csv(output_file, index=False)

print("✅ Conversion to CSV completed!")
