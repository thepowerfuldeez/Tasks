import theano  # нейронки
import lasagne  # готовые нейронки
import time
import numpy as np
import pandas as pd
from scipy.misc import imresize
from sklearn.cross_validation import train_test_split
from lasagne.layers import InputLayer, DenseLayer, get_output
from lasagne.nonlinearities import softmax, sigmoid
from lasagne.objectives import categorical_crossentropy, categorical_accuracy
from lasagne.layers import MaxPool2DLayer as Pool
from lasagne.layers import Conv2DLayer as Conv


class EmotionRecognizer():
    """
    Convolutional Neural Network, educated at Kaggle dataset: https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data
    39%
    """

    def __init__(self):
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

        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(np.array(X), np.array(Y),
                                                                                test_size=0.20, random_state=42)

        self.input_X = theano.tensor.tensor4("X")
        # X_reshaped = input_X.dimshuffle([0,3,1,2])
        self.target_y = theano.tensor.vector("target Y", dtype='int32')

        # Архитектура
        self.in_0 = InputLayer(shape=[None, 1, 64, 64], input_var=self.input_X)
        self.in_downsample = Pool(self.in_0, [4, 4])
        self.conv_0 = Conv(self.in_downsample, 64, (2, 2), nonlinearity=sigmoid)
        self.pool_0 = Pool(self.conv_0, (3, 3))
        # conv_1 = Conv(pool_0, 64, (3, 3), nonlinearity=sigmoid)
        # pool_1 = Pool(conv_1, (3, 3))
        # drop_0 = Drop(pool_1, p=0.15)
        # dense_0 = Dense(drop_0, 40, nonlinearity=sigmoid)
        self.out = DenseLayer(self.pool_0, num_units=7, nonlinearity=softmax)

        self.all_weights = lasagne.layers.get_all_params(self.out)

        self.y_predicted = get_output(self.out)
        self.loss = categorical_crossentropy(self.y_predicted, self.target_y).mean()
        self.accuracy = categorical_accuracy(self.y_predicted, self.target_y).mean()

        self.updates = lasagne.updates.adadelta(self.loss, self.all_weights, learning_rate=0.01)
        self.train_fun = theano.function([self.input_X, self.target_y], [self.loss, self.accuracy],
                                         updates=self.updates, allow_input_downcast=True)
        self.accuracy_fun = theano.function([self.input_X, self.target_y], self.accuracy, allow_input_downcast=True)

    @staticmethod
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

    def training(self, num_epochs=500, batch_size=50):
        for epoch in range(num_epochs):
            # In each epoch, we do a full pass over the training data:
            train_err = 0
            train_acc = 0
            train_batches = 0
            start_time = time.time()
            for batch in self.iterate_minibatches(self.X_train, self.Y_train, batch_size):
                inputs, targets = batch
                train_err_batch, train_acc_batch = self.train_fun(inputs, targets)
                train_err += train_err_batch
                train_acc += train_acc_batch
                train_batches += 1

            # And a full pass over the validation data:
            val_acc = 0
            val_batches = 0
            for batch in self.iterate_minibatches(self.X_test, self.Y_test, batch_size):
                inputs, targets = batch
                val_acc += self.accuracy_fun(inputs, targets)
                val_batches += 1

            self.save_current_state('Project/emo_model.npz')

            # Then we print the results for this epoch:
            print("Epoch {} of {} took {:.3f}s".format(
                epoch + 1, num_epochs, time.time() - start_time))

            print("Validation accuracy:\t\t{:.2f}%".format(
                val_acc / val_batches * 100))

    def save_current_state(self, path):
        np.savez(path, *lasagne.layers.get_all_param_values(self.out))

    def load_last_state(self, path='Project/emo_model_37.npz'):
        # noinspection PyBroadException
        try:
            with np.load(path) as f:
                self.param_values = [f['arr_%d' % i] for i in range(len(f.files))]
            lasagne.layers.set_all_param_values(self.out, self.param_values)
        except Exception:
            print("Couldn't load model")

    def predict(self, file):

        predict = theano.compile.function([self.input_X], get_output(self.out))

        x = predict(file).argmax()
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
