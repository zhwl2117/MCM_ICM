import xlrd
from pylab import *


def read_excel(name):
    pat = r"C:\Users\17998\Desktop\MCM_ICN" + "\\" + name + ".xlsx"
    excel = xlrd.open_workbook(pat)
    sheet = excel.sheet_by_name(name)
    star_list = sheet.col_values(7)
    return star_list[1:]


def draw_bar(star_list):
    star_set = [1, 2, 3, 4, 5]
    star_dict = {}
    for star in star_set:
        star_dict[star] = star_list.count(star)
    star_key = list(star_dict.keys())
    star_value = list(star_dict.values())
    for i in range(len(star_key)):
        star_key[i] = int(star_key[i])
    x = np.array(star_key)
    y = np.array(star_value)
    plt.figure(1)
    plt.bar(x, y, 0.6)
    plt.title("star distribution")
    plt.xlabel("star range")
    plt.ylabel("counts of star")
    plt.show()


def draw_bars(product_list):
    star_set = [1, 2, 3, 4, 5]
    star_dict = {}
    plt.figure(1)
    for star_list in product_list:
        for star in star_set:
            star_dict[star] = star_list.count(star)
        star_key = list(star_dict.keys())
        star_value = list(star_dict.values())
        x = np.array(star_key)
        y = np.array(star_value)
        plt.bar(x, y, alpha=0.6)
    plt.title("star distribution")
    plt.xlabel("star range")
    plt.ylabel("counts of star")
    plt.show()


if __name__ == "__main__":
    hair_drier = read_excel("hair_dryer")
    microwave = read_excel("microwave")
    pacifier = read_excel("pacifier")
    draw_bars([hair_drier, microwave, pacifier])

