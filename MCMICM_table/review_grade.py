from extract_data import get_msg
from WIlson import get_wilson_weight
from most_popular import get_10_most_popular, read_excel
import xlwt


def cal_grade(msg_list):
    help_votes = []
    total_votes = []
    review = []
    for msg in msg_list:
        print(msg)
        help_votes.append(msg[0])
        total_votes.append(msg[1])
        review.append(msg[2])
    weights = get_wilson_weight(help_votes, total_votes)
    score = 0
    for i in range(len(review)):
        score += weights[i] * review[i]
    return score


def cal_grades(name):
    msgs = get_msg(name)
    scores = []
    for msg in msgs:
        scores.append(cal_grade(msg))
    most = get_10_most_popular(read_excel(name))
    sum_s = sum(scores)
    result = []
    res_o = []
    for i in range(len(most)):
        result.append((most[i][0], scores[i]))
        res_o.append((most[i][0], scores[i] / sum_s))
    print(result)
    print(res_o)
    return result


if __name__ == "__main__":
    result = cal_grades("hair_dryer")
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    for i in range(len(result)):
        worksheet.write(i, 0, label=str(result[i][0]))
        worksheet.write(i, 1, label=str(result[i][1]))
    workbook.save(r'C:\Users\17998\Desktop\MCM_ICN\review_grade_hair_dryer.xls')
