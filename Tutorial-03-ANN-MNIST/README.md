# Tutorial 03 - ANN for MNIST Digit Classification

## Objective

This tutorial implements and evaluates an Artificial Neural Network (ANN) for handwritten digit classification using the MNIST dataset.

The tutorial covers:

- Loading and preprocessing the MNIST dataset
- Normalization and one-hot encoding
- Building and training an ANN
- Comparing different network architectures
- Comparing activation functions
- Comparing different optimizers
- Analyzing overfitting and underfitting
- Implementing Early Stopping
- Applying Dropout regularization
- Improving model generalization

## Baseline Model

The baseline ANN consists of:

- Flatten layer: 28 × 28 images converted to 784 features
- Dense layer: 128 neurons with ReLU
- Dense layer: 64 neurons with ReLU
- Output layer: 10 neurons with Softmax

The baseline model achieved approximately:

- Test Accuracy: 97.82%
- Test Loss: 0.0874

## Architecture Experiment

Different architectures were tested by changing the number of hidden layers and neurons.

Among the tested architectures, the `(256, 128)` configuration achieved the highest test accuracy of approximately 97.73%.

The experiment showed that increasing the number of neurons can improve performance slightly, while simply adding more hidden layers does not necessarily produce better results.

## Activation Function Comparison

ReLU, tanh, and sigmoid activation functions were compared.

Approximate test accuracies:

- ReLU: 97.36%
- tanh: 97.06%
- Sigmoid: 97.50%

Sigmoid achieved the highest test accuracy in this experiment.

## Optimizer Comparison

SGD, RMSprop, and Adam were compared.

| Optimizer | Test Accuracy | Training Time |
|---|---:|---:|
| SGD | 95.76% | 48.81 s |
| RMSprop | 97.72% | 65.19 s |
| Adam | 97.45% | 64.50 s |

SGD had the shortest wall-clock training time but converged more slowly in terms of model performance and produced lower final accuracy.

RMSprop achieved the highest test accuracy, while Adam also demonstrated fast and stable convergence.

## Overfitting Analysis

The model was trained for 30 epochs to observe the effect of prolonged training.

Training accuracy continued to increase and training loss continued to decrease, while validation accuracy stopped improving and validation loss began to increase.

This demonstrated overfitting.

## Early Stopping

Early Stopping was implemented by monitoring validation loss with a patience value of 3.

Training automatically stopped when validation loss stopped improving, preventing unnecessary training and limiting overfitting.

## Regularization and Improved Model

Dropout regularization with a dropout rate of 0.2 was applied to the hidden layers together with Early Stopping.

The improved model achieved approximately:

- Test Accuracy: 97.94%
- Test Loss: 0.0707

The training and validation curves remained relatively close, showing improved generalization compared with the deliberately overfitted model.

## Conclusion

The experiments demonstrate that neural network performance depends on architecture, activation function, optimizer selection, training duration, and regularization.

Dropout and Early Stopping helped control overfitting and produced a model with good generalization performance on the MNIST dataset.

## Author

**Moiz Shahid**
