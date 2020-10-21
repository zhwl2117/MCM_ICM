import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
datafile = u'D:\\pythondata\\learn\\matplotlib.xlsx'
data = pd.read_excel(datafile)

plt.figure(figsize=(10, 5))  # 设置画布的尺寸
plt.title('Examples of Histogram', fontsize=20)  # 标题，并设定字号大小
plt.xlabel(u'x-year', fontsize=14)  # 设置x轴，并设定字号大小
plt.ylabel(u'y-income', fontsize=14)  # 设置y轴，并设定字号大小

width_val = 0.4  # 若显示 n 个柱状图，则width_val的值需小于1/n ，否则柱形图会有重合

# alpha：透明度；width：柱子的宽度；facecolor：柱子填充色；edgecolor：柱子轮廓色；lw：柱子轮廓的宽度；label：图例；
plt.bar(data['时间'], data['收入_Jay'], alpha=0.6, width=width_val, facecolor='deeppink', edgecolor='deeppink', lw=1,
        label='Jay income')
plt.bar(data['时间'] + width_val, data['收入_JJ'], alpha=0.6, width=width_val, facecolor='darkblue', edgecolor='darkblue',
        lw=1, label='JJ income')

plt.legend(loc=2)  # 图例展示位置，数字代表第几象限
plt.show()  # 显示图像6