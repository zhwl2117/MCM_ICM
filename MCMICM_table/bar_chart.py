import matplotlib.pyplot as plt
from pie_chart import read_excel


# 添加数据标签 就是矩形上面的数值
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2, height, height, ha='center', va='bottom')
        rect.set_edgecolor('white')


def draw_bars(start_dict_list):
    plt.figure(figsize=(10, 5))  # 设置画布的尺寸
    plt.title('Star Distribution', fontsize=20)  # 标题，并设定字号大小
    plt.xlabel(u'star range', fontsize=14)  # 设置x轴，并设定字号大小
    plt.ylabel(u'counts of star', fontsize=14)  # 设置y轴，并设定字号大小
    width_val = 0.3  # 若显示 n 个柱状图，则width_val的值需小于1/n ，否则柱形图会有重合
    hair_drier_star_dict = start_dict_list[0]
    microwave_star_dict = start_dict_list[1]
    pacifier_star_dict = start_dict_list[2]
    x = list(hair_drier_star_dict.keys())
    y_hair_dryer = list(hair_drier_star_dict.values())
    y_microwave = list(microwave_star_dict.values())
    y_pacifier = list(pacifier_star_dict.values())
    for i in range(len(x)):
        x[i] -= width_val
    rect_hair_dryer = plt.bar(x, y_hair_dryer, alpha=0.6, width=width_val, facecolor='deeppink', edgecolor='deeppink', lw=1,
            label='hair dryer')
    for i in range(len(x)):
        x[i] += width_val
    rect_microwave = plt.bar(x, y_microwave, alpha=0.6, width=width_val, facecolor='darkblue',
            edgecolor='darkblue',
            lw=1, label='microwave')
    for i in range(len(x)):
        x[i] += width_val
    rect_pacifier = plt.bar(x, y_pacifier, alpha=0.6, width=width_val, facecolor='green',
            edgecolor='darkblue',
            lw=1, label='pacifier')
    add_labels(rect_hair_dryer)
    add_labels(rect_microwave)
    add_labels(rect_pacifier)
    plt.legend(loc=2)  # 图例展示位置，数字代表第几象限
    plt.show()  # 显示图像6


def figure_deal(star_list):
    star_set = [1, 2, 3, 4, 5]
    star_dict = {}
    for star in star_set:
        star_dict[star] = star_list.count(star)
    return star_dict


if __name__ == "__main__":
    hair_drier = read_excel("hair_dryer")
    microwave = read_excel("microwave")
    pacifier = read_excel("pacifier")
    hair_drier_dict = figure_deal(hair_drier)
    microwave_dict = figure_deal(microwave)
    pacifier_dict = figure_deal(pacifier)
    draw_bars([hair_drier_dict, microwave_dict, pacifier_dict])
