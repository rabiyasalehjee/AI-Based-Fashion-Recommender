from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def get_fashion_suggestions(image_path: str):
    image = Image.open(image_path).convert("RGB")

    prompts = [
        "a trendy outfit",
        "a casual streetwear look",
        "a formal suit",
        "a stylish summer look",
        "a cozy winter outfit",
        "an outdated fashion style"
    ]

    inputs = processor(text=prompts, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1).detach().numpy()[0]

    ranked = sorted(zip(prompts, probs), key=lambda x: x[1], reverse=True)
    suggestions = [desc for desc, score in ranked[:3]]
    return suggestions
