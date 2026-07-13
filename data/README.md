# Dataset Plan

Primary dataset: Food-101 (`ethz/food101`)

Source: https://huggingface.co/datasets/ethz/food101

The dataset contains 101 food categories and about 101,000 total images. Each class has 750 training images and 250 test/validation images. The labels are food category names, making the dataset a strong match for an image classification project.

## Use in This Project

The project will use Food-101 to evaluate and optionally fine-tune a pretrained image classification model. If full-dataset training or evaluation is too slow, the project will use a 10-20 class subset for a realistic course-project scope.

## Preparation Steps

- Load dataset with Hugging Face Datasets.
- Resize images to the model input size.
- Normalize pixel values using the model image processor.
- Apply light augmentation if fine-tuning, such as horizontal flip, small rotation, and brightness changes.

## Data Storage

The dataset should not be committed directly to GitHub. It can be downloaded dynamically through the `datasets` library.
