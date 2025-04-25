import os
from pyread import Pyread
from visualizer.pointcloud import visualize_pointcloud

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

pyread = Pyread(file_path=ROOT_DIR + "/test.yaml")
pyread.read()