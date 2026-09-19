import random

def predict_image(filepath):
    """
    Load image, preprocess, run through trained model.
    Replace this stub with actual ML pipeline.
    """
    # Example stub: random prediction
    classes = ["melanoma", "nevus", "seborrheic keratosis"]
    prediction = random.choice(classes)
    confidence = round(random.uniform(0.7, 0.95), 2)

    return prediction, confidence
