import theano  # нейронки
import lasagne  # готовые нейронки
import time
import scipy.io
import numpy as np  # наука
from sklearn.cross_validation import train_test_split
from lasagne.objectives import categorical_crossentropy, categorical_accuracy
from lasagne.nonlinearities import softmax, sigmoid
from lasagne.layers import InputLayer, DenseLayer, get_output
from lasagne.layers import MaxPool2DLayer as Pool
from lasagne.layers import Conv2DLayer as Conv


class GenderRecognizer():
    """Convolutional Neural Network educated at https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/
    71%
    """

    def __init__(self):
        data = scipy.io.loadmat("Project/wiki_crop/wiki.mat")

        Y = data['wiki'][0][0][3][0]
        Y = Y.astype(np.uint8)

        # x_0 = data['wiki'][0][0][2][0]
        # get_photo_path = lambda i: x_0[i][0]
        # from scipy.misc import imread, imresize
        # X = np.empty(shape=[62328, 64, 64, 3], dtype='uint8')
        # for i in range(62328):  # 62328
        #     path = get_photo_path(i)
        #     img = imread('wiki_crop/{}'.format(path),)
        # #     print(img.shape)
        #     img_resized = imresize(img, (64, 64))
        # #     print(img_resized.shape)
        #     img_resized = img_resized.reshape([64, 64, -1])
        #     X[i] = img_resized
        # np.save("X", X)

        X = np.load("Project/X.npy")

        a = Y[Y == 0]
        b = Y[Y == 1][:len(a)]
        y_0 = np.concatenate([a, b])
        a = X[Y == 0]
        b = X[Y == 1][:len(a)]
        x_0 = np.concatenate([a, b])

        X, Y = x_0, y_0

        p = np.random.permutation(len(X))
        X, Y = X[p], Y[p]

        t = int(len(X) * 0.8)
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(X, Y, test_size=0.2)

        self.input_X = theano.tensor.tensor4("X")
        self.X_reshaped = self.input_X.dimshuffle([0, 3, 1, 2])
        self.target_y = theano.tensor.vector("target Y", dtype='int32')

        # Архитектура
        self.in_0 = InputLayer(shape=[None, 3, 64, 64], input_var=self.X_reshaped)
        self.in_downsample = Pool(self.in_0, [2, 2])
        self.conv_0 = Conv(self.in_downsample, 32, (3, 3), nonlinearity=sigmoid)
        self.pool_0 = Pool(self.conv_0, (3, 3))
        self.out = DenseLayer(self.pool_0, num_units=2, nonlinearity=softmax)

        self.all_weights = lasagne.layers.get_all_params(self.out)

        self.y_predicted = get_output(self.out)
        self.loss = categorical_crossentropy(self.y_predicted, self.target_y).mean()
        self.accuracy = categorical_accuracy(self.y_predicted, self.target_y).mean()

        self.updates = lasagne.updates.adadelta(self.loss, self.all_weights, learning_rate=0.01)
        self.train_fun = theano.function([self.input_X, self.target_y], [self.loss, self.accuracy], updates=self.updates, allow_input_downcast=True)
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

    def training(self, num_epochs=500, batch_size=100):
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

            self.save_current_state('Project/model.npz')

            # Then we print the results for this epoch:
            print("Epoch {} of {} took {:.3f}s".format(
                epoch + 1, num_epochs, time.time() - start_time))
            print("Validation accuracy:\t\t{:.2f}%".format(
                val_acc / val_batches * 100))

    def save_current_state(self, path):
        np.savez(path, *lasagne.layers.get_all_param_values(self.out))

    def load_last_state(self, path='Project/model_66.npz'):
        try:
            with np.load(path) as f:
                param_values = [f['arr_%d' % i] for i in range(len(f.files))]
            lasagne.layers.set_all_param_values(self.out, param_values)
        except Exception:
            print("Couldn't load model")

    def predict(self, file):
        predict = theano.compile.function([self.input_X], get_output(self.out))
        return "Male" if predict(file)[0].argmax() else "Female"
