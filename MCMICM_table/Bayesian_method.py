import math


def cal_grade(rating, z=1.65):
    N = len(rating)
    K = 5
    s = [1, 2, 3, 4, 5]
    rating_dis = [0, 0, 0, 0, 0]
    for n in rating:
        rating_dis[n-1] += 1
    sum1 = 0
    for k in range(K):
        sum1 += s[k] * (rating_dis[k] + 1) / (N + K)
    sum2 = 0
    for k in range(K):
        sum2 += (s[k] ^ 2) * (rating_dis[k] + 1) / (N + K)
    sum3 = sum1 * sum1
    interval = 2 * z * math.sqrt(abs(sum2 - sum3) / (N + K + 1))
    print(interval)
    S = sum1 - interval / 2
    print(S)
    return S
