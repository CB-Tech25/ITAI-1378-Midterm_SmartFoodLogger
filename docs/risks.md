# Risks and Backup Plans

| Risk | Probability | Impact | Backup Plan |
| --- | --- | --- | --- |
| Accuracy is too low on test images | Medium | The demo may feel unreliable | Try the Swin or EfficientNet backup model, reduce to a smaller class subset, and add augmentation |
| Colab runs slowly or crashes | Medium | Training or evaluation may take too long | Use only 10-20 classes, run batch inference, or switch to Kaggle GPU |
| Food image has multiple dishes | Medium | Classification may predict only one item | Scope the project to single-dish images and document this limitation |
| Nutrition estimate is inaccurate | High | Could weaken the project if treated as the main output | Treat calorie estimate as optional demo text and focus grading on image classification |
| Model loading fails | Medium | Demo cannot run | Use the EfficientNet or ONNX backup model |
