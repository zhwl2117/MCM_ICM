import review_grade as rg
import Bayesian_method as Bm
from most_popular import get_10_most_popular,read_excel
import matplotlib.pyplot as plt
from extract_data import get_msg_year, get_msg_star_year


def combine(review_grade, star_grade, a=0.5):
    sum_review = sum(review_grade)
    for i in range(len(review_grade)):
        review_grade[i] /= sum_review
    sum_star = sum(star_grade)
    for i in range(len(star_grade)):
        star_grade[i] /= sum_star
    combine_grade = []
    for i in range(len(review_grade)):
        print(star_grade[i], review_grade[i], end=" ")
        combine_grade.append(a*star_grade[i]+(1-a)*review_grade[i])
    sum_combine = sum(combine_grade)
    for i in range(len(combine_grade)):
        combine_grade[i] /= sum_combine
    return combine_grade


def cal_review_grades(review_table):
    most = []
    for pro in review_table:
        years = []
        for year in pro:
            years.append(rg.cal_grade(year))
        most.append(years)
    return most


def cal_star_grades(star_table):
    most = []
    for pro in star_table:
        years = []
        for year in pro:
            years.append(Bm.cal_grade(year))
        most.append(years)
    return most


def cal_grades(review_table, star_table):
    most_review = cal_review_grades(review_table)
    most_star = cal_star_grades(star_table)
    combine_grade = []
    for i in range(len(most_review)):
        combine_grade.append(combine(most_review[i], most_star[i], a=0.6))
    return combine_grade


def draw_pic(combine_grade, name):
    x = range(2009, 2019)
    plt.figure(1)
    most = get_10_most_popular(read_excel(name))
    for i in range(len(combine_grade)):
        plt.plot(x, combine_grade[i], label=most[i][0])
    plt.title("product evaluation trend")
    plt.xlabel("years")
    plt.ylabel("evaluation")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    name = "hair_dryer"
    review_table = get_msg_year(name)
    star_table = get_msg_star_year(name)
    combine_grade = cal_grades(review_table, star_table)
    print(combine_grade)
    draw_pic(combine_grade, name)
