import os
from scripts.pyread import Pyread
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

pyread = Pyread(file_path=ROOT_DIR + "/test.yaml")
pyread.read()