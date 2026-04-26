# Safety Detection YOLOv8

AI-Based Smart Campus Safety Monitoring System  
Course: BCS407 – Artificial Intelligence | Canadian University Dubai

## Project Overview
This project implements a real-time object detection system using YOLOv8m to monitor campus safety. The model detects 15 safety-related classes including safety helmets, emergency exits, fire alarms, and exit violations. All training was performed locally using PyTorch with CUDA acceleration on an NVIDIA RTX 3070 Ti Laptop GPU.

## Classes Detected
1. Fire Alarm
2. Left Exit
3. Right Exit
4. Left/Right Exit
5. Straight Exit
6. Blocked Emergency Exit
7. Boxes Blocking Exit
8. Emergency Exit Door
9. Exit Block Violation
10. Exit-Sign
11. Head
12. Helmet
13. Objects Blocked Emergency Exit
14. Person
15. Sign

## Model Performance
- mAP@0.5: 0.978 (97.8%)
- Precision: 0.953
- Recall: 0.946
- F1 Score: 0.95

## Training Details
- Model: YOLOv8m (25.8M parameters)
- Epochs: 50
- Batch Size: 16
- Image Size: 640x640
- Dataset: 1,672 images, 15 classes
- GPU: NVIDIA RTX 3070 Ti Laptop GPU (8GB VRAM)
- Framework: PyTorch 2.5.1 + CUDA 12.1
- Python: 3.12

## Installation

### Requirements
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install ultralytics supervision opencv-python
```

### Run Training
```bash
py -3.12 train.py
```

### Run Inference
```bash
py -3.12 predict.py
```

## Files
- `train.py` — training script
- `predict.py` — inference script
- `data.yaml` — dataset configuration
- `best.pt` — trained model weights
- `results.csv` — training metrics per epoch

## Ethical Considerations
- All human faces in the dataset were blurred prior to training
- No personal data or license plates were collected
- System intended for safety monitoring purposes only
