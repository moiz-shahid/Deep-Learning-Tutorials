# Tutorial 08-A — Object Detection using Pretrained Faster R-CNN (PyTorch)

## Objective

This tutorial explores object detection using COCO-pretrained Faster R-CNN models in PyTorch, including image inference, bounding-box visualization, model comparison, and mAP evaluation.

## Dataset

**Bottle Object Detection Dataset**

- Evaluation images: 150
- Class: Bottle (COCO class ID 44)
- Annotations: Publicly sourced YOLO-format bounding boxes, converted to pixel coordinates
- Framework: PyTorch and torchvision

The models were evaluated without additional training or fine-tuning.

## Experiments

### Task 1 — Test Pretrained Faster R-CNN on an Image

A COCO-pretrained Faster R-CNN ResNet50-FPN model was loaded and tested on an uploaded image.

It detected two objects:
- Person: **99.98%** confidence
- Tie: **99.96%** confidence

Predicted bounding boxes, class labels, and confidence scores were visualized.

### Task 2 — Compare Pretrained Models

Three Faster R-CNN configurations were compared on the same image:

| Model | Parameters | Detections | Inference Time |
|---|---:|---:|---:|
| ResNet50-FPN | 41.76M | 2 | 0.1326 s |
| MobileNetV3-Large-FPN | 19.39M | 2 | 0.0245 s |
| ResNet50-FPN V2 | 43.71M | 2 | 0.1503 s |

All three models detected a person and a tie. MobileNetV3-FPN was the fastest and smallest in this experiment.

ResNet50-FPN V2 is an updated ResNet50 configuration, not a separate backbone family.

### Task 3 — Evaluate Pretrained Models Using mAP

The three models were evaluated on 150 annotated bottle images. The existing YOLO labels were converted to bounding boxes and mapped to the COCO bottle class.

| Model | mAP@0.5 | mAP@0.5:0.95 | Average Time/Image |
|---|---:|---:|---:|
| ResNet50-FPN | 95.97% | 81.00% | 0.1048 s |
| MobileNetV3-Large-FPN | 97.95% | 79.67% | **0.0200 s** |
| ResNet50-FPN V2 | **97.99%** | **87.45%** | 0.1523 s |

## Conclusion

All three pretrained Faster R-CNN models performed well on the bottle dataset. ResNet50-FPN V2 achieved the highest mAP@0.5:0.95, while MobileNetV3-FPN offered the fastest inference.

The results illustrate the trade-off between detection performance and computational efficiency. These metrics describe performance on this particular public dataset; possible overlap with the original pretraining data was not assessed.


