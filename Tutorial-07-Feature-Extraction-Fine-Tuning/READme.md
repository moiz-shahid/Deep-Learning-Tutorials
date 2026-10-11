# Tutorial 07 — Feature Extraction vs. Fine-Tuning using PyTorch

## Objective

This tutorial explores transfer learning using pretrained Convolutional Neural Networks (CNNs), comparing feature extraction and fine-tuning approaches using PyTorch.

The experiments evaluate VGG16, ResNet50, and a custom CNN on the Hymenoptera dataset.

## Dataset

**Hymenoptera Dataset — Ants vs. Bees**

- Training Images: 244
- Validation Images: 153
- Classes: Ants and Bees
- Image Size: 224 × 224
- Framework: PyTorch

## Experiments

### Experiment 1 — VGG16 Feature Extraction

Pretrained VGG16 convolutional layers were frozen, and a new binary classification head was trained.

The original model achieved **94.12% validation accuracy** with **0.7884 validation loss** at the selected checkpoint.

An improved classifier with fewer neurons, a smaller learning rate, and weight decay achieved **94.77% validation accuracy** and **0.2206 validation loss**.

### Experiment 2 — ResNet50 Fine-Tuning

The final residual block (`layer4`) and new classification head were trained while earlier layers remained frozen.

- Validation Accuracy: **96.08%**
- Validation Loss: **0.0988**

### Experiment 3 — ResNet50 Feature Extraction

The pretrained ResNet50 backbone was frozen, and only the new classifier was trained.

- Validation Accuracy: **94.77%**
- Validation Loss: **0.4439**

### Experiment 4 — VGG16 Fine-Tuning

The final convolutional block of VGG16 was unfrozen and trained alongside a new classifier.

- Validation Accuracy: **94.12%**
- Validation Loss: **0.2252**

### Experiment 5 — Custom CNN

A custom CNN was developed and trained from scratch without pretrained weights.

- Validation Accuracy: **71.90%**
- Validation Loss: **0.5725**

The custom CNN performed substantially worse than the pretrained models, demonstrating the benefits of transfer learning with limited training data.

### Experiment 6 — Improved ResNet50 Fine-Tuning

The original ResNet50 fine-tuning configuration was modified using:

- Smaller learning rates
- Dropout regularization
- Increased weight decay
- Early Stopping
- Longer training duration

The improved model achieved:

- Validation Accuracy: **96.73%**
- Validation Loss: **0.1028**

## Final Model Comparison

| Model | Validation Accuracy | Validation Loss |
|---|---:|---:|
| Original VGG16 Feature Extraction | 94.12% | 0.7884 |
| Improved VGG16 Feature Extraction | 94.77% | 0.2206 |
| ResNet50 Feature Extraction | 94.77% | 0.4439 |
| ResNet50 Fine-Tuning | 96.08% | **0.0988** |
| VGG16 Fine-Tuning | 94.12% | 0.2252 |
| Custom CNN | 71.90% | 0.5725 |
| Improved ResNet50 Fine-Tuning | **96.73%** | 0.1028 |

Results are reported at each model's lowest-validation-loss checkpoint.

## Conclusion

The experiments demonstrate the effectiveness of transfer learning on a small image-classification dataset.

Feature extraction provided strong performance with fewer trainable parameters, while ResNet50 fine-tuning achieved higher validation accuracy by adapting pretrained features to the target task.

The custom CNN performed substantially worse than the pretrained models because it had to learn image features from a limited dataset.

The improved ResNet50 configuration achieved the highest validation accuracy of **96.73%**, while the original ResNet50 fine-tuning configuration achieved the lowest validation loss of **0.0988**.

## Technologies Used

- Python
- PyTorch
- torchvision
- NumPy
- Matplotlib
- Google Colab

## Author

**Moiz Shahid**

GitHub: [@moiz-shahid](https://github.com/moiz-shahid)
