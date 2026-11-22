# Deep-Learning-Tutorials

This repository contains implementations of tutorials and practical exercises completed as part of the **Deep Learning** course.

The repository is organized tutorial-wise, with each folder containing the code, experimental results, and related documentation for a specific tutorial.

## Tutorials

### Tutorial 01 - Understanding a Perceptron

This tutorial covers the basic implementation and working of a Perceptron, including:

- Perceptron architecture
- Weights and bias
- Weighted sum
- Activation functions
- Training and testing
- Iris dataset classification
- Manual input and prediction
- Sigmoid activation function

### Tutorial 02 - MLP Classifier

Implementation and analysis of a Multi-Layer Perceptron classifier using the Iris dataset, including experiments with different network architectures and learning rates.

### Tutorial 03 - ANN for MNIST Digit Classification

Implementation and evaluation of an Artificial Neural Network for MNIST handwritten digit classification, including architecture and activation experiments, optimizer comparison, overfitting analysis, Early Stopping, and Dropout regularization.

### Tutorial 04 - Data Augmentation using PyTorch

Implementation of image data augmentation using PyTorch and torchvision. A single JPEG image is transformed using rotation, shear, zoom, horizontal flipping, and brightness adjustment to generate 40 augmented images.

### Tutorial 05 - Convolutional Neural Network (CNN) using PyTorch

Implementation and evaluation of CNN architectures for CIFAR-10 image classification using PyTorch.

Experiments include kernel size comparison, convolutional layers and filters, fully connected architectures, model accuracy improvement, and overfitting reduction using data augmentation and regularization.

The improved CNN achieved **80.31% test accuracy**.

### Tutorial 06 - Transfer Learning using PyTorch

Implementation of image classification using pretrained VGG16, ResNet50, AlexNet, ResNet101, and MobileNetV2 models.

The tutorial includes top-five ImageNet predictions and a transfer-learning experiment using pretrained ResNet18 on the MNIST dataset.

The transfer-learning model achieved **92.30% test accuracy** after five epochs.

### Tutorial 07 - Feature Extraction vs. Fine-Tuning using PyTorch

Comparison of feature extraction and fine-tuning using pretrained VGG16 and ResNet50 models on the Hymenoptera ants-versus-bees dataset.

The tutorial also includes a custom CNN trained from scratch and experiments with improving fine-tuning through learning-rate adjustment, Dropout, weight decay, and Early Stopping.

The highest validation accuracy achieved was **96.73%** using improved ResNet50 fine-tuning.

### Tutorial 08 - Object Detection using Faster R-CNN (PyTorch)

Implementation and evaluation of a custom Faster R-CNN object detection architecture using PyTorch and Torchvision.

The tutorial covers:

- Custom CNN backbone for feature extraction
- Region Proposal Network (RPN)
- Anchor boxes and bounding-box regression
- Region of Interest (ROI) Pooling and ROI Align
- Classification and regression heads
- Intersection over Union (IoU)
- Precision, Recall, Average Precision (AP), and Mean Average Precision (mAP)

**Practical experiments:**

1. **Backbone Architecture Comparison:** Compared Faster R-CNN models with three and four convolutional layers using the Penn-Fudan pedestrian dataset. The three-layer model achieved **28.45% validation mAP@0.5**, outperforming the four-layer model.

2. **Real-Image Object Detection:** Tested the trained pedestrian detector on randomly selected validation images, visualized bounding boxes, compared confidence thresholds, and examined prediction quality.

3. **Custom Bottle Detection:** Prepared a 150-image dataset from publicly available bottle images and annotations, converted bounding-box labels into PyTorch-compatible coordinates, and trained a custom Faster R-CNN model using a three-layer CNN backbone.

**Final bottle detection results:**

| Metric | Result |
|---|---:|
| Training Images | 105 |
| Validation Images | 22 |
| Testing Images | 23 |
| Training Epochs | 15 |
| Test mAP@0.5 | **79.21%** |
| Test mAP@0.5:0.95 | **35.70%** |

The experiments demonstrate how backbone architecture, confidence thresholds, and training conditions influence object detection performance.

## Repository Structure

```text
Deep-Learning-Tutorials/
│
├── Tutorial-01-Perceptron/
│   ├── Perceptron.py
│   └── README.md
│
├── Tutorial-02-MLP/
│   ├── DL_Tutorial_2.ipynb
│   └── README.md
│
├── Tutorial-03-ANN-MNIST/
│   ├── DL_Tutorial_3.ipynb
│   └── README.md
│
├── Tutorial-04-Data-Augmentation/
│   ├── DL_Tutorial_4.ipynb
│   └── README.md
│
├── Tutorial-05-CNN/
│   ├── DL_Tutorial_5.ipynb
│   └── README.md
│
├── Tutorial-06-Transfer-Learning/
│   ├── DL_Tutorial_6.ipynb
│   └── README.md
│
├── Tutorial-07-Feature-Extraction-Fine-Tuning/
│   ├── DL_Tutorial_7.ipynb
│   └── README.md
│
├── Tutorial-08-Faster-RCNN-Object-Detection/
│   ├── DL_Tutorial_8.ipynb
│   └── README.md
│
└── README.md
```



---

Additional deep learning tutorials and practical experiments will be added as the course progresses.
