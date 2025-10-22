import torch
from torchvision import transforms
from torchvision.models import vit_b_16
from PIL import Image
import numpy as np
import os

def run(image_path):
    print("[DINO Hunters] Starting feature extraction...")
    
    # Load pretrained DINOv3 model (you can replace this with your fine-tuned one)
    model = vit_b_16(weights=None)
    model.eval()

    transform = transforms.Compose([
        transforms.Resize((518, 518)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    # Load and preprocess the image
    img = Image.open(image_path).convert("RGB")
    img_t = transform(img).unsqueeze(0)

    with torch.no_grad():
        features = model.forward_features(img_t)
        emb = features[:, 0, :].cpu().numpy()

    # Save embedding to results folder
    os.makedirs("results", exist_ok=True)
    np.save("results/embedding.npy", emb)
    print("[DINO Hunters] Embedding extracted successfully and saved to 'results/embedding.npy'")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python dynohunters.py <path_to_image>")
    else:
        run(sys.argv[1])
