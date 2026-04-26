"""
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8s.pt")

    model.train(
        data="data.yaml",
        epochs=50,
        imgsz=640,
        batch=32,
        device="0",
        workers=8,
        project="runs",
        name="my_model",
        exist_ok=True,
        cache=True,
        amp=True
    )

    print("Training done. Weights saved to runs/my_model/weights/best.pt")


    """
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("runs/detect/runs/my_model/weights/last.pt")

    model.train(
        data="data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        device="0",
        workers=8,
        project="runs",
        name="my_model",
        exist_ok=True,
        cache=False,
        amp=True,
        resume=True
    )

    print("Training done. Weights saved to runs/my_model/weights/best.pt")