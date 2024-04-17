import os.path

import cv2

from task1.ImageEnhancer import save_image


def detect_face(image_path, scaleFactor=1.3, minNeighbors=5, output_path=None, filename=None):
    # Загружаем предварительно обученный классификатор Haar Cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Читаем изображение
    image = cv2.imread(image_path)

    # Конвертируем изображение в градации серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Обнаруживаем лица в изображении
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor, minNeighbors)
    if len(faces) == 0:
        relative_image_path = os.path.relpath(image_path, start=os.path.curdir)
        print(f'No face detected for {relative_image_path}')
        return None
    else:
        # Создаем словарь для хранения результата
        result = {
            'image': None,
            'faces': None
        }

        for (x, y, w, h) in faces:
            center = (x + w // 2, y + h // 2)
            axes = (w // 2, h // 2)
            cv2.ellipse(image, center, axes, 0, 0, 360, color=(255, 0, 255), thickness=2)

        x, y, w, h = faces[0]
        if output_path and filename:
            print(f"Face detected at coordinates: ({x}, {y}, {w}, {h})")
            save_image(output_path, image, filename)
            print(f"Image saved to {output_path}")
        result['image_detected_face'] = image  # Добавляем изображение с эллипсом в словарь
        result['faces'] = faces
        return result
