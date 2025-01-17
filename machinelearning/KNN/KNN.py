import tensorflow as tf
import matplotlib.pyplot as plt
from data import *

def plot_history(history):
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
  ax1.plot(history.history['loss'], label='loss')
  ax1.plot(history.history['val_loss'], label='val_loss')
  ax1.set_xlabel('Epoch')
  ax1.set_ylabel('Binary crossentropy')
  ax1.grid(True)

  ax2.plot(history.history['accuracy'], label='accuracy')
  ax2.plot(history.history['val_accuracy'], label='val_accuracy')
  ax2.set_xlabel('Epoch')
  ax2.set_ylabel('Accuracy')
  ax2.grid(True)

  plt.show()

nn_model = tf.keras.Sequential([
    tf.keras.layers.Dense(64,activation='relu',input_shape =(10,)),
    tf.keras.layers.Dense(32,activation ='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
]) 
nn_model.add(tf.keras.layers.Dense(1, activation=None))
nn_model.compile(optimizer=tf.keras.optimizers.Adam(0.001), loss='binary_crossentropy', metrics=['accuracy'])


history = nn_model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=0)

plot_history(history)