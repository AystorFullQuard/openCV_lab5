import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


def sharpen_image(image_path):
    image = cv2.imread(image_path)
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel_sharpening)
    return sharpened_image


def sharpen_image_alternative(image_path, force=2.5):
    image = cv2.imread(image_path)
    blured_image = blur_image(image_path, (0, 0), 10)
    sharpened_image = cv2.addWeighted(image, 1.0 + force, blured_image, -force, 0.0)
    return sharpened_image


def blur_image(image_path, kernel_size=(5, 5), sigmaX=20):
    image = cv2.imread(image_path)
    blurred_image = cv2.GaussianBlur(image, kernel_size, sigmaX)
    return blurred_image


def show_image_and_save_by_path(title, input_path, output_path=None, filename=None):
    image = cv2.imread(input_path)
    plt.title(title)
    plt.subplot(1, 1, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
    if output_path and filename:
        save_image(output_path, image, filename)


def save_image(output_path, image, filename):
    try:
        cv2.imwrite(output_path + '\\' + filename, image)
    except Exception as e:
        print("Error saving the image:", e)
        print("Wrong input. Please check the file paths and the image.")


def show_image(image, title):
    plt.title(title)
    plt.subplot(1, 1, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()


def show_two_images(image1, image2, title1, title2):
    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
    plt.title(title1)

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
    plt.title(title2)

    plt.show()
