# Tutorial 06 — Transfer Learning using PyTorch

## Objective

This tutorial demonstrates image classification using pretrained Convolutional Neural Networks and transfer learning with PyTorch.

The objectives include:

- Loading pretrained CNN architectures
- Preprocessing images for pretrained models
- Predicting the top five ImageNet classes
- Comparing different pretrained architectures
- Applying transfer learning to a new dataset
- Evaluating model performance

## Part 1 — Predictions using Pretrained Models

VGG16 and ResNet50 pretrained on ImageNet were used to classify an uploaded image.

### Results

| Model | Top Prediction | Probability |
|---|---|---:|
| VGG16 | Barracouta | 80.22% |
| ResNet50 | Barracouta | 64.48% |

Both models predicted the same class but assigned different probabilities.

## Part 2 — Comparing Pretrained Architectures

Three additional pretrained models were evaluated: AlexNet, ResNet101, and MobileNetV2.

| Model | Top Prediction | Probability |
|---|---|---:|
| AlexNet | Barracouta | 48.83% |
| ResNet101 | Barracouta | 89.56% |
| MobileNetV2 | Barracouta | 23.33% |

All five pretrained models agreed on the top predicted class.

ResNet101 assigned the highest probability for this particular image. However, a higher prediction probability does not necessarily indicate better overall classification accuracy.

## Part 3 — Transfer Learning on MNIST

Transfer learning was implemented using a pretrained ResNet18 model on the MNIST handwritten digit dataset.

### Implementation

- Loaded ResNet18 with pretrained ImageNet weights.
- Froze the pretrained feature-extraction layers.
- Replaced the original 1,000-class output layer with a 10-class classifier.
- Converted grayscale MNIST images to three-channel RGB format.
- Resized images to 224 × 224 pixels.
- Trained the new classification layer using Adam and Cross-Entropy Loss.

### Dataset

| Dataset | Samples |
|---|---:|
| Training | 5,000 |
| Testing | 1,000 |

### Training Results

| Metric | Result |
|---|---:|
| Epochs | 5 |
| Final Training Accuracy | 94.10% |
| Final Training Loss | 0.2755 |
| Test Accuracy | **92.30%** |
| Test Loss | 0.3155 |

The training accuracy increased throughout the five epochs, while training loss decreased consistently.

The pretrained ResNet18 feature extractor successfully supported classification of handwritten digits after training a new output layer.

## Conclusion

This tutorial demonstrated the use of pretrained CNNs for image classification and the application of transfer learning to a different dataset.

VGG16, ResNet50, AlexNet, ResNet101, and MobileNetV2 were compared using their top-five ImageNet predictions.

Transfer learning was implemented using ResNet18 on MNIST, achieving **92.30% test accuracy** after five training epochs.

## Technologies Used

- Python
- PyTorch
- torchvision
- NumPy
- Matplotlib
- Google Colab

## Files

`DL_Tutorial_6.ipynb` — Complete PyTorch implementation, pretrained model comparisons, transfer-learning experiment, results, and visualizations.

## Author

**Moiz Shahid**

GitHub: [@moiz-shahid](https://github.com/moiz-shahid)
