import cv2
import numpy as np

from Constants import Paths
from task2.ImageDetection import detect_face


def is_photo_colored(image_path):
    image = cv2.imread(image_path)
    # Если изображение не было загружено, вернуть False
    if image is None:
        return False
    # Разделяем каналы изображения
    R, G, B = cv2.split(image)
    # Если все каналы одинаковы, изображение серое
    if np.array_equal(B, G) and np.array_equal(B, R):
        return False
    return True


def get_photo_orientation(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    if width > height:
        return "Landscape"
    elif height > width:
        return "Portrait"
    else:
        return "Square"


def get_face_coordinates(image_path):
    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # image = cv2.imread(image_path)
    # gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.5, minNeighbors=5)
    # return faces
    face_data = detect_face(image_path, scaleFactor=1.5, minNeighbors=6, output_path=Paths.results_path_task2.value,
                            filename='detected_face.jpg')
    if face_data is not None:
        return face_data['faces']
    return None


def check_eyes_level(image_path):
    eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = get_face_coordinates(image_path)
    if faces is not None:
        x, y, w, h = faces[0]
        roi_gray = gray_image[y:y + h, x:x + w]
        eyes = eyes_cascade.detectMultiScale(roi_gray)
        if len(eyes) == 2:
            eye1 = eyes[0]
            eye2 = eyes[1]
            if abs(eye1[1] - eye2[1]) <= 5:
                return True
    return False


def is_single_face(image_path):
    faces = get_face_coordinates(image_path)
    if faces is not None:
        return len(faces) == 1
    return False


def check_head_proportion(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    faces = get_face_coordinates(image_path)
    if faces is not None:
        if len(faces) > 0:
            x, y, w, h = faces[0]
            face_area = w * h
            image_area = width * height
            ratio = (face_area / image_area) * 100
            if 20 <= ratio <= 50:
                return True
    return False


def passport_photo_check(image_path):
    if not is_photo_colored(image_path):
        return "Image is not colored"
    if get_photo_orientation(image_path) == "Landscape":
        return "Image is not in portrait orientation or square"
    if not check_eyes_level(image_path):
        return "Eyes are not at the same level"
    if not is_single_face(image_path):
        return "More than one person in the photo"
    if not check_head_proportion(image_path):
        return "Head does not represent 20% to 50% of the area of the photo."
    return "Photo is suitable for a passport"
