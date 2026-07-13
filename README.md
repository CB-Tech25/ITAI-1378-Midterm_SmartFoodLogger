# Smart Food Logger: Image-Based Meal Classification

Team member: Lakwan Bonsu & Courtney Bernard

Course: ITAI 1378 - Computer Vision and Artificial Intelligence

Project tier: Tier 2 - uses a pretrained computer vision model and a public dataset, with planned fine-tuning or evaluation on a scoped subset of Food-101.

## Problem Statement

Many people who want to eat healthier or keep track of their nutrition struggle to log every meal consistently. Manually searching for foods and entering meals can be time-consuming, so people often forget to log their meals or stop tracking altogether. This can make it harder to monitor eating habits and reach health or fitness goals. 

## Solution Overview

Our Smart Food Logger uses an image classification model to recognize food from a photo and automatically create a meal log. This makes meal tracking quicker and easier, and more convenient for users.

Input Food Image -> Image Preprocessing -> Food Classification Model -> Predicted Food Label -> Meal Log Output

## Technical Approach

Computer vision task: image classification.

Primary model: `eslamxm/vit-base-food101`, a Vision Transformer model fine-tuned for Food-101 image classification.

Backup model options:

* `dwililiya/food101-model-classification` - EfficientNet-B0 model for Food-101.
* `onnx-community/swin-finetuned-food101-ONNX` - ONNX Swin Transformer option for faster inference or dependency issues.

Frameworks:

* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* PIL/Pillow for image handling
* Gradio for an optional demo interface

The reason for using image classification is that the goal is to identify the food category from a single photo. A pretrained Food-101 model keeps the project feasible because training a model from scratch would require more compute and time than the course project allows.

## Dataset Plan

Dataset: `ethz/food101` from Hugging Face Datasets.

Source: https://huggingface.co/datasets/ethz/food101

Dataset details:

* 101 food categories
* About 101,000 images total
* 750 training images per class
* 250 test/validation images per class
* Labels are food category names such as pizza, ramen, hamburger, apple pie, and sushi

Scope plan:

* Start with the full dataset for baseline evaluation.
* If compute is slow, reduce the project to a 10-20 class subset.
* Use basic preprocessing: resize images, normalize pixel values, and apply light augmentation if fine-tuning.

## Success Metrics

Primary metric:

* Top-1 classification accuracy target: at least 85 percent on the selected evaluation set.

Secondary metrics:

* Inference time target: under 2 seconds per image on Google Colab.
* Demo usability: upload one image and receive a readable food label without manual steps.

## Week-by-Week Plan

|Week|Task|Milestone|
|-|-|-|
|1|Set up GitHub repo, install dependencies, load Food-101 dataset|Dataset ready|
|2|Load pretrained model and run baseline inference on sample images|Model working|
|3|Evaluate model on a small test subset and optionally fine-tune 10-20 classes|Baseline metrics recorded|
|4|Improve results with preprocessing, augmentation, or model swap if needed|Accuracy improved|
|5|Build a simple demo with Gradio or a Colab widget|Demo ready|
|6|Final testing, documentation, slides, and AI usage log|Repo and proposal complete|
|7|Present project in class|Presentation complete|

## Resources Needed

Compute:

* Google Colab free tier
* Backup: Kaggle GPU notebook

Software:

* Python 3.10+
* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* Pillow
* Gradio

Estimated cost:

* $0 using free compute and public datasets.

## Risks and Mitigation

|Risk|Probability|Mitigation|
|-|-|-|
|Accuracy is lower than expected|Medium|Evaluate another pretrained model, add augmentation, or reduce to a cleaner 10-20 class subset|
|Colab is too slow or crashes|Medium|Reduce dataset size, use batch inference, or switch to Kaggle GPU|
|Model dependency errors|Medium|Use the EfficientNet backup model or ONNX Swin model|
|Calorie estimates are unreliable|High|Keep calorie output as a simple demo feature and make classification accuracy the main project goal|
|Food images contain multiple dishes|Medium|Limit demo to single-dish images and document this limitation|

## Repository Structure

```text
ITAI 1378 Midterm\_SmartFoodLogger/
├── README.md
├── requirements.txt
├── data/
│   └── README.md
├── docs/
│   ├── ai\_usage\_log.md
│   ├── proposal\_slides.md
│   ├── risks.md
│   └── system\_diagram.mmd
├── notebooks/
│   └── 01\_exploration.ipynb
└── src/
    └── predict.py
```

## References

* Food-101 dataset: https://huggingface.co/datasets/ethz/food101
* ViT Food-101 model: https://huggingface.co/eslamxm/vit-base-food101
* EfficientNet Food-101 backup model: https://huggingface.co/dwililiya/food101-model-classification
* ONNX Swin Food-101 backup model: https://huggingface.co/onnx-community/swin-finetuned-food101-ONNX

