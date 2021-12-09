import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

@st.cache(allow_output_mutation = True)
def load_caption_model():
    model = load_model("image_caption_pred.h5")
    model.load_weights("weights.h5")
    return model
def load_image_model():
    image_model = load_model("resnet50.h5")
    return image_model
def load_vocab():
    vocab = np.load("vocab.npy", allow_pickle=True)
    return vocab

with st.spinner("Loading Model into Memory......"):
    model = load_caption_model()
    image_model = load_image_model()
    vocab = load_vocab()

count_words = vocab.flatten()[0]
inverse_dict = {v:k for k,v in count_words.items()}

st.write("""
            # Image Caption Generation
                                        """)
file = st.file_uploader("Upload Image here : ", type = ['jpg', 'png'])

import numpy as np
import cv2
from tensorflow.keras.preprocessing.sequence import  pad_sequences
from PIL import Image, ImageOps

def getImage(img):
    img = ImageOps.fit(img, (128, 128), Image.ANTIALIAS)
    img = np.asarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.reshape(img, (1,224, 224,3))
    return img

def prediction(image, model, image_model, count_words, inverse_dict):
    caption = ''
    text_input = ['start']
    Max_len = 23
    image = image_model.predict(getImage(image)).reshape(1, 2048)
    count = 0
    while count < Max_len:
        count = count+1
    
        encoded = list()
        for x in text_input:
            encoded.append(count_words[x])
    
        encoded = pad_sequences([encoded], padding='post', truncating='post', maxlen=Max_len)
    
        prediction = np.argmax(model.predict([image, encoded]))
        word = inverse_dict[prediction]
        caption =caption + ' '+ word
        if word == 'end':
            break

        text_input.append(word)
        text = " ".join(text_input[1:])
    return text

if file is None:
    pass
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    img = np.array(image)
    text = prediction(image, model, image_model, count_words, inverse_dict)
    st.success(text)
