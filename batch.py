import torch
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

import os
from transformers import pipeline
import shutil
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Startup Parameters')
    parser.add_argument("--device", type=str, default=0, help="Cuda")
    parser.add_argument("--path", type=str, default="test", help="Input folder")
    parser.add_argument("--output", type=str, default="outputs", help="Output folder")
    parser.add_argument("--threshold", type=str, default=0.5, help="HQ threshold")
    parser.add_argument("--batch", type=str, default=8, help="Batch size")
    return parser.parse_args()
args = get_args()

pipe = pipeline("image-classification", model="shadowlilac/aesthetic-shadow-v2", device=f"cuda:{args.device}")

# Define the paths for the input folder and output folders
input_folder = args.path
output_folder_hq = f"{args.output}/hq_folder" 
output_folder_lq = f"{args.output}/lq_folder"
# Threshhold
batch_hq_threshold = args.threshold
# Define the batch size
batch_size = args.batch

# List all image files in the input folder
image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]

if not os.path.exists(output_folder_hq): 
    os.makedirs(output_folder_hq, exist_ok=True)
if not os.path.exists(output_folder_lq): 
    os.makedirs(output_folder_lq, exist_ok=True)

# Process images in batches
for i in range(0, len(image_files), batch_size):
    batch = image_files[i:i + batch_size]

    # Perform classification for the batch
    results = pipe(images=batch)

    for idx, result in enumerate(results):
        # Extract the prediction scores and labels
        predictions = result
        hq_score = [p for p in predictions if p['label'] == 'hq'][0]['score']

        # Determine the destination folder based on the prediction and threshold
        destination_folder = output_folder_hq if hq_score >= batch_hq_threshold else output_folder_lq

        # Copy the image to the appropriate folder
        shutil.copy(batch[idx], os.path.join(destination_folder, os.path.basename(batch[idx])))
print("Processing complete.")
