import matplotlib.pyplot as plt
import pandas as pd
import xlrd
from combine_algo import combine


def read_data(pat):
    excel = xlrd.open_workbook(pat)
    sheet = excel.sheet_by_index(0)
    name, data = sheet.col_values(0), sheet.col_values(1)
    return name, data


def draw_pic(names, datas):
    b = []
    for i in range(len(datas[0])):  # 行数
        t = []
        for j in range(len(datas)):
            t.append(datas[j][i])
        b.append(t)
    df = pd.DataFrame(b,
                      index=names[0],
                      columns=pd.Index(['review grade', 'star grade', 'combined grade'], name='Genus'))
    plt.figure(figsize=(20, 10))
    rect1 = [0.1, 0.1, 0.75, 0.75]
    axe = plt.axes(rect1)
    x = df.plot.barh(ax=axe, alpha=0.7, legend=False)
    axe.set_title('The different types of scores of pacifier')
    axe.legend(loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=-0.2)
    plt.savefig(r'C:\Users\17998\Desktop\MCM_ICN\pacifier.png')


def get_datas(name):
    path = r"C:\Users\17998\Desktop\MCM_ICN" + "\\"
    review_pat = path + "review_grade_" + name + ".xls"
    score_pat = path + "star_grade_" + name + ".xls"
    names = []
    datas = []
    name, data = read_data(review_pat)
    names.append(name)
    datas.append(data)
    name1, data1 = read_data(score_pat)
    names.append(name1)
    datas.append(data1)
    com = combine(data1, data)
    names.append(name)
    datas.append(com)
    return names, datas


if __name__ == "__main__":
    names, datas = get_datas("pacifier")
    draw_pic(names, datas)







