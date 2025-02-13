import h5py

h5_file_path = "/media/mldadmin/home/s124mdg32_04/Dataset/mnt/data1/data_ifl/scene20/2_scene.hdf5"

# Read structure
# with h5py.File(h5_file_path, 'r') as f:
#     def print_hdf5_structure(name, obj):
#         print(name)
#     f.visititems(print_hdf5_structure)


with h5py.File(h5_file_path, 'r') as f:
    
    dset = f['non_colliding_grasps/paralleljaw/contact_width']
    print("Dataset shape:", dset.shape)
    print("First 10 values:", dset[:300]) 
