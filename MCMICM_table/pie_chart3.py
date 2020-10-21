from bar_chart import figure_deal
from pie_chart import read_excel
import matplotlib.pyplot as plt
import matplotlib as mpl


def draw_pie(star_dict):
    x = ["1 star", "2 stars", "3 stars", "4 stars", "5 stars"]
    y = list(star_dict.values())
    sum_v = sum(y)
    for v in y:
        v /= sum_v
    plt.figure(1, figsize=(6, 6))
    # For China, make the piece explode a bit
    expl = [0, 0, 0, 0, 0.1]  # 第二块即China离开圆心0.1
    # Colors used. Recycle if not enough.
    colors = ["blue", "red", "coral", "green", "yellow"]  # 设置颜色（循环显示）
    # Pie Plot
    # autopct: format of "percent" string;百分数格式
    plt.pie(y, explode=expl, colors=colors, labels=x, autopct='%1.1f%%', pctdistance=0.8, shadow=True)
    plt.title('Pacifier Star Distribution', bbox={'facecolor': '0.8', 'pad': 5})
    plt.show()


if __name__ == "__main__":
    hair_drier = read_excel("hair_dryer")
    microwave = read_excel("microwave")
    pacifier = read_excel("pacifier")
    hair_drier_dict = figure_deal(hair_drier)
    microwave_dict = figure_deal(microwave)
    pacifier_dict = figure_deal(pacifier)
    draw_pie(pacifier_dict)