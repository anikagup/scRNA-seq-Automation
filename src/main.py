import json
import scanpy as sc
import os

from preprocessing import preprocess_data, load_data, export_adata_to_csv
from analysis import generate_umap, prediction_umap, perform_differential_expression, user_umap
from ML.workflow import predict_labels


import os
import json

# Get the absolute path of the directory containing main.py (which is src/)
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the correct path to config.json (always inside src/)
CONFIG_PATH = os.path.join(SRC_DIR, "config.json")

print(f"📂 Looking for config.json at: {CONFIG_PATH}")  # Debugging print

# Load config.json safely
if not os.path.exists(CONFIG_PATH):
    raise FileNotFoundError(f"❌ ERROR: config.json not found at {CONFIG_PATH}")

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

print(f"✅ Loaded config from: {CONFIG_PATH}")


# Define file paths
input_file = config.get("input_file", "uploads/latest.csv")

if not os.path.exists(input_file):
    print(f"⚠️ Input file '{input_file}' not found.")
    print("💡 Please upload a valid input file via the UI.")
    exit(1)  # Exit gracefully to avoid Docker crash

file_type = config.get("file_type", "auto")


# input_file = config.get("input_file", "data/pbmc3k.h5ad")
# file_type = config.get("file_type", "h5ad")
params = config.get("preprocessing_params", {})
umap_params=config.get("visualization", {})

print("📂 Loading dataset...")
adata = load_data(input_file, file_type)

if adata is None:
    print("❌ ERROR: No valid data loaded. Exiting.")
    exit(1)

print(f"✅ Data loaded! Shape: {adata.shape}")  # Debugging step

# Preprocess data
print("🔄 Running preprocessing...")
adata = preprocess_data(adata, params)
print("✅ Preprocessing complete!")

export_adata_to_csv(adata, output_path="processed_data/processed_matrix.csv")
print("✅ processed data matrix has been downloaded")

# Generate UMAPs and perform clustering
generate_umap(adata, config)

user_umap(adata, umap_params)
#predict_labels(adata)

#prediction_umap(adata, config)

# Perform differential gene expression analysis
perform_differential_expression(adata, config)



# Save processed data
adata.write("processed_data/final_processed_data.h5ad")
print("✅ Processed data saved to 'processed_data/final_processed_data.h5ad'")