# Tutorial 09 — Object Detection using SSD and YOLO (PyTorch)

## Objective

Implement SSD (Single Shot MultiBox Detector) and YOLO object detection architectures in PyTorch, then compare custom models trained from scratch with pretrained models fine-tuned for bottle detection.

## Dataset

**Bottle Object Detection Dataset**

- Total images: 150
- Training: 105 images
- Validation: 22 images
- Testing: 23 images
- Class: Bottle
- Annotations: YOLO-format bounding boxes sourced from a public dataset
- Framework: PyTorch / Torchvision and Ultralytics

## Implementation

The original tutorial was implemented using two simplified custom detection architectures:

- **Custom SSD:** CNN backbone, multiscale feature maps, classification and bounding-box regression heads, anchor matching, and simplified detection losses.
- **Custom YOLO:** CNN backbone, a 13 × 13 detection grid, three boxes per cell, and simplified objectness, classification, and box regression losses.

The output shapes were verified with dummy inputs before training.

## Experiments

### Task 1 — Custom SSD and YOLO

Both custom models were trained from scratch for 15 epochs on the bottle dataset. Their training and validation losses were recorded, and their predictions were evaluated using mAP.

| Model | Test mAP@0.5 | Test mAP@0.5:0.95 |
|---|---:|---:|
| Custom SSD | 68.52% | 21.32% |
| Custom YOLO | 5.78% | 1.71% |

### Task 2 — Fine-Tuning Pretrained SSD and YOLO

- **SSD300-VGG16:** COCO-pretrained detector with frozen backbone and fine-tuned detection head; trained for 10 epochs.
- **YOLOv8 Nano:** COCO-pretrained model fine-tuned on the bottle dataset for 20 epochs.

| Model | Test mAP@0.5 | Test mAP@0.5:0.95 |
|---|---:|---:|
| Pretrained SSD300-VGG16 | 93.55% | 74.36% |
| Pretrained YOLOv8n | **94.79%** | **85.89%** |

## Final Model Comparison

| Model | Test mAP@0.5 | Test mAP@0.5:0.95 |
|---|---:|---:|
| Custom SSD | 68.52% | 21.32% |
| Custom YOLO | 5.78% | 1.71% |
| Pretrained SSD300-VGG16 | 93.55% | 74.36% |
| Pretrained YOLOv8n | **94.79%** | **85.89%** |

## Conclusion

Both pretrained models outperformed the simplified custom architectures on the held-out bottle test images. YOLOv8n achieved the highest test mAP@0.5:0.95 of **85.89%**, demonstrating stronger localization performance in this experiment.

The comparison illustrates the value of pretrained detection models on small datasets. The custom models used simplified loss and matching implementations, so the results should not be interpreted as a general comparison of SSD and YOLO.

## Technologies Used

- Python
- PyTorch and Torchvision
- Ultralytics YOLO
- NumPy and Pandas
- Matplotlib
- Google Colab

## Author

**Moiz Shahid**

GitHub: [@moiz-shahid](https://github.com/moiz-shahid)
