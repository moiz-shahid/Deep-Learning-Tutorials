import numpy as np
import pandas as pd

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# PERCEPTRON CLASS

class Perceptron(object):

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    # Weighted Sum
    def weighted_sum(self, X):

        return np.dot(X, self.w_[1:]) + self.w_[0]

    # Sigmoid Activation Function
    def sigmoid(self, X):

        z = self.weighted_sum(X)

        return 1 / (1 + np.exp(-z))

    # Prediction Function
    def predict(self, X):

        probability = self.sigmoid(X)

        return np.where(probability >= 0.5, 1, 0)

    # Training Function
    def fit(self, X, y):

        # Initialize weights with zero
        self.w_ = np.zeros(1 + X.shape[1])

        self.errors_ = []

        # Repeat training n_iter times
        for _ in range(self.n_iter):

            errors = 0

            # Go through every training sample
            for xi, target in zip(X, y):

                # Make prediction
                prediction = self.predict(xi)

                # Calculate update
                update = self.eta * (target - prediction)

                # Update feature weights
                self.w_[1:] = self.w_[1:] + update * xi

                # Update bias
                self.w_[0] = self.w_[0] + update

                # Count errors
                errors += int(update != 0.0)

            # Store errors after every iteration
            self.errors_.append(errors)


        return self

# LOAD IRIS DATASET

df = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    header=None
)

# Shuffle dataset
df = shuffle(df)

# SEPARATE INPUT FEATURES AND LABELS

# First 4 columns
X = df.iloc[:, 0:4].values

# Fifth column
y = df.iloc[:, 4].values

# SPLIT INTO TRAIN AND TEST DATA

train_data, test_data, train_labels, test_labels = train_test_split(
    X,
    y,
    test_size=0.25
)

# CHANGE LABELS TO 1 AND 0
# Iris-setosa = 1
# Other flowers = 0

train_labels = np.where(
    train_labels == 'Iris-setosa',
    1,
    0
)

test_labels = np.where(
    test_labels == 'Iris-setosa',
    1,
    0
)

# CREATE PERCEPTRON

perceptron = Perceptron(
    eta=0.01,
    n_iter=10
)

# TRAIN MODEL

perceptron.fit(
    train_data,
    train_labels
)


# TEST MODEL
test_preds = perceptron.predict(test_data)

# Calculate accuracy
accuracy = accuracy_score(
    test_labels,
    test_preds
)

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


# MANUAL INPUT

print("\nEnter flower measurements:")

sepal_length = float(
    input("Enter sepal length: ")
)

sepal_width = float(
    input("Enter sepal width: ")
)

petal_length = float(
    input("Enter petal length: ")
)

petal_width = float(
    input("Enter petal width: ")
)


# Create one flower sample
sample = np.array([[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]])

# MAKE PREDICTION

prediction = perceptron.predict(sample)

# DISPLAY RESULT

if prediction[0] == 1:

    print("Prediction: The flower is Iris-setosa")

else:

    print("Prediction: The flower is NOT Iris-setosa")