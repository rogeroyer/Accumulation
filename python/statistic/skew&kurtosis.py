
import pandas as pd
from scipy import stats

x = [41, 37, 33, 30.5, 44.2, 28.5, 34.5, 37.5, 39.5, 44.7, 40.5, 41.2, 36.5, 35.8]
s = pd.Series(x)
print(s.skew())
print(s.kurt())

n = len(x)
x_ = sum(x) / n
# print(x_)
f1, f2 = 0, 0
for index in x:
    f1 += (index - x_)**4
    f2 += (index - x_)**2

f = (f1 / n) / (f2 / n)**2 - 3
print(f)

kurt = stats.kurtosis(x)   # 偏度
skew = stats.skew(x)
print(skew)
print(kurt)
