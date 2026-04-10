import numpy as np
from ultralytics import YOLO
from PIL import Image

class FruitDetector:
    def __init__(self, model_path):
        try:
            self.model = YOLO(model_path)
        except Exception as e:
            raise Exception(f"Error al cargar el modelo: {e}")

    def detect(self, image_source):
        results = self.model.predict(source=image_source, save=False, conf=0.25)

        result = results[0]

        confidences = result.boxes.conf.cpu().numpy() 

        count = len(confidences)
        
        if count > 0:
            avg_conf = np.mean(confidences)
            min_conf = np.min(confidences)
            max_conf = np.max(confidences)
        else:
            avg_conf = min_conf = max_conf = 0.0

        annotated_frame = result.plot()

        annotated_image = Image.fromarray(annotated_frame[..., ::-1])

        return {
            "count": count,
            "avg_conf": f"{avg_conf:.2f}",
            "min_conf": f"{min_conf:.2f}",
            "max_conf": f"{max_conf:.2f}",
            "annotated_image": annotated_image
        }