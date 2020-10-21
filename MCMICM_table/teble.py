import xlrd
import matplotlib.pyplot as plt


# 添加数据标签 就是矩形上面的数值
def add_labels(rects, words):
    for i in range(len(rects)):
        height = rects[i].get_height()
        plt.text(rects[i].get_x() + rects[i].get_width()/2, height,  words[i], ha='center', va='bottom')
        rects[i].set_edgecolor('white')


def read_table(name):
    pat = r"C:\Users\17998\Documents\Tencent Files\1799878714\FileRecv\2e\2e\hair_dryer" + "\\" + name + ".xlsx"
    excel = xlrd.open_workbook(pat)
    sheet = excel.sheet_by_index(0)
    words = sheet.col_values(1)[1:3]
    frequency = sheet.col_values(2)[1:3]
    return words, frequency


def read_star(i, state):
    star = ""
    if i == 1:
        star = "one"
    elif i == 2:
        star = "two"
    elif i == 3:
        star = "three"
    elif i == 4:
        star = "four"
    elif i == 5:
        star = "five"
    file_name = star + "_" + state + "_" + "words"
    return read_table(file_name)


def read_all_stars(state):
    all_words = []
    all_frequency = []
    for i in range(1, 6):
        words, frequency = read_star(i, state)
        all_words.append(words)
        all_frequency.append(frequency)
    return all_words, all_frequency


def draw_pic(all_words, all_frequency):
    num = list(range(1, 6))
    plt.figure(figsize=(10, 5))  # 设置画布的尺寸
    plt.title('Negative Word frequency in each rating of hair dryer', fontsize=20)  # 标题，并设定字号大小
    plt.xlabel(u'star range', fontsize=14)  # 设置x轴，并设定字号大小
    plt.ylabel(u'occurrence times', fontsize=14)  # 设置y轴，并设定字号大小
    width_val = 0.3  # 若显示 n 个柱状图，则width_val的值需小于1/n ，否则柱形图会有重合
    first_most = []
    second_most = []
    for words in all_words:
        first_most.append(words[0])
        second_most.append(words[1])
    first_freq = []
    second_freq = []
    for freq in all_frequency:
        first_freq.append(freq[0])
        second_freq.append(freq[1])
    second_word = plt.bar(num, second_freq, alpha=0.6, width=width_val, facecolor='darkblue',
                             edgecolor='darkblue',
                             lw=1, label='second most occurrence')
    for i in range(len(num)):
        num[i] += width_val
    first_word = plt.bar(num, first_freq, alpha=0.6, width=width_val, facecolor='green',
                            edgecolor='darkblue',
                            lw=1, label='most occurrence')
    add_labels(second_word, second_most)
    add_labels(first_word, first_most)
    plt.legend(loc=2)  # 图例展示位置，数字代表第几象限
    plt.show()  # 显示图像6


if __name__ == "__main__":
    all_words, all_frequency = read_all_stars("negative")
    draw_pic(all_words, all_frequency)