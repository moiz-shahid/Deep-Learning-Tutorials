# Tutorial 11 — Semantic Segmentation using DeepLabV3 and Mask R-CNN (PyTorch)

## Objective

Implement and evaluate pretrained semantic and instance segmentation models using PyTorch and Torchvision, visualize their predictions, and compare performance on a real pet segmentation dataset.

## Dataset

**Oxford-IIIT Pet Dataset**

- Total selected images: 150
- Training split: 105 images
- Validation split: 22 images
- Test split: 23 images
- Evaluation input resolution: 128 × 128 pixels
- Target: Binary pet foreground versus background
- Ground-truth annotations: Existing Oxford-IIIT Pet segmentation masks

The same data selection and held-out test split from Tutorial 10 were reused. The dataset masks were publicly sourced, not manually annotated for this tutorial.

## Experiments

### Part 1 — Pretrained DeepLabV3

A pretrained **DeepLabV3-ResNet101** semantic segmentation model was loaded from Torchvision. Images were normalized, passed through the model, and decoded into pixel-level semantic predictions. The cat and dog classes were combined into a binary pet foreground mask to compare against ground truth.

The original tutorial PDF calls the method DeepLabV3+, but its supplied Torchvision architecture is DeepLabV3.

### Task 1 — Evaluate Pretrained Segmentation on Real Images

DeepLabV3 was evaluated on **23 held-out pet images**, with no additional model training or fine-tuning. The notebook visualizes original images, ground-truth masks, semantic masks, and segmentation overlays.

### Task 2 — Implement Mask R-CNN

A pretrained **Mask R-CNN ResNet50-FPN** instance segmentation model was implemented using Torchvision inference. The model produces bounding boxes, class labels, confidence scores, and individual object masks.

Cat and dog instances with confidence scores of at least **0.5** were retained, and their predicted masks were merged into a single binary pet foreground mask for evaluation against the same test images.

## Final Model Comparison

| Test Metric | DeepLabV3-ResNet101 | Mask R-CNN ResNet50-FPN |
|---|---:|---:|
| Pixel Accuracy | **93.45%** | 91.43% |
| Dice Score | **86.54%** | 80.09% |
| IoU | **80.18%** | 74.53% |

Results are average per-image metrics on the 23-image test split, not segmentation mAP.

## Analysis

DeepLabV3 achieved higher pixel accuracy, Dice, and IoU on this dataset. It directly assigns semantic class labels to pixels, whereas Mask R-CNN predicts and filters individual object instances before their masks are combined.

Visual inspection showed that Mask R-CNN sometimes returned no retained cat or dog masks at the chosen confidence threshold, while DeepLabV3 generally covered pet regions more consistently.

These results compare pretrained inference under the specified evaluation settings; they do not establish which architecture performs best across other datasets, confidence thresholds, or after fine-tuning.

## Conclusion

Both DeepLabV3 and Mask R-CNN were successfully implemented and evaluated in PyTorch. **DeepLabV3-ResNet101 achieved the highest test Dice (86.54%) and IoU (80.18%)** in this experiment, illustrating the practical differences between semantic and instance segmentation.

## Technologies Used

- Python
- PyTorch and Torchvision
- NumPy and Pandas
- Pillow and Matplotlib
- Google Colab

## Author

**Moiz Shahid**

GitHub: [@moiz-shahid](https://github.com/moiz-shahid)
