import xlrd
import matplotlib.pyplot as plt


def read_table(name):
    path = r"C:\Users\17998\Documents\Tencent Files\1799878714\FileRecv\aspect (1)\aspect\aspect_" + name + ".xlsx"
    excel = xlrd.open_workbook(path)
    sheet = excel.sheet_by_index(0)
    aspects = sheet.col_values(1)[1:]
    return aspects


def count_aspect(aspects):
    set_aspect = set(aspects)
    aspect_dict = {}
    for s in set_aspect:
        aspect_dict[s] = aspects.count(s)
    return aspect_dict


def draw_pie(aspect_dict):
    x = list(aspect_dict.keys())
    y = list(aspect_dict.values())
    sum_v = sum(y)
    for v in y:
        v /= sum_v
    plt.figure(1, figsize=(6, 6))
    # For China, make the piece explode a bit
    expl = [0, 0.1, 0, 0]  # 第二块即China离开圆心0.1
    # Colors used. Recycle if not enough.
    colors = ["blue", "coral", "green", "yellow"]  # 设置颜色（循环显示）
    # Pie Plot
    # autopct: format of "percent" string;百分数格式
    plt.pie(y, explode=expl, colors=colors, labels=x, autopct='%1.1f%%', pctdistance=0.8, shadow=True)
    plt.title('Aspects of review distribution of pacifier', bbox={'facecolor': '0.8', 'pad': 5})
    plt.show()


if __name__ == "__main__":
    draw_pie(count_aspect(read_table("pacifier")))