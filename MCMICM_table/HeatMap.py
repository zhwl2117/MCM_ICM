import seaborn as sns

import matplotlib.pyplot as plt


def test(df):

    dfData = df.corr()

    plt.subplots(figsize=(9, 9)) # 设置画面大小

    sns.heatmap(dfData, annot=True, vmax=1, square=True, cmap="Blues")

    plt.show()

