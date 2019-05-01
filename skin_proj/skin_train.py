import keras
from keras.layers import Input, Dense, Conv2D, Flatten, MaxPooling2D
from keras.models import Model

from keras.applications import VGG19

# Img Input
main_input = Input(shape=(224,224,3), name='main_input')
# Topological, Symptoms, Additional Info Input
aux_input  = Input(shape=(1,), name='aux_input')

# Main Model for Image Recognition
conv_base = VGG19(weights='imagenet', include_top=False)

conv_base.trainable = False
for layer in conv_base.layers:
	layer.trainable = False
mm = conv_base.get_layer('block4_pool')(main_input)

mm = Conv2D(64, (3,3), activation='relu')(mm)
mm = MaxPooling2D((2,2))(mm)
mm = Conv2D(64, (3,3), activation='relu')(mm)
mm = Flatten()(mm)
aux_out = Dense(1, activation='sigmoid', name='aux_out')(mm)

fm = keras.layers.concatenate([mm, aux_input])
fm = Dense(32, activation='relu')(fm)
main_out = Dense(1, activation='sigmoid', name='main_out')(fm)

model = Model(inputs=[main_input, aux_input], outputs=[main_out, aux_out])
model.summary()

model.compile(optimizer='rmsprop', loss='binary_crossentropy', loss_weights=[1.0,0.2])



# TRAIN MODEL For Vitiligo

import skin_data as sd
import numpy as np

aux_data = np.zeros(len(sd.labels))

model.fit([sd.image_data,aux_data], [sd.labels, sd.labels], epochs=10, batch_size=20)

