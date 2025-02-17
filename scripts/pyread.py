import h5py
import trimesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Pyread():
    def __init__(self, file_path):
        self.file_path = file_path

    def read_obj(self):
        """
        Read .obj file and plot the 3D mesh
        """
        mesh = trimesh.load(self.file_path)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        vertices = mesh.vertices
        faces = mesh.faces
        ax.plot_trisurf(vertices[:, 0], vertices[:, 1], faces, vertices[:, 2], cmap='viridis', edgecolor='k')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    
    def read_hdf5_structure(self):
        """
        Read the data structure of h5 files.    
        """
        # Read structure
        with h5py.File(self.file_path, 'r') as f:
            def print_hdf5_structure(name, obj):
                print(name)
            f.visititems(print_hdf5_structure)

    def read_hdf5_values(self, key):
        """
        Read the key values.
        """
        # Read key and values
        with h5py.File(self.file_path, 'r') as f:
            dset = f[key]
            print("Dataset shape:", dset.shape)
            print("First 10 values:", dset[:5])

    def read_npz(self):
        """
        Read .npz file and show the content.
        """
        try:
            # Read .npz file
            data = np.load(self.file_path)
            
            # Output the variable names in the file
            print(f"Keys in '{self.file_path}': {data.files}")
            
            # Traverse the file content
            for key in data.files:
                print(f"Key: {key}, Shape: {data[key].shape}, Data Type: {data[key].dtype}")
            
            # Convert data to dictionary and return
            data_dict = {key: data[key] for key in data.files}
            # return data_dict
        except Exception as e:
            print(f"Error reading .npz file: {e}")
            return None
        
        if data_dict:
            for key, value in data_dict.items():
                print(f"\nKey: {key}")
                
                # Only print the first 10 elements
                # if value.ndim == 1:  # one-dimensional array
                #     print(f"First 10 elements: {value[:10]}")
                # elif value.ndim > 1:  # multi-dimensional array
                #     print(f"First 10 elements (flattened): {value.flatten()[:10]}")
                print(f"First elements: {value[:1]}")