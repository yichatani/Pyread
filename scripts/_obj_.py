import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 加载 .obj 文件
mesh = trimesh.load('/home/ani/synthesize_pregrasp/envs/assets/plate_cvx_simple.obj')

# 创建一个 3D 图形窗口
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 获取网格的顶点和面
vertices = mesh.vertices
faces = mesh.faces

# 绘制3D三角网格
ax.plot_trisurf(vertices[:, 0], vertices[:, 1], faces, vertices[:, 2], cmap='viridis', edgecolor='k')

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 显示图形
plt.show()
