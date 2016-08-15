import theano  # нейронки
import lasagne  # готовые нейронки
import os  # работа с путями
import numpy as np
from scipy.misc import imresize
from skimage.color import rgb2gray
from lasagne.layers import InputLayer as Input
from lasagne.layers import DenseLayer as Dense
from lasagne.layers import MaxPool2DLayer as Pool
from lasagne.layers import Conv2DLayer as Conv
from lasagne.layers import get_output
from lasagne.nonlinearities import softmax, sigmoid

# for training
import time
import pandas as pd
from sklearn.cross_validation import train_test_split


class EmotionRecognizer:
    """
    Convolutional Neural Network, educated at Kaggle dataset: https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data
    Accuracy 40%
    """

    def __init__(self):
        self.input_X = theano.tensor.tensor4("X")
        # self.X_reshaped = self.input_X.dimshuffle([0, 3, 1, 2])
        self.target_y = theano.tensor.vector("target Y", dtype='int32')

        # Архитектура
        in_0 = Input(shape=[None, 1, 64, 64], input_var=self.input_X)
        in_downsample = Pool(in_0, [4, 4])
        conv_0 = Conv(in_downsample, 64, (2, 2), nonlinearity=sigmoid)
        pool_0 = Pool(conv_0, (3, 3))
        self.out = Dense(pool_0, num_units=7, nonlinearity=softmax)

        # load last state(if file exists)
        self.path = "{}/{}.npz".format(os.getcwd(), self.__class__.__name__)
        if os.path.exists(self.path):
            with np.load(self.path) as f:
                param_values = [f['arr_%d' % i] for i in range(len(f.files))]
            lasagne.layers.set_all_param_values(self.out, param_values)

        self.predict_net = theano.compile.function([self.input_X], get_output(self.out))

        # Для обучения (Можно удалить)
        self.all_weights = lasagne.layers.get_all_params(self.out)

        self.y_predicted = get_output(self.out)
        self.loss = lasagne.objectives.categorical_crossentropy(self.y_predicted, self.target_y).mean()
        self.accuracy = lasagne.objectives.categorical_accuracy(self.y_predicted, self.target_y).mean()

        self.updates = lasagne.updates.adadelta(self.loss, self.all_weights, learning_rate=0.01)
        self.train_fun = theano.function([self.input_X, self.target_y], [self.loss, self.accuracy], updates=self.updates, allow_input_downcast=True)
        self.accuracy_fun = theano.function([self.input_X, self.target_y], self.accuracy, allow_input_downcast=True)

    @staticmethod
    def get_data():
        """Читает полученную выборку, строит по байтам картинки и отдает 4д и 1д массивы"""
        data = pd.read_csv('Project/fer2013/fer2013.csv')

        X = np.empty(shape=[35887, 1, 64, 64], dtype='uint8')
        Y = np.empty(shape=[35887], dtype='uint8')

        for i in range(data.shape[0]):
            img = np.zeros((1, 48, 48), dtype='uint8')
            pixels = [int(elem) for elem in data.ix[i]['pixels'].split()]
            for i_ in range(48):
                for j_ in range(48):
                    img[0, i_, j_] = pixels[i_ * 48 + j_]
            X[i, 0] = imresize(img[0], (64, 64))
            Y[i] = int(data.ix[i]['emotion'])

        return X, Y

    # noinspection PyPep8Naming
    def fit(self, X, Y, num_epochs=500, batch_size=50):
        X_train, X_test, Y_train, Y_test = train_test_split(np.array(X), np.array(Y), test_size=0.2, random_state=42)

        def iterate_minibatches(inputs, targets, batchsize, shuffle=True):
            assert len(inputs) == len(targets)
            if shuffle:
                indices = np.arange(len(inputs))
                np.random.shuffle(indices)
            for start_idx in range(0, len(inputs) - batchsize + 1, batchsize):
                if shuffle:
                    excerpt = indices[start_idx:start_idx + batchsize]
                else:
                    excerpt = slice(start_idx, start_idx + batchsize)
                yield inputs[excerpt], targets[excerpt]

        for epoch in range(num_epochs):
            # In each epoch, we do a full pass over the training data:
            train_err = 0
            train_acc = 0
            train_batches = 0
            start_time = time.time()
            for batch in iterate_minibatches(X_train, Y_train, batch_size):
                inputs, targets = batch
                train_err_batch, train_acc_batch = self.train_fun(inputs, targets)
                train_err += train_err_batch
                train_acc += train_acc_batch
                train_batches += 1

            # And a full pass over the validation data:
            val_acc = 0
            val_batches = 0
            for batch in iterate_minibatches(X_test, Y_test, batch_size):
                inputs, targets = batch
                val_acc += self.accuracy_fun(inputs, targets)
                val_batches += 1

            # save current state
            np.savez(self.path, *lasagne.layers.get_all_param_values(self.out))

            # Then we print the results for this epoch:
            print("Epoch {} of {} took {:.3f}s".format(
                epoch + 1, num_epochs, time.time() - start_time))

            print("  training loss (in-iteration):\t\t{:.6f}".format(train_err / train_batches))
            print("  train accuracy:\t\t{:.2f} %".format(
                train_acc / train_batches * 100))
            print("  validation accuracy:\t\t{:.2f} %".format(
                val_acc / val_batches * 100))

    def predict(self, face) -> str:
        face = np.array([np.reshape(imresize(rgb2gray(face), (64, 64)), (1, 64, 64))])
        x = self.predict_net(face).argmax()
        if x == 0:
            return "Angry"
        elif x == 1:
            return "Disgust"
        elif x == 2:
            return "Fear"
        elif x == 3:
            return "Happy"
        elif x == 4:
            return "Sad"
        elif x == 5:
            return "Surprise"
        elif x == 6:
            return "Neutral"
