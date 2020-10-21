from HeatMap import test
import xlrd
import pandas as pd


def read_target(name):
    excel = xlrd.open_workbook(name)
    sheet = excel.sheet_by_name("Sheet1")
    avg_star = sheet.col_values(1)
    avg_review = sheet.col_values(2)
    return pd.DataFrame({"avg_star": avg_star, "avg_review": avg_review})


if __name__ == "__main__":
    df = read_target(r"C:\Users\17998\Desktop\MCM_ICN\top_10_microwave.xlsx")
    print(df)
    test(df)
