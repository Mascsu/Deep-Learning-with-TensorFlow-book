import os
os.environ["KERAS_BACKEND"]="tensorflow"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.layers as layers

a = 1.2
aa = tf.constant(1.2)
print(type(a), type(aa), tf.is_tensor(aa))
print(tf.__version__)