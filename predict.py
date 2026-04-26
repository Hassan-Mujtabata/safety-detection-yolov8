from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("runs/detect/runs/my_model/weights/best.pt")

    results = model.predict(
        source="IMG_6881.PNG",  # <-- change this to your image filename
        conf=0.5,
        save=True,
        show=True
    )

    print("Done! Result saved in runs/detect/predict/")