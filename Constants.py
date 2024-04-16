import os
from enum import Enum


class Paths(Enum):
    project_path = os.path.dirname(os.path.realpath(__file__))
    test_images_path = os.path.join(project_path, 'test_images')
    output_path = os.path.join(project_path, 'results')
