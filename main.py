from Constants import *
from task1.ImageEnhancer import *
from task2.ImageDetection import *
from task3.PassportControl import *
from task4.Accuracy import check_accuracy


def test_task1(image_path, image):
    save_image(Paths.results_path_task1.value, image, 'original_image_test.jpg')

    blurred_image = blur_image(image_path, kernel_size=(15, 15), sigmaX=20)
    show_two_images(image, blurred_image, 'Original Image', 'Blurred Image')
    save_image(Paths.results_path_task1.value, blurred_image, 'blurred_image_test.jpg')

    sharpened_image_1 = sharpen_image(image_path)
    show_two_images(image, sharpened_image_1, 'Original Image', 'Sharpened Image')
    save_image(Paths.results_path_task1.value, sharpened_image_1, 'sharpened_image_1_test.jpg')

    sharpened_image_2 = sharpen_image_alternative(image_path, 1)
    show_two_images(image, sharpened_image_2, 'Original Image', 'Sharpened Image alt')
    save_image(Paths.results_path_task1.value, sharpened_image_2, 'sharpened_image_2_test.jpg')


def test_task2(image_path):
    detected_face = detect_face(image_path, scaleFactor=1.3, minNeighbors=5, output_path=Paths.results_path_task2.value,
                                filename='detected_face.jpg')
    if detected_face is not None:
        print(detected_face['faces'])
    else:
        print("Failed to detect a face in the image")


def test_task3(image_path, image):
    show_image(image, 'Passport check Image')
    result = passport_photo_check(image_path, output_path=Paths.results_path_task3.value, filename='passport_image.jpg')
    print(result)


if __name__ == '__main__':
    test_images_jpg_files = [f for f in os.listdir(Paths.test_images_path.value) if f.endswith('7E0875.jpg')]
    #test_images_jpg_files = [f for f in os.listdir(Paths.test_images_path.value) if f.endswith('.jpg')]

    image_path = Paths.test_images_path.value + '\\' + test_images_jpg_files[0]
    image = cv2.imread(image_path)
    # task1
    #test_task1(image_path, image)
    # task 2
    #test_task2(image_path)
    # task 3
    #test_task3(image_path, image)
    # task 4
    check_accuracy(Paths.csv_path.value)
