from Bayesian_method import cal_grade
from extract_data import get_msg_star
from extract_data import get_10_most_popular
from extract_data import read_excel
import xlwt


def cal_grades(name):
    msgs = get_msg_star(name)
    scores = []
    for msg in msgs:
        scores.append(cal_grade(msg))
    most = get_10_most_popular(read_excel(name))
    result = []
    for i in range(len(most)):
        result.append((most[i][0], scores[i]))
    print(result)
    return result


if __name__ == "__main__":
    result = cal_grades("pacifier")
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    for i in range(len(result)):
        worksheet.write(i, 0, label=str(result[i][0]))
        worksheet.write(i, 1, label=str(result[i][1]))
    workbook.save(r'C:\Users\17998\Desktop\MCM_ICN\star_grade_hair_pacifier.xls')
