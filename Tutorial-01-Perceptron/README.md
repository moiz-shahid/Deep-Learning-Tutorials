# Tutorial 01 - Understanding a Perceptron

## Objective

The objective of this tutorial is to understand the basic working of a Perceptron, including:

- Weights and bias
- Weighted sum
- Activation function
- Training and testing
- Prediction using the Iris dataset

## Dataset

The Iris dataset is used for binary classification. The four input features are:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The classes are represented as:

- `1` - Iris-setosa
- `0` - Not Iris-setosa

## Tasks

1. Take manual input for the four features and predict whether the flower is Iris-setosa or not.
2. Replace the Step Function with the Sigmoid activation function.
3. Replace the labels `1, -1` with `1, 0`.

## Sigmoid Activation Function

The Step Function was replaced with the Sigmoid function:

`sigmoid(z) = 1 / (1 + exp(-z))`

A threshold of `0.5` is used for classification:

- Output >= 0.5 -> Iris-setosa
- Output < 0.5 -> Not Iris-setosa

## Output

### Accuracy

```text
Accuracy: 100.0 %
```

### Manual Input and Prediction

```text
Enter flower measurements:
Enter sepal length: 0.4
Enter sepal width: 0.7
Enter petal length: 0.33
Enter petal width: 0.9
Prediction: The flower is Iris-setosa
```

## Author

**Moiz Shahid**
