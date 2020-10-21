import xlrd
from pylab import *


def read_excel(name):
    pat = r"C:\Users\17998\Desktop\MCM_ICN" + "\\" + name + ".xlsx"
    excel = xlrd.open_workbook(pat)
    sheet = excel.sheet_by_name(name)
    helpful_votes = sheet.col_values(8)
    total_votes = sheet.col_values(9)
    helpful_votes = helpful_votes[1:]
    helpful_votes1 = []
    total_votes = total_votes[1:]
    unhelpful_votes = []
    len1 = len(helpful_votes)
    len2 = len(total_votes)
    for i in range(len(total_votes)):
        if total_votes[i] != 0:
            unhelpful_votes.append(total_votes[i] - helpful_votes[i])
            helpful_votes1.append(helpful_votes[i])
    return helpful_votes1, unhelpful_votes


if __name__ == "__main__":
    hair_dryer_helpful, hair_dryer_unhelpful = read_excel("hair_dryer")
    length = len(hair_dryer_helpful)
    max_h = max(hair_dryer_helpful)
    max_u = max(hair_dryer_unhelpful)
    x = range(length)
    plt.figure(1)
    plt.bar(x, hair_dryer_helpful, 1 / length, color="coral")
    plt.title("vote distribution")
    plt.ylabel("helpfulness of review")
    plt.show()
