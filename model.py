import numpy as np
import tensorflow as tf
import os
from keras.preprocessing.image import load_img, img_to_array

# Load DenseNet121 model
dense_net_path = "./models/DenseNet121.h5"
model_denseNet121 = tf.keras.models.load_model(dense_net_path)

# Load DenseNet169 model
dense_net_path = "./models/DenseNet169.h5"
model_denseNet169 = tf.keras.models.load_model(dense_net_path)

# Load DenseNet201 model
dense_net_path = "./models/DenseNet201.h5"
model_denseNet201 = tf.keras.models.load_model(dense_net_path)

# Load InceptionV3 model
inception_v3_path = "./models/InceptionV3.h5"
model_inceptionV3 = tf.keras.models.load_model(inception_v3_path)

# Load VGG16 model
vgg16_path = "./models/VGG16.h5"
model_vgg16 = tf.keras.models.load_model(vgg16_path)

# Load Xception model
Xception_path = "./models/Xception.h5"
model_Xception = tf.keras.models.load_model(Xception_path)

# Define class labels
class_labels = {
    0: "Apple___Apple_scab",
    1: "Apple___Black_rot",
    2: "Apple___Cedar_apple_rust",
    3: "Apple___healthy",
}


# preprocessing image (224)
def process_image_224(image_file):
    image = load_img(image_file, target_size=(224, 224))
    img_array = img_to_array(image)
    img_batch = img_array.reshape((1,) + img_array.shape)
    img_batch = img_batch / 255.0
    return img_batch


# preprocessing image (299)
def process_image_299(image_file):
    image = load_img(image_file, target_size=(299, 299))
    img_array = img_to_array(image)
    img_batch = img_array.reshape((1,) + img_array.shape)
    img_batch = img_batch / 255.0
    return img_batch


# Predict disease class
def model_predict(model, image_file, size=None):
    img = process_image_224(image_file)
    if size == 299:
        img = process_image_299(image_file)
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction[0])
    disease_name = class_labels[predicted_class]
    print(disease_name)
    return disease_name


def poll(data_list: list):
    most_frequent = max(data_list, key=data_list.count)
    return most_frequent


def predict_image(filename):
    image_file = os.path.join("./uploads", filename)
    prediction = [
        model_predict(model_denseNet121, image_file),
        model_predict(model_denseNet169, image_file),
        model_predict(model_denseNet201, image_file),
        model_predict(model_inceptionV3, image_file, 299),
        model_predict(model_vgg16, image_file),
        model_predict(model_Xception, image_file),
    ]
    return poll(prediction)
