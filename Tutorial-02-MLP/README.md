# Tutorial 02 - MLP Classifier

## Objective

This tutorial explores the implementation and training of a Multi-Layer Perceptron (MLP) classifier using the Iris dataset.

The tutorial covers:

- Data loading and train-test splitting
- Feature scaling using StandardScaler
- Training an MLP classifier
- Model evaluation
- Learning curve visualization
- Effect of hidden layers and neurons
- Effect of learning rate on convergence

## Task 1 - Hidden Layers and Neurons

Different MLP architectures were tested by changing the number of hidden layers and neurons.

The experiments showed that all tested configurations achieved 100% test accuracy. However, the architectures differed in their convergence speed.

The `(20, 20, 10)` configuration converged in the fewest epochs (354) while maintaining 100% accuracy.

## Task 2 - Learning Rate

Different learning rates were tested to study their effect on convergence.

| Learning Rate | Accuracy | Epochs |
|---|---:|---:|
| 0.0001 | 100% | 2000 |
| 0.001 | 100% | 609 |
| 0.01 | 100% | 157 |
| 0.1 | 95.56% | 159 |

A learning rate of `0.01` provided the best balance between convergence speed and model performance, achieving 100% test accuracy in 157 epochs.

## Files

- `DL_Tutorial_2.ipynb` - Complete Colab notebook containing implementation, experiments, outputs, learning curves, and analysis.

## Author

**Moiz Shahid**
