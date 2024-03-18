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
    parser.add_argument("--image", type=str, default="test/01.jpg", help="Image")
    return parser.parse_args()
args = get_args()

pipe = pipeline("image-classification", model="shadowlilac/aesthetic-shadow-v2", device=f"cuda:{args.device}")

# Input image file
single_image_file = args.image

result = pipe(images=[single_image_file])

prediction_single = result[0]
print("High Quality: " + str(round([p for p in prediction_single if p['label'] == 'hq'][0]['score'], 2)) )
