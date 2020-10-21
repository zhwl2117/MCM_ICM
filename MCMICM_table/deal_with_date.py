import xlrd
import datetime


def deal_to_space(time):
    begin = 1
    begin_date = time[0]
    sp = []
    sp.append(begin)
    for date in time:
        delta = date - begin_date
        day = begin + delta.days
        sp.append(day)
    return sp


def deal_rating(rating):
    r_rating = []
    for r in rating:
        r_rating.append((float(r) - 1) / 8)
    return r_rating


def deal_date(time):
    date = []
    for t in time:
        t_str = t.replace("/", "-")
        d = datetime.datetime.strptime(t_str, '%m-%d-%Y')
        date.append(d)
    return date


def read_file(name):
    pat = r"C:\Users\17998\Desktop\MCM_ICN\hawkes_" + name + ".xls"
    excel = xlrd.open_workbook(pat)
    sheet = excel.sheet_by_index(0)
    rating = sheet.col_values(0)
    time = sheet.col_values(1)
    return rating, time


if __name__ == "__main__":
    rating, time = read_file("microwave")
    date = deal_date(time)
    date.reverse()
    r_rating = deal_rating(rating)
    sp = deal_to_space(date)
    print(r_rating)
    print(sp)