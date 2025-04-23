import os
import h5py
import trimesh
import numpy as np
import matplotlib.pyplot as plt
import cv2
from mpl_toolkits.mplot3d import Axes3D


class Pyread:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        """
        Automatically select the reading method based on the file extension
        """
        ext = os.path.splitext(self.file_path)[-1].lower()
        if ext == ".h5":
            self.read_hdf5_structure()
        elif ext == ".npz":
            self.read_npz()
        elif ext == ".npy":
            self.read_npy()
        elif ext == ".obj":
            self.read_obj()
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


if __name__ == "__main__":

    # read .h5
    reader = Pyread("/home/ani/astar/my_Isaac/episodes/episode_7.h5")
    reader.read()
    reader.read_hdf5_values("agent_pos")
    
    # read .npz
    reader = Pyread("/path/to/file.npz")
    reader.read()
    
    # read depth .npy
    reader = Pyread("/path/to/depth.npy")
    reader.read()
    
    # read .obj mesh file
    reader = Pyread("/path/to/mesh.obj")
    reader.read()
