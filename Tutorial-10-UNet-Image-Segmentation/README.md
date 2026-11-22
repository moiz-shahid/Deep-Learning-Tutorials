# Tutorial 10 — Image Segmentation using U-Net (PyTorch)

## Objective

Implement a custom U-Net for binary image segmentation using PyTorch, evaluate its predictions, and investigate the effects of network depth and learning rate.

## Datasets

**Synthetic Segmentation Dataset**
- 100 generated images with rectangular foreground masks
- Training: 80 images
- Validation: 20 images
- Image size: 128 × 128

**Oxford-IIIT Pet Dataset**
- 150 selected pet images with existing segmentation masks
- Training: 105 images
- Validation: 22 images
- Testing: 23 images
- Image size: 128 × 128
- Task: Binary pet-versus-background segmentation

The Oxford-IIIT Pet annotations are publicly sourced. Independent manual labeling, requested in the tutorial assignment, was not demonstrated in this experiment.

## Experiments

### Original U-Net on Synthetic Data

A custom U-Net was implemented with an encoder, bottleneck, decoder, and skip connections. It was trained for 20 epochs with Adam and BCEWithLogitsLoss.

| Validation Metric | Result |
|---|---:|
| Pixel Accuracy | 99.96% |
| Dice Score | 99.75% |
| IoU | 99.50% |

### Task 1 — U-Net on Real Pet Images

The same U-Net was trained from scratch on 150 selected Oxford-IIIT Pet images using a learning rate of 0.0001 for 20 epochs.

- Best validation loss: **0.5267** (epoch 14)
- Highest recorded validation Dice: **66.82%** (epoch 18)
- Highest recorded validation IoU: **51.71%** (epoch 18)

These peak metrics are from a different epoch than the lowest-validation-loss checkpoint.

### Task 2 — U-Net Architecture Comparison

A deeper U-Net with three encoder and decoder stages was compared against the original two-stage model on the same data split.

| Metric | Original U-Net | Deeper U-Net |
|---|---:|---:|
| Parameters | 1,862,849 | 7,697,345 |
| Validation Loss | 0.5267 | **0.4806** |
| Validation Dice | 64.61% | **70.03%** |
| Validation IoU | 50.11% | **54.63%** |
| Pixel Accuracy | 73.34% | **78.26%** |

Metrics are measured at each model's selected lowest-validation-loss checkpoint.

### Task 3 — Learning Rate Comparison

The deeper U-Net was trained for 20 epochs with three different learning rates.

| Learning Rate | Validation Loss | Dice | IoU |
|---|---:|---:|---:|
| 0.001 | 0.5083 | **69.23%** | **53.87%** |
| 0.0001 | **0.4857** | 68.47% | 53.49% |
| 0.00001 | 0.5956 | 0.00% | 0.00% |

The learning rate of **0.0001** was selected using the lowest-validation-loss criterion and evaluated on 23 held-out images.

**Final Test Results**

| Metric | Result |
|---|---:|
| Test Loss | 0.5429 |
| Pixel Accuracy | 74.15% |
| Dice Score | **64.71%** |
| IoU | **50.15%** |

## Conclusion

The U-Net achieved near-perfect segmentation on simple synthetic rectangles but lower performance on real pet images. Increasing encoder-decoder depth improved validation Dice and IoU under the tested conditions. Learning rate influenced convergence and predicted mask quality; 0.0001 gave the lowest validation loss, while 0.001 achieved slightly higher validation overlap scores.
