# Tutorial 12 — Basic Autoencoders using PyTorch

## Objective

Implement a convolutional autoencoder for MNIST handwritten digit reconstruction using PyTorch, visualize reconstructed images, and improve reconstruction quality by modifying the model architecture.

## Dataset

**MNIST Handwritten Digit Dataset**

- Training images: 54,000
- Validation images: 6,000
- Test images: 10,000
- Image resolution: 28 × 28 pixels
- Image format: Grayscale, normalized to [0, 1]

The autoencoders learn to reconstruct the input image rather than predict its digit label.

## Experiments

### Part 1 — Basic Convolutional Autoencoder

A convolutional autoencoder was implemented using convolutional layers and max-pooling for encoding, followed by convolutional layers and upsampling for decoding.

The model was trained for **50 epochs** using the Adam optimizer, a learning rate of **0.001**, and Binary Cross-Entropy reconstruction loss.

The baseline produced a latent feature representation of shape **(64, 7, 7)**.

### Assignment — Improve the Autoencoder Architecture

An improved convolutional autoencoder was implemented with:

- Additional convolutional layers
- Batch Normalization
- Transposed convolution layers for learnable upsampling
- A deeper latent feature representation of shape **(128, 7, 7)**

The improved model was trained for **50 epochs** on the same MNIST training and validation splits, using the same learning rate and loss function.

Both architectures were evaluated on the same **10,000 test images**. Training curves and side-by-side reconstructed digit images were used for comparison.

## Final Model Comparison

| Metric | Basic Autoencoder | Improved Autoencoder |
|---|---:|---:|
| Parameters | 74,497 | 252,609 |
| Best Validation Loss | 0.06250 | **0.05969** |
| Best Validation Epoch | 48 | 50 |
| Test BCE Loss | 0.062099 | **0.059357** |
| Test MSE | 0.000911 | **0.000296** |

The improved architecture reduced **test BCE by 4.41%** and **test MSE by 67.55%** relative to the baseline.

## Analysis

Both autoencoders successfully reconstructed recognizable handwritten digits. The improved architecture produced lower validation and test reconstruction losses, and its output generally showed cleaner digit strokes and boundaries in the visual comparison.

The improved model had approximately **3.39 times** as many parameters as the basic model, so its reconstruction gains came with increased model complexity.

Although the models reduce the spatial dimensions of the image, their latent tensors contain more scalar values than the 784-pixel input. They therefore do not form strict dimensional compression bottlenecks.

## Conclusion

The custom autoencoder and model-improvement assignment were successfully completed in PyTorch. The improved convolutional architecture achieved the best reconstruction performance, with **0.059357 test BCE** and **0.000296 test MSE** on MNIST.

## Technologies Used

- Python
- PyTorch and Torchvision
- NumPy and Pandas
- Matplotlib
- Google Colab

## Author

**Moiz Shahid**

GitHub: [@moiz-shahid](https://github.com/moiz-shahid)
