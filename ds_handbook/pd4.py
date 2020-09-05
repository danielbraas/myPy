# https://jakevdp.github.io/PythonDataScienceHandbook/03.04-missing-values.html

import pandas as pd
import numpy as np

vals1 = np.array([1, None, 3, 4])
vals1

for dtype in ['object', 'int']:
    print("dtype =", dtype)
    %timeit np.arange(1E6, dtype=dtype).sum()
    print()

vals2 = np.array([1, np.nan, 3, 4]) 
vals2.dtype

vals2.sum(), vals2.min(), vals2.max() # Will produce NaNs

np.nansum(vals2), np.nanmin(vals2), np.nanmax(vals2)

pd.Series([1, np.nan, 2, None])

x = pd.Series(range(2), dtype=int, index=['A','B'])
x

x.iloc[0] = None
x

data = pd.Series([1, np.nan, 'hello', None])
data.isnull()

data[data.notnull()]
data.dropna()

df = pd.DataFrame([[1,      np.nan, 2],
                   [2,      3,      5],
                   [None, 4,      6]],
                   columns=['A','B','C'])
df

df.dropna()
df.dropna(axis='columns')

df['D'] = np.nan
df.dropna(axis='columns', how='all')
df = df.drop(columns=3)

df.dropna(axis='rows', thresh=3)

df[1].loc[1] = np.nan
df.dropna(axis='rows', thresh=2)

data = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
data

data.fillna(0)

# forward-fill
data.fillna(method='ffill')

# back-fill
data.fillna(method='bfill')

df.fillna(method='ffill', axis=1)