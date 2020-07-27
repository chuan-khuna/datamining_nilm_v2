import tensorflow as tf
import numpy as np
import pandas as pd


def windowing_arr(series, window_size, output_size=1, shuffle_buffer=1000):
    """windowing the input series to ML train-dataset
        window_size: time step of input
        output_size: time step of output/forcast/predicted

        return: tensor flow object
    """

    ds = tf.data.Dataset.from_tensor_slices(series)
    windows = ds.window(window_size + output_size, shift=1, drop_remainder=True)
    ds = windows.flat_map(lambda window: window.batch(window_size + output_size))
    ds = ds.shuffle(shuffle_buffer)
    ds = ds.map(lambda window: (window[:-output_size], window[-output_size:]))
    return ds


def tensor_to_numpy(tensor_ds):
    """convert tensorflow object to numpy array"""

    X = []
    Y = []

    for window in tensor_ds:
        x, y = window
        X.append(x.numpy())
        Y.append(y.numpy())

    X = np.asarray(X)
    Y = np.asarray(Y)

    return X, Y