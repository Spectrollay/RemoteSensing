import numpy as np
from scipy.signal import savgol_filter

#从文件中读取
file_path = "/workespace/Remopote/Sensing/SG/123.txt"
data = []
with open(file_path,'r') as file :
    for line in file:
        row = line.strip().split(' ')
        data.append(row)
print (data)

#测试
data = np.array([1,2,3])  # 数据

# 应用Savitzky-Golay滤波
filtered_data = savgol_filter(data, window_length=3, polyorder=2)
