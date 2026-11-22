# Tutorial 08 — Object Detection with Faster R-CNN (PyTorch)

Implementation of the university Deep Learning Tutorial 8 in **PyTorch / Torchvision**, using Google Colab. The notebook covers the architecture of Faster R-CNN, ROI pooling, IoU, precision, recall, AP and mAP, followed by three experiments.

## Contents

- **Original tutorial:** Custom CNN feature extractor, RPN objectness and box-regression outputs, ROI pooling, classification and regression heads, illustrative forward pass, and evaluation metric examples. The assembled original model is an *architecture demonstration*, not a complete trainable detector.
- **Task 1 — Backbone depth:** Trainable Faster R-CNN with 3- and 4-convolution backbones on Penn-Fudan pedestrians; compare training loss, parameters and validation mAP@0.5.
- **Task 2 — Inference:** Visualize the 3-layer model's detections on Penn-Fudan validation images at different score thresholds, compare with ground-truth boxes and inspect IoU.
- **Task 3 — Bottle detection:** Train a 3-layer custom-backbone Faster R-CNN on 150 bottle images with converted bounding-box annotations, evaluate with COCO-style mAP, and visualize held-out test detections.

## Results

### Task 1: Penn-Fudan (preliminary, 3 epochs)

| Backbone | Parameters | Final training loss | Validation mAP@0.5 |
|---|---:|---:|---:|
| 3 convolution layers | 14,886,101 | 0.4085 | 28.45% |
| 4 convolution layers | 15,476,181 | 0.4001 | 17.28% |

The 3-layer variant achieved higher validation AP despite slightly higher training loss.

### Task 2: Prediction visualization

On five randomly selected validation images (six labeled pedestrians total), the 3-layer model produced **no displayed detections at score thresholds 0.3, 0.5 or 0.7**. This demonstrates the distinction between confidence-ranked AP and thresholded visualization. The test is a qualitative sample, not a substitute for full validation evaluation.

### Task 3: Bottle object detection

| Metric | Recorded value |
|---|---:|
| Images | 150 |
| Train / validation / test | 105 / 22 / 23 |
| Backbone | 3 convolution layers, trained from scratch |
| Epochs run | 15 |
| Selected checkpoint | Epoch 11 (best validation mAP@0.5, first occurrence) |
| Final-epoch training loss | 0.1831 |
| Test mAP@0.5 (selected checkpoint) | **79.21%** |
| Test mAP@0.5:0.95 (selected checkpoint) | **35.70%** |

At a display threshold of 0.3, three predicted boxes were displayed across five randomly selected test images containing six annotated bottles. Metrics are from the executed notebook and depend on this small dataset and split.

## Dataset and annotation provenance

- **Task 1/2:** Penn-Fudan pedestrian dataset with provided mask annotations, converted to bounding boxes at load time.
- **Task 3:** A subset of 150 images selected from a publicly sourced bottle dataset. Pre-existing segmentation labels were converted into YOLO-format bounding boxes and the four original bottle categories were merged into one `bottle` class. **These labels were not manually annotated from scratch by the notebook author.** The original dataset's source/provenance notes should be retained when distributing the data.
- The original tutorial assignment requests labeling approximately 150 images using an annotation tool. The provided notebook demonstrates conversion, verification, training and testing; independent manual labeling has **not** been documented.

The Task 3 dataset archive is not included here, to keep the code repository focused on the notebook. To reproduce Task 3, provide the referenced dataset archive and preserve its provenance notes.

## Running in Colab

1. Open [`DL_Tutorial_8.ipynb`](DL_Tutorial_8.ipynb) in Google Colab and select a GPU runtime.
2. Run the notebook top-to-bottom. The earlier architecture and Penn-Fudan tasks run before Task 3.
3. For Task 3, upload `BottleDataset_150_Clean.zip` when prompted. Expected internal layout:

   ```text
   BottleDataset/
   ├── images/    # 150 images
   └── labels/    # corresponding YOLO .txt bounding-box files
   ```

4. Install the required packages when the notebook prompts (`torchmetrics`, `pycocotools`). Other libraries include PyTorch, Torchvision, NumPy, Matplotlib, scikit-learn, Pillow and pandas.
5. The notebook writes model checkpoints and CSV outputs into the ephemeral Colab filesystem. Copy important outputs to Google Drive before the runtime resets.

**Note:** Model weights, generated datasets and other large files are not tracked in this repository.

## Implementation notes

- Torchvision Faster R-CNN implements anchor generation, RPN proposal filtering, NMS, detection losses and ROI Align. The illustrative custom model near the beginning uses manual ROIs and is not itself an end-to-end trained detector.
- Task 1 is a short experiment with three training epochs; differences should not be interpreted as definitive architectural comparisons.
- Task 3 used validation mAP@0.5 to select a checkpoint, while the best validation mAP@0.5:0.95 occurred later in training. Final test metrics correspond to the restored checkpoint.

## Author

[moiz-shahid](https://github.com/moiz-shahid) — Deep Learning Tutorials
