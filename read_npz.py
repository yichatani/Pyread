import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-file_path", default="/Users/mayicheng/Downloads/grasp_label/001_labels.npz")
args = parser.parse_args()

def read_npz(file_path):
    """
    读取 .npz 文件并显示其中的内容。

    Args:
        file_path (str): .npz 文件的路径。

    Returns:
        dict: 包含 .npz 文件内容的字典。
    """
    try:
        # 读取 .npz 文件
        data = np.load(file_path)
        
        # 输出文件中包含的变量名称
        print(f"Keys in '{file_path}': {data.files}")
        
        # 遍历文件内容
        for key in data.files:
            print(f"Key: {key}, Shape: {data[key].shape}, Data Type: {data[key].dtype}")
        

        # 将数据转为字典返回
        data_dict = {key: data[key] for key in data.files}
        return data_dict
    except Exception as e:
        print(f"Error reading .npz file: {e}")
        return None

if __name__ == "__main__":
    # 替换为你的 .npz 文件路径
    file_path = args.file_path
    
    # 调用函数读取文件
    content = read_npz(file_path)
    
    if content:
        for key, value in content.items():
            print(f"\nKey: {key}")
            
            # 只打印前10个元素
            # if value.ndim == 1:  # 一维数组
            #     print(f"First 10 elements: {value[:10]}")
            # elif value.ndim > 1:  # 多维数组
            #     print(f"First 10 elements (flattened): {value.flatten()[:10]}")
            print(f"First elements: {value[:1]}")
