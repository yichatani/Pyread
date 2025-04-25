# Pyread


## Preview

Try to solve **'can't open it'** when facing `.npz`  `.npy`  `.hdf5` `.json` ...

✅ **Fully Integrated**: The `Pyread` class supports reading and visualizing a wide range of commonly used scientific data formats:

- `.h5` / `.npz` / `.npy` — Scientific data arrays  
- `.obj` — 3D mesh models  
- `.json` / `.yaml` — Configuration or annotation files  
- `.bin` — Binary point cloud data (e.g., from LiDAR)  
- `.csv` — Structured tabular data  
- `.pkl` / `.pickle` — Serialized Python objects  
- `.zarr` — Chunked and compressed multi-dimensional arrays  
- `.pcd` — Placeholder for point cloud files *(recommended to use Open3D for full support)*
- `.ckpt` — Training checkpoint files  

## Point cloud visualizer

```bash
pip install kaleido plotly
cd visualizer
python setup.py install
```