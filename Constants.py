import os
from enum import Enum


class Paths(Enum):
    project_path = os.path.dirname(os.path.realpath(__file__))
    test_images_path = os.path.join(project_path, 'test_images')
    results_path = os.path.join(project_path, 'results')
    results_path_task1 = os.path.join(results_path, 'task1')
