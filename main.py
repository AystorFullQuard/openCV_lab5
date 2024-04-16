from Constants import *
from task1.ImageEnhancer import *


def print_hi(name):
    print(f'Hi, {name}')


def test_task1(image_path, image):
    blurred_image = blur_image(image_path, kernel_size=(15, 15), sigmaX=20)
    show_two_images(image, blurred_image, 'Original Image', 'Blurred Image')

    sharpened_image_1 = sharpen_image(image_path)
    show_two_images(image, sharpened_image_1, 'Original Image', 'Sharpened Image')

    sharpened_image_2 = sharpen_image_alternative(image_path, 1)
    show_two_images(image, sharpened_image_2, 'Original Image', 'Sharpened Image alt')


if __name__ == '__main__':
    test_images_jpg_files = [f for f in os.listdir(Paths.test_images_path.value) if f.endswith('.jpg')]
    original_image_path = Paths.test_images_path.value + '\\' + test_images_jpg_files[1]
    original_image = cv2.imread(original_image_path)

    test_task1(original_image_path, original_image)
