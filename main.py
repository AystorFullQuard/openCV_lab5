from Constants import *
from task1.ImageEnhancer import *


def test_task1(image_path, image):
    save_image(Paths.results_path.value, image, 'original_image_test.jpg')

    blurred_image = blur_image(image_path, kernel_size=(15, 15), sigmaX=20)
    show_two_images(image, blurred_image, 'Original Image', 'Blurred Image')
    save_image(Paths.results_path.value, blurred_image, 'blurred_image_test.jpg')

    sharpened_image_1 = sharpen_image(image_path)
    show_two_images(image, sharpened_image_1, 'Original Image', 'Sharpened Image')
    save_image(Paths.results_path.value, sharpened_image_1, 'sharpened_image_1_test.jpg')

    sharpened_image_2 = sharpen_image_alternative(image_path, 1)
    show_two_images(image, sharpened_image_2, 'Original Image', 'Sharpened Image alt')
    save_image(Paths.results_path.value, sharpened_image_2, 'sharpened_image_2_test.jpg')


if __name__ == '__main__':
    test_images_jpg_files = [f for f in os.listdir(Paths.test_images_path.value) if f.endswith('.jpg')]
    image_path = Paths.test_images_path.value + '\\' + test_images_jpg_files[0]
    image = cv2.imread(image_path)

    test_task1(image_path, image)
