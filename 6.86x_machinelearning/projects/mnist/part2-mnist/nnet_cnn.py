#! /usr/bin/env python
import sys
sys.path.append("..")
from train_utils import batchify_data, run_epoch, train_model, Flatten
from utils import *
import utils
import _pickle as c_pickle
import gzip
import numpy as np
from tqdm import tqdm
import torch
import torch.autograd as autograd
import torch.nn.functional as F
import torch.nn as nn


def main():
    # Load the dataset
    num_classes = 10
    X_train, y_train, X_test, y_test = get_MNIST_data()

    # We need to rehape the data back into a 1x28x28 image
    X_train = np.reshape(X_train, (X_train.shape[0], 1, 28, 28))
    X_test = np.reshape(X_test, (X_test.shape[0], 1, 28, 28))

    # Split into train and dev
    dev_split_index = int(9 * len(X_train) / 10)
    X_dev = X_train[dev_split_index:]
    y_dev = y_train[dev_split_index:]
    X_train = X_train[:dev_split_index]
    y_train = y_train[:dev_split_index]

    permutation = np.array([i for i in range(len(X_train))])
    np.random.shuffle(permutation)
    X_train = [X_train[i] for i in permutation]
    y_train = [y_train[i] for i in permutation]

    # Split dataset into batches
    batch_size = 32
    train_batches = batchify_data(X_train, y_train, batch_size)
    dev_batches = batchify_data(X_dev, y_dev, batch_size)
    test_batches = batchify_data(X_test, y_test, batch_size)

    #################################
    # Model specification TODO
    model = nn.Sequential(
        # Convolutional layer with 32 filters of size 3x3
        nn.Conv2d(1, 32, kernel_size=(3, 3)),
        nn.ReLU(),                            # ReLU nonlinearity
        nn.MaxPool2d(kernel_size=(2, 2)),     # Max pooling layer with size 2x2

        # Convolutional layer with 64 filters of size 3x3
        nn.Conv2d(32, 64, kernel_size=(3, 3)),
        nn.ReLU(),                            # ReLU nonlinearity
        nn.MaxPool2d(kernel_size=(2, 2)),     # Max pooling layer with size 2x2

        nn.Flatten(),                         # Flatten layer

        # Fully connected layer with 128 neurons
        nn.Linear(64 * 5 * 5, 128),
        # nn.ReLU(),                            # ReLU nonlinearity
        # Dropout layer with drop probability 0.5
        nn.Dropout(p=0.5),

        nn.Linear(128, 10)
    )
    ##################################

    train_model(train_batches, dev_batches, model, nesterov=True)

    # Evaluate the model on test data
    loss, accuracy = run_epoch(test_batches, model.eval(), None)

    print("Loss on test set:" + str(loss) +
          " Accuracy on test set: " + str(accuracy))


if __name__ == '__main__':
    # Specify seed for deterministic behavior, then shuffle. Do not change seed for official submissions to edx
    np.random.seed(12321)  # for reproducibility
    torch.manual_seed(12321)
    main()
