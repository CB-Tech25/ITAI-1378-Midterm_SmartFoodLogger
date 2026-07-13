# Smart Food Logger Proposal Slides

## Slide 1 - Title

Smart Food Logger: Image-Based Meal Classification

Lakwan Bonsu

ITAI 1378 - Computer Vision and Artificial Intelligence

Project Tier: Tier 2 - pretrained Food-101 model with evaluation and possible fine-tuning

Speaker notes: Introduce the project as a practical computer vision system that uses food photos to reduce manual meal logging.

## Slide 2 - The Problem

- Manually logging food is time-consuming.
- Users often forget meals or choose the wrong food item.
- People tracking nutrition need a faster way to record meals.
- Example: logging 3 meals per day at 5 minutes each can waste about 15 minutes daily.

Speaker notes: Focus on the practical pain point. This is not trying to solve all nutrition tracking, only the first step: identifying the food.

## Slide 3 - Solution Overview

- User uploads or takes a photo of food.
- A pretrained image classification model predicts the food category.
- The predicted label is used to auto-fill a meal log.
- Optional demo: show a rough calorie estimate or lookup placeholder.

Flow: food photo -> ViT classifier -> food label -> meal log output

Speaker notes: Keep the scope clear. The core deliverable is classification, not perfect calorie estimation.

## Slide 4 - Technical Approach

| Component | Choice |
| --- | --- |
| Computer vision task | Image classification |
| Primary model | `eslamxm/vit-base-food101` |
| Dataset | `ethz/food101` |
| Frameworks | PyTorch, Hugging Face Transformers, Hugging Face Datasets |
| Backup models | EfficientNet-B0 or ONNX Swin Food-101 |

Justification: Food classification directly matches the project goal. A pretrained Food-101 model makes the project feasible without training from scratch.

Speaker notes: Mention that image classification is the correct technique because the desired output is one food category label.

## Slide 5 - Data Plan

- Dataset: Food-101 from Hugging Face (`ethz/food101`)
- Size: about 101,000 images
- Classes: 101 food categories
- Split: 750 training images and 250 test/validation images per class
- Prep: resize, normalize, and optionally augment images
- Scope control: reduce to 10-20 classes if compute is limited

Speaker notes: Point out that this dataset is already labeled, public, and directly related to the project.

## Slide 6 - System Diagram

```text
User uploads food photo
        |
        v
Resize and normalize image
        |
        v
Food classification model
        |
        v
Top predicted food label
        |
        v
Meal log output
        |
        v
Optional calorie estimate
```

Speaker notes: Walk through each step from input to output. Keep it simple and implementation-focused.

## Slide 7 - Success Metrics

| Metric Type | Metric | Target |
| --- | --- | --- |
| Primary | Top-1 classification accuracy | At least 85 percent |
| Secondary | Inference time | Under 2 seconds per image |
| Demo | Single-image upload workflow | Label appears without manual steps |

Speaker notes: Explain that accuracy and speed are measurable, realistic, and tied to user experience.

## Slide 8 - Week-by-Week Plan

| Week | Task | Milestone |
| --- | --- | --- |
| 1 | Set up repo and load Food-101 | Dataset ready |
| 2 | Load pretrained model and run baseline inference | Model working |
| 3 | Evaluate or fine-tune on a subset | Metrics recorded |
| 4 | Improve preprocessing or switch model if needed | Better results |
| 5 | Build simple demo | Demo ready |
| 6 | Final testing, README, slides, AI usage log | Submission ready |
| 7 | Present project | Presentation complete |

Speaker notes: Emphasize that every week ends with a concrete deliverable.

## Slide 9 - Challenges and Backup Plans

| Challenge | Backup Plan |
| --- | --- |
| Accuracy too low | Try Swin or EfficientNet, add augmentation, or reduce to fewer classes |
| Colab too slow | Use 10-20 class subset or Kaggle GPU |
| Multiple foods in one image | Scope demo to single-dish images |
| Calorie estimate unreliable | Keep calories optional and focus on classification |

Speaker notes: Show that the project is realistic because there are practical fallback options.

## Slide 10 - Resources Needed

- Compute: Google Colab free tier
- Backup compute: Kaggle GPU notebook
- Libraries: PyTorch, Transformers, Datasets, Pillow, Gradio
- Dataset: Food-101 from Hugging Face
- Cost: $0 if using free tools

Speaker notes: Close by reinforcing feasibility: public data, pretrained models, free compute, and a scoped deliverable.
