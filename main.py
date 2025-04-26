import os
from pyread import Pyread

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

pyread = Pyread(file_path=ROOT_DIR + "/examples/test.yaml")
pyread.read()
pyread.file_path = ROOT_DIR + "/examples/bunny.pcd"
pyread.read()
