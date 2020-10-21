import xlrd
import xlwt
import numpy as np
from extract_data import *


def read_votes(name):
    pat = r"C:\Users\17998\Desktop\MCM_ICN" + "\\" + name + ".xlsx"
    excel = xlrd.open_workbook(pat)
    sheet = excel.sheet_by_name(name)
    help_votes = sheet.col_values(8)
    total_votes = sheet.col_values(9)
    return help_votes[1:], total_votes[1:]


def wilson_score(pos, total, p_z=2.):
    """
    威尔逊得分计算函数
    参考：https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
    :param pos: 正例数
    :param total: 总数
    :param p_z: 正太分布的分位数
    :return: 威尔逊得分
    """
    pos += 1
    total += 1
    pos_rat = pos * 1. / total * 1.  # 正例比率
    score = (pos_rat + (np.square(p_z) / (2. * total))
             - ((p_z / (2. * total)) * np.sqrt(4. * total * (1. - pos_rat) * pos_rat + np.square(p_z)))) / \
            (1. + np.square(p_z) / total)
    return score


def get_review(name):
    help_votes, total_votes = read_votes(name)
    scores = []
    for i in range(len(help_votes)):
        print(type(help_votes[i]), type(total_votes[i]))
        if isinstance(help_votes[i], float) and isinstance(total_votes[i], float):
            scores.append(wilson_score(help_votes[i], total_votes[i]))
    print(scores)
    return scores


def get_wilson(name):
    help_votes, total_votes = read_votes(name)
    scores = []
    for i in range(len(help_votes)):
        print(type(help_votes[i]), type(total_votes[i]))
        if isinstance(help_votes[i], float) and isinstance(total_votes[i], float):
            scores.append(wilson_score(help_votes[i], total_votes[i]))
    print(scores)
    return scores


def get_wilson_weight(help_votes, total_votes):
    scores = []
    for i in range(len(help_votes)):
        scores.append(wilson_score(help_votes[i], total_votes[i]))
    sum_score = sum(scores)
    weights = []
    for _ in scores:
        weights.append(_ / sum_score)
    return weights


if __name__ == "__main__":
    scores = get_wilson("pacifier")
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    for i in range(len(scores)):
        worksheet.write(i, 0, label=str(scores[i]))
    workbook.save(r'C:\Users\17998\Desktop\MCM_ICN\wilson_score_pacifier.xls')

