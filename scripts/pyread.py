import os
import h5py
import json
import yaml
import zarr
import pickle
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import trimesh


class Pyread:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        ext = os.path.splitext(self.file_path)[-1].lower()
        if ext == ".h5":
            self.read_hdf5_structure()
        elif ext == ".npz":
            self.read_npz()
        elif ext == ".npy":
            self.read_npy()
        elif ext == ".obj":
            self.read_obj()
        elif ext == ".json":
            self.read_json()
        elif ext in [".yaml", ".yml"]:
            self.read_yaml()
        elif ext == ".bin":
            self.read_bin_pointcloud()
        elif ext == ".pcd":
            self.read_pcd()
        elif ext in [".pkl", ".pickle"]:
            self.read_pickle()
        elif ext == ".csv":
            self.read_csv()
        elif ext == ".zarr":
            self.read_zarr_structure()
        else:
            print("Unsupported file type.")

    def read_obj(self):
        try:
            mesh = trimesh.load(self.file_path)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            vertices = mesh.vertices
            faces = mesh.faces
            ax.plot_trisurf(vertices[:, 0], vertices[:, 1], faces, vertices[:, 2],
                            cmap='viridis', edgecolor='k')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            plt.title("3D Mesh Viewer")
            plt.show()
        except Exception as e:
            print(f"Error reading .obj file: {e}")

    def read_hdf5_structure(self):
        try:
            with h5py.File(self.file_path, 'r') as f:
                def print_hdf5_structure(name, obj):
                    print(name)
                f.visititems(print_hdf5_structure)
        except Exception as e:
            print(f"Error reading .h5 structure: {e}")

    def read_hdf5_values(self, key):
        try:
            with h5py.File(self.file_path, 'r') as f:
                dset = f[key]
                print("Dataset shape:", dset.shape)
                print("First 5 values:", dset[:5])
        except Exception as e:
            print(f"Error reading key '{key}': {e}")

    def read_npz(self):
        data_dict = {}
        try:
            data = np.load(self.file_path)
            print(f"Keys in '{self.file_path}': {data.files}")
            for key in data.files:
                print(f"Key: {key}, Shape: {data[key].shape}, Data Type: {data[key].dtype}")
                data_dict[key] = data[key]
        except Exception as e:
            print(f"Error reading .npz file: {e}")
            return None

        for key, value in data_dict.items():
            print(f"\nKey: {key}")
            print(f"First elements: {value[:1]}")

    def read_npy(self):
        try:
            depth_data = np.load(self.file_path)
            plt.imshow(depth_data, cmap='viridis')
            plt.colorbar(label="Depth")
            plt.title("Depth Map")
            plt.show()
        except Exception as e:
            print(f"Error reading .npy file: {e}")

    def read_json(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                print(json.dumps(data, indent=2))
        except Exception as e:
            print(f"Error reading .json file: {e}")

    def read_yaml(self):
        try:
            with open(self.file_path, 'r') as f:
                data = yaml.safe_load(f)
                print(data)
        except Exception as e:
            print(f"Error reading .yaml file: {e}")

    def read_bin_pointcloud(self):
        try:
            pointcloud = np.fromfile(self.file_path, dtype=np.float32).reshape(-1, 4)
            print(f"Loaded point cloud shape: {pointcloud.shape}")
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(pointcloud[:, 0], pointcloud[:, 1], pointcloud[:, 2], s=1, c=pointcloud[:, 3], cmap='viridis')
            ax.set_title("PointCloud from .bin")
            plt.show()
        except Exception as e:
            print(f"Error reading .bin file: {e}")

    def read_pcd(self):
        print("PCD reader not implemented. You can use open3d or pypcd.")

    def read_pickle(self):
        try:
            with open(self.file_path, 'rb') as f:
                obj = pickle.load(f)
                print(f"Unpickled object type: {type(obj)}")
                print(obj)
        except Exception as e:
            print(f"Error reading .pkl file: {e}")

    def read_csv(self):
        try:
            df = pd.read_csv(self.file_path)
            print(df.head())
        except Exception as e:
            print(f"Error reading .csv file: {e}")

    def read_zarr_structure(self):
        try:
            z = zarr.open(self.file_path, mode='r')
            print("Zarr structure:")
            print(z.tree())
        except Exception as e:
            print(f"Error reading .zarr structure: {e}")

if __name__ == "__main__":
    reader = Pyread("/path/to/your/file")
    reader.read()
    reader.read_hdf5_values("some/key")
