import os
from enum import Enum


class Paths(Enum):
    project_path = os.path.dirname(os.path.realpath(__file__))
    test_images_path = os.path.join(project_path, 'test_images')
    results_path = os.path.join(project_path, 'results')
    results_path_task1 = os.path.join(results_path, 'task1')
    results_path_task2 = os.path.join(results_path, 'task2')
    results_path_task4 = os.path.join(results_path, 'task4')
    csv_path = os.path.join(project_path, 'test.csv')
