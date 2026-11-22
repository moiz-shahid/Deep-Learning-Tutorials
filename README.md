# Deep-Learning-Tutorials

This repository contains implementations of tutorials and practical exercises completed as part of the **Deep Learning** course.

The repository is organized tutorial-wise, with each folder containing the code and related material for a specific tutorial.

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

### Tutorial 05 — Convolutional Neural Network (CNN) using PyTorch

Implementation and evaluation of CNN architectures for CIFAR-10 image classification using PyTorch.

Experiments include kernel size comparison, convolutional layers and filters, fully connected architectures, model accuracy improvement, and overfitting reduction using data augmentation and regularization.

The improved CNN achieved **80.31% test accuracy**.

### Tutorial 06 — Transfer Learning using PyTorch

Implementation of image classification using pretrained VGG16, ResNet50, AlexNet, ResNet101, and MobileNetV2 models.

The tutorial includes top-five ImageNet predictions and a transfer-learning experiment using pretrained ResNet18 on the MNIST dataset.

The transfer-learning model achieved **92.30% test accuracy** after five epochs.

### Tutorial 07 — Feature Extraction vs. Fine-Tuning using PyTorch

Comparison of feature extraction and fine-tuning using pretrained VGG16 and ResNet50 models on the Hymenoptera ants-versus-bees dataset.

The tutorial also includes a custom CNN trained from scratch and experiments with improving fine-tuning through learning-rate adjustment, Dropout, weight decay, and Early Stopping.

The highest validation accuracy achieved was **96.73%** using improved ResNet50 fine-tuning.

### Tutorial 08 — Object Detection using Faster R-CNN (PyTorch)

Implementation and evaluation of a custom Faster R-CNN object detection model using PyTorch.

The tutorial covers CNN backbone construction, Region Proposal Networks (RPN), ROI Pooling, bounding-box regression, IoU, precision, recall, and mAP.

Experiments include comparing different numbers of convolutional layers, testing object detection on real images, and training a custom Faster R-CNN model using a 150-image bottle dataset.

The final model achieved **79.21% test mAP@0.5** and **35.70% test mAP@0.5:0.95**.

### Tutorial 08-A — Object Detection using Pretrained Faster R-CNN (PyTorch)

Implementation and evaluation of pretrained Faster R-CNN object detection models using PyTorch and Torchvision.

Experiments include testing object detection on a custom image, comparing ResNet50-FPN, MobileNetV3-FPN, and ResNet50-FPN V2 models, and evaluating detection performance on a 150-image bottle dataset using mAP.

ResNet50-FPN V2 achieved the highest detection performance with **97.99% mAP@0.5** and **87.45% mAP@0.5:0.95**, while MobileNetV3-FPN achieved the fastest inference time.

### Tutorial 09 — Object Detection using SSD and YOLO (PyTorch)

Implementation and evaluation of custom and pretrained SSD and YOLO object detection models using PyTorch.

Experiments include constructing SSD and YOLO architectures from scratch, training both models on a 150-image bottle dataset, and fine-tuning pretrained SSD300-VGG16 and YOLOv8 Nano models.

The pretrained YOLOv8 Nano achieved the highest detection performance with **94.79% test mAP@0.5** and **85.89% test mAP@0.5:0.95**, outperforming the custom models and pretrained SSD.

### Tutorial 10 — Image Segmentation using U-Net (PyTorch)

Implementation and evaluation of a custom U-Net architecture for binary image segmentation using PyTorch.

Experiments include training U-Net on synthetic images and the Oxford-IIIT Pet dataset, comparing original and deeper U-Net architectures, and analyzing the effect of different learning rates on segmentation performance.

The deeper U-Net achieved **70.03% validation Dice** and **54.63% validation IoU** in the architecture comparison. The final selected model achieved **64.71% test Dice** and **50.15% test IoU** using a learning rate of 0.0001.

### Tutorial 11 — Semantic Segmentation using DeepLabV3 and Mask R-CNN (PyTorch)

Implementation and evaluation of pretrained DeepLabV3-ResNet101 and Mask R-CNN ResNet50-FPN models using PyTorch and Torchvision.

Experiments include semantic segmentation using DeepLabV3, instance segmentation using Mask R-CNN, visualization of segmentation masks, and performance comparison on the Oxford-IIIT Pet dataset using pixel accuracy, Dice, and IoU.

DeepLabV3-ResNet101 achieved the highest segmentation performance with **86.54% test Dice** and **80.18% test IoU**, outperforming Mask R-CNN on the evaluated dataset.

### Tutorial 12 — Basic Autoencoders using PyTorch

Implementation and evaluation of convolutional autoencoders for MNIST handwritten digit reconstruction using PyTorch.

Experiments include building a basic encoder-decoder architecture, training for 50 epochs, visualizing reconstructed images, and improving the architecture using additional convolutional layers, Batch Normalization, and transposed convolutions.

The improved autoencoder achieved **0.059357 test BCE loss** and **0.000296 test MSE**, reducing reconstruction errors by **4.41%** and **67.55%**, respectively, compared with the original model.

More tutorials will be added throughout the course.

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
├── Tutorial-08A-Pretrained-Faster-RCNN/
│   ├── DL_Tutorial_8A.ipynb
│   └── README.md
│
├── Tutorial-09-SSD-YOLO-Object-Detection/
│   ├── DL_Tutorial_9.ipynb
│   └── README.md
│
├── Tutorial-10-UNet-Image-Segmentation/
│   ├── DL_Tutorial_10.ipynb
│   └── README.md
│
├── Tutorial-11-DeepLabV3-Mask-RCNN-Segmentation/
│   ├── DL_Tutorial_11.ipynb
│   └── README.md
│
├── Tutorial-12-Basic-Autoencoders/
│   ├── DL_Tutorial_12.ipynb
│   └── README.md
│
└── README.md
```
