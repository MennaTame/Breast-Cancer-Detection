import PIL
import keras
from PIL import Image, ImageOps
import numpy as np


def ultrasound_classification(img, weights_file):
    # Load the model
    model = keras.models.load_model(weights_file)

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    image = img
    #image sizing
    size = (224, 224)
    image = ImageOps.fit(image, size, PIL.Image.Resampling.LANCZOS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return np.argmax(prediction) # return position of the highest probability

def thermal_classification(img, weights_file):

    np.set_printoptions(suppress=True)
    model = keras.models.load_model(weights_file)

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS).convert("RGB")

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    return np.argmax(prediction)

def mammography_classification(img, weights_file):

    np.set_printoptions(suppress=True)
    model = keras.models.load_model(weights_file)

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS).convert("RGB")

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    return np.argmax(prediction)
