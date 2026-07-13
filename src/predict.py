from pathlib import Path

import torch
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification


MODEL_NAME = "eslamxm/vit-base-food101"


def load_model(model_name: str = MODEL_NAME):
    processor = AutoImageProcessor.from_pretrained(model_name)
    model = AutoModelForImageClassification.from_pretrained(model_name)
    model.eval()
    return processor, model


def predict_image(image_path: str, top_k: int = 5):
    processor, model = load_model()
    image = Image.open(Path(image_path)).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        probabilities = outputs.logits.softmax(dim=-1)[0]

    top = torch.topk(probabilities, k=top_k)
    results = []
    for score, class_id in zip(top.values, top.indices):
        label = model.config.id2label[int(class_id)]
        results.append({"label": label, "score": float(score)})
    return results


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Predict food category from an image.")
    parser.add_argument("image", help="Path to a food image")
    parser.add_argument("--top-k", type=int, default=5, help="Number of predictions to show")
    args = parser.parse_args()

    for item in predict_image(args.image, top_k=args.top_k):
        print(f"{item['label']}: {item['score']:.3f}")
