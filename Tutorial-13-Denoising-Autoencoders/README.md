# Tutorial 13 — Denoising Autoencoders using PyTorch

## Objective

Implement and evaluate denoising autoencoders using PyTorch to reconstruct clean MNIST digit images from noisy inputs. Compare a basic convolutional denoising autoencoder, a deeper denoising autoencoder, and a Variational Autoencoder (VAE).

## Dataset

**MNIST Handwritten Digit Dataset**

- Training images: 54,000
- Validation images: 6,000
- Test images: 10,000
- Resolution: 28 × 28 grayscale pixels
- Input normalization: [0, 1]
- Noise type: Additive Gaussian noise, clipped to [0, 1]
- Noise factor: **0.5**
- Reconstruction target: Original clean image

The same MNIST splits and test-noise configuration were used to compare reconstruction quality across models.

## Experiments

### Part 1 — Basic Denoising Autoencoder

A convolutional denoising autoencoder was implemented with convolutional layers, max-pooling in the encoder, and convolutional layers with upsampling in the decoder.

The network was trained on **noisy inputs and clean targets** for 10 epochs using Adam, a learning rate of 0.001, and Binary Cross-Entropy (BCE) loss. Its encoder produced a latent feature tensor of shape (64, 7, 7).

**Results:** Test BCE **0.095913**, test MSE **0.011030**.

### Task 1 — Deep Denoising Autoencoder

A deeper convolutional denoising autoencoder was implemented using additional convolutional layers, Batch Normalization, and transposed convolutions for learnable upsampling.

Both basic and deep models were trained for 10 epochs using the same dataset, noise factor, optimizer, and learning rate. Comparisons included training and validation losses, held-out test reconstruction errors, and reconstructed digit visualizations.

**Results:** Test BCE **0.088734**, test MSE **0.008836**. Relative to the basic model, the deep architecture reduced test BCE by **7.49%** and MSE by **19.89%**.

### Task 2 — Variational Autoencoder (VAE)

A convolutional **denoising VAE** was implemented with:

- Encoder layers predicting a latent mean and log variance
- A **16-dimensional** probabilistic latent space
- The reparameterization trick for differentiable latent sampling
- A decoder reconstructing clean images from noisy inputs
- A training objective combining reconstruction BCE and KL-divergence regularization

The VAE was trained for 10 epochs. Besides denoising, the notebook demonstrates generation of new digit-like images by sampling the latent space.

**VAE results:**

| Metric | Value |
|---|---:|
| Best Validation Total Loss (per image) | 120.2236 |
| Sampled Test Total Loss (per image) | 119.0519 |
| Test KL Divergence (per image) | 22.1540 |
| Deterministic Test BCE (per pixel) | 0.115052 |
| Deterministic Test MSE (per pixel) | 0.017190 |

The VAE's total objective includes KL divergence and is measured per image, so it should not be directly compared with the other models' per-pixel BCE scores.

## Final Model Comparison

| Metric | Basic Denoising AE | Deep Denoising AE | Variational AE |
|---|---:|---:|---:|
| Model Parameters | 74,497 | 252,609 | 180,865 |
| Epochs | 10 | 10 | 10 |
| Test BCE (per pixel) | 0.095913 | **0.088734** | 0.115052 |
| Test MSE (per pixel) | 0.011030 | **0.008836** | 0.017190 |

The VAE values use deterministic reconstructions from its latent mean; its sampled test objective is reported separately above.

## Analysis

All three models learned to reconstruct recognizable digits from heavily corrupted inputs.

The **deep denoising autoencoder** achieved the lowest reconstruction BCE and MSE. Its additional network capacity improved the preservation of digit strokes and boundaries, at the cost of more parameters.

The **VAE** produced smoother reconstructions and higher pixel-level reconstruction errors in this experiment. However, it learned a compact regularized probabilistic representation and was also able to generate new digit-like images from random latent samples. These properties serve a different purpose from reconstruction accuracy alone.

## Conclusion

The basic denoising autoencoder, deeper denoising autoencoder, and variational autoencoder were successfully implemented and evaluated in PyTorch.

The **deep denoising autoencoder** achieved the best reconstruction performance, with **0.088734 test BCE** and **0.008836 test MSE**. The VAE demonstrated latent-space sampling and image generation, illustrating the difference between conventional denoising autoencoders and generative probabilistic models.

