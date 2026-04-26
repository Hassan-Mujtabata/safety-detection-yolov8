# Safety Detection YOLOv8

AI-Based Smart Campus Safety Monitoring System
Course: BCS407 – Artificial Intelligence | Canadian University Dubai

## Project Overview
This project implements a real-time object detection system using YOLOv8m to monitor campus safety. The model detects 15 safety-related classes including safety helmets, emergency exits, fire alarms, and exit violations. All training was performed locally using PyTorch with CUDA acceleration on an NVIDIA RTX 3070 Ti Laptop GPU.

## Step 1 - Install Python 3.12
Download and install Python 3.12 from:
https://www.python.org/downloads/release/python-3129/
Choose Windows installer (64-bit)

## Step 2 - Install Dependencies
Open terminal and run these commands one by one:
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install ultralytics supervision opencv-python

## Step 3 - Download the Dataset
Download the dataset zip file from Hugging Face:
https://huggingface.co/Hassanmujtabat/safety-detection-yolov8/blob/main/safety%20helmet.yolov8.zip

Extract the zip file and place the train folder and data.yaml in the same folder as train.py

## Step 4 - Download Model Weights
Download best.pt and last.pt from Hugging Face:
https://huggingface.co/Hassanmujtabat/safety-detection-yolov8/tree/main

Place both files in this exact path:
runs/detect/runs/my_model/weights/

best.pt — best performing checkpoint, use this for inference
last.pt — final epoch checkpoint

## Step 5 - Run Training (optional, skip if using downloaded weights)
Open terminal in the project folder and run:
py -3.12 train.py

## Step 6 - Run Inference
Place your test image in the project folder and update the image filename in predict.py, then run:
py -3.12 predict.py

Results will be saved in runs/detect/predict/

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
- Parameters: 25.8M (YOLOv8m)

## Training Details
- Model: YOLOv8m (medium)
- Epochs: 50
- Batch Size: 16
- Image Size: 640x640
- Dataset: 1,672 images, 15 classes
- GPU: NVIDIA RTX 3070 Ti Laptop GPU (8GB VRAM)
- Framework: PyTorch 2.5.1 + CUDA 12.1
- Python: 3.12

## Repository Structure
```
project/
├── train.py               # Training script
├── predict.py             # Inference script
├── run_once_to_download.py # Downloads base YOLOv8m weights
├── data.yaml              # Dataset configuration
└── runs/
    └── detect/
        └── runs/
            └── my_model/
                ├── results.png
                ├── results.csv
                ├── confusion_matrix_normalized.png
                ├── BoxPR_curve.png
                ├── BoxF1_curve.png
                ├── labels.jpg
                └── weights/
                    ├── best.pt  (download from Hugging Face)
                    └── last.pt  (download from Hugging Face)
```

## Ethical Considerations
- All human faces in the dataset were blurred prior to training
- No personal data or license plates were collected
- System intended for safety monitoring purposes only
## Contributors
- Hassan Mujtaba (20220002085)
- Leanne Jessica Rodrigo (20210001983)
- Khaled Riyan (20220001526)
- Izaan Shaikh (20220001735)

Canadian University Dubai — BCS407 Artificial Intelligence, 2026
