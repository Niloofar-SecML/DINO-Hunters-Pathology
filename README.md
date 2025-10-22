# DINO-Hunters-Pathology
Unsupervised glomeruli detection in kidney histopathology using DINOv3 + QuPath extension
This project integrates a **DINOv3-based self-supervised model** into **QuPath** to enable *label-free* glomeruli detection (GS vs Non-GS) in kidney histopathology.

<img width="1440" height="900" alt="Screen Shot 1404-07-30 at 01 28 32" src="https://github.com/user-attachments/assets/ef230573-d233-4a76-99bf-0f6499653673" />


## Problem Statement
Labeling pathology images is **expensive, time-consuming, and error-prone**.  
We use **self-supervised learning (SSL)** with DINOv3 to learn robust features **without manual labels**.

## Method (High-level)
1. **Dataset:** KPMP kidney pathology (WSI → tiles).  
2. **Domain Adaptation:** DINOv3 self-supervised pretraining on KPMP tiles.  
3. **Feature Use:** Embeddings for clustering / visualization; optional linear probe.  
4. **QuPath Extension:** “**DINO Hunters**” runs inside QuPath → one-click detection.

## QuPath Extension (How to use)
- Copy files from `qupath_extension/` into your QuPath extensions folder.
- In QuPath: `Extensions → DINO Hunters → Run` on the selected region.

## Repo Layout
See folders: `dataset/`, `qupath_extension/`, `notebook/`, `model/`, `demo/`.

## Demo
- Screenshots in `/demo/screenshots/`
- (If large) Video link: <add Google Drive / YouTube link>

## Notes
- Do **not** commit full KPMP data (size/privacy). Provide **small samples** only.
