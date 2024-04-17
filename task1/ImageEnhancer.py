import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


# Функция для увеличения резкости изображения
# Матрица kernel_sharpening
# Это ядро используется для выделения краев в изображении.
# Центральный элемент (9) увеличивает яркость центрального пикселя,
# в то время как окружающие его элементы с отрицательными значениями (-1) уменьшают яркость соседних пикселей.
# Это создает контраст на границах объектов, делая края более заметными и изображение кажется более резким.
def sharpen_image(image_path):
    # Загрузка изображения по указанному пути
    image = cv2.imread(image_path)
    # Создание ядра для увеличения резкости, где центральный пиксель имеет высокую положительную весовую характеристику
    # окруженную отрицательными значениями для выделения границ
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    # Применение свертки для увеличения резкости изображения
    sharpened_image = cv2.filter2D(image, -1, kernel_sharpening)
    return sharpened_image


# Альтернативный метод увеличения резкости изображения с использованием фильтрации
# force=2.5: Этот параметр определяет интенсивность эффекта увеличения резкости.
# Чем больше значение, тем сильнее увеличение резкости.
def sharpen_image_alternative(image_path, force=2.5):
    # Загрузка изображения по указанному пути
    image = cv2.imread(image_path)
    # Сначала размываем изображение
    blured_image = blur_image(image_path, (0, 0), 10)
    # Затем добавляем размытое изображение к исходному с определенными весами,
    # чтобы создать эффект увеличения резкости
    sharpened_image = cv2.addWeighted(image, 1.0 + force, blured_image, -force, 0.0)
    return sharpened_image


# Функция для размытия изображения с использованием Гауссового фильтра
# kernel_size Этот параметр определяет размер матрицы, которая будет использоваться для размытия.
# Каждый элемент в ядре умножается на значение пикселя, который он покрывает,
# и результаты суммируются для получения нового значения центрального пикселя.
# Увеличение kernel_size приведет к более размытом изображению,
# поскольку больше пикселей окрестности участвуют в вычислении каждого нового пикселя.
# Уменьшение kernel_size приведет к менее сильному размытию, сохраняя больше деталей изображения.
# Изменение sigmaX:
# Увеличение sigmaX приведет к тому, что веса в Гауссовом ядре
# будут уменьшаться менее стремительно, что приводит к более мягкому и широкому размытию.
# Уменьшение sigmaX сделает уменьшение весов более резким, что приводит к более "жесткому" и локализованному размытию.
def blur_image(image_path, kernel_size=(5, 5), sigmaX=20):
    # Загрузка изображения по указанному пути
    image = cv2.imread(image_path)
    # Применение Гауссового размытия к изображению с заданными размером ядра и сигма-значениями
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
