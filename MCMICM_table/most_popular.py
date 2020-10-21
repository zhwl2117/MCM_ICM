import xlrd


def read_excel(name):
    pat = r"C:\Users\17998\Desktop\MCM_ICN" + "\\" + name + ".xlsx"
    excel = xlrd.open_workbook(pat)
    sheet = excel.sheet_by_name(name)
    product_names = sheet.col_values(3)[1:]
    names_set = set(product_names)
    names_dict = {}
    for name in names_set:
        names_dict[name] = product_names.count(name)
    return names_dict


def get_10_most_popular(product_dict):
    h = sorted(product_dict.items(), key=lambda x: x[1], reverse=True)
    return h[:10]


if __name__ == "__main__":
    hair_dryer = read_excel("pacifier")
    h = get_10_most_popular(hair_dryer)
    print(h)