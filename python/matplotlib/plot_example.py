# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)    # 作图的变量自变量

y = np.sin(x) + 1      # 因变量 y
z = np.cos(x**2) + 1   # 因变量 z

plt.rcParams['font.sans-serif'] = ['SimHei']    # 用于显示中文标签
plt.rcParams['axes.unicode_minus'] = False      # 用于正常显示负号

plt.figure(figsize=(8, 4))    # 设置图像大小
plt.plot(x, y, label='$\ sinx + 1$', color='red', linewidth=2)     # 作图设置标签、线条颜色、线条大小
plt.plot(x, z, 'b--', label='$\ cos x^2+1$')                          # 作图设置标签、线条类型
plt.xlabel('Time(s)')    # x轴名称
plt.ylabel('Volt')       # y轴名称
plt.title('A simple example 你好')     # 标题
plt.ylim(-0.2, 2.2)         # 显示的y轴范围
plt.legend()             # 显示图例
plt.show()               # 显示作图结果

