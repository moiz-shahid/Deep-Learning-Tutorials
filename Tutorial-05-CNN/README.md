# Tutorial 05 — Convolutional Neural Network (CNN) using PyTorch

## Objective

This tutorial focuses on implementing and evaluating Convolutional Neural Networks (CNNs) for image classification using the CIFAR-10 dataset and PyTorch.

The tutorial covers CNN architecture, convolution operations, feature extraction, model training, performance evaluation, and techniques for improving accuracy and reducing overfitting.

## Dataset

**CIFAR-10** contains 60,000 RGB images of size 32 × 32 pixels, divided into 10 classes.

- Training images: 50,000
- Testing images: 10,000

## Task 1 — Different CNN Architectures

Different CNN configurations were tested by changing kernel sizes, convolutional layers, filters, and fully connected layers.

| Model | Test Accuracy | Test Loss |
|---|---:|---:|
| Baseline CNN (3×3) | 67.84% | 0.9194 |
| Task 1A — 5×5 Kernels | 67.59% | 0.9231 |
| Task 1B — Deeper CNN | 76.30% | 0.7691 |
| Task 1C — More FC Layers | 75.95% | 0.8315 |

The deeper CNN with additional convolutional layers and filters achieved the highest accuracy among the architecture experiments.

## Task 2 — Improving Model Accuracy

The CNN was improved using:

- Data augmentation
- Batch Normalization
- Dropout
- Weight decay
- Early Stopping

The improved model achieved:

- **Test Accuracy: 80.31%**
- **Test Loss: 0.5757**

This represents an improvement of **12.47 percentage points** over the original baseline.

## Task 3 — Reducing Overfitting and Underfitting

Training and validation accuracy/loss curves were analyzed to identify generalization problems.

The deeper CNN showed signs of overfitting due to the gap between training and test accuracy.

Data augmentation, Dropout, Batch Normalization, and weight decay were applied to improve generalization.

The final model demonstrated improved validation performance without clear evidence of severe overfitting during the observed training period.

Early Stopping was implemented but did not trigger within the 30 training epochs.

## Final Results

| Metric | Result |
|---|---:|
| Baseline Test Accuracy | 67.84% |
| Improved Test Accuracy | 80.31% |
| Improved Test Loss | 0.5757 |
| Training Epochs | 30 |

## Technologies Used

- Python
- PyTorch
- torchvision
- NumPy
- Matplotlib
- Google Colab

## Files

`DL_Tutorial_5.ipynb` — Complete PyTorch implementation, architecture experiments, training results, comparison graphs, and conclusions.

## Author

**Moiz Shahid**

GitHub: [@moiz-shahid](https://github.com/moiz-shahid)
