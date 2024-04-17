import cv2
import pandas as pd
import os

from Constants import Paths
from task1.ImageEnhancer import save_image
from task3.PassportControl import passport_photo_check


def check_accuracy(csv_path):
    csv_file = pd.read_csv(csv_path)
    correct_detections = 0
    test_images_jpg_files = [f for f in os.listdir(Paths.test_images_path.value) if f.endswith('.jpg')]
    for filename in os.listdir(Paths.results_path_task4.value):
        os.remove(os.path.join(Paths.results_path_task4.value, filename))

    for test_image in test_images_jpg_files:
        image_path = os.path.join(Paths.test_images_path.value, test_image)

        result = passport_photo_check(image_path, scaleFactor=1.3, minNeighbors=2)
        file_name = 'test_images/' + os.path.basename(image_path)

        actual_label = csv_file[csv_file['new_path'] == file_name]['label'].item()
        if (result == "Photo is suitable for a passport" and actual_label == True) or \
                (result != "Photo is suitable for a passport" and actual_label == False):
            correct_detections += 1

        if result == "Photo is suitable for a passport" and actual_label == True:
            save_image(output_path=Paths.results_path_task4.value, image=cv2.imread(image_path),
                       filename=f'detected_face_true_{correct_detections}.jpg')
        elif result != "Photo is suitable for a passport" and actual_label == False:
            save_image(output_path=Paths.results_path_task4.value, image=cv2.imread(image_path),
                       filename=f'detected_face_false_{correct_detections}.jpg')

    accuracy = correct_detections / len(csv_file)
    print(f'Correct detections: {correct_detections}')
    print(f'Accuracy of the system is: {accuracy:.3f}')
