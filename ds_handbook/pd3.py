import pandas as pd
import numpy as np
rng = np.random.RandomState(42)
ser = pd.Series(rng.randint(0, 10, 4))
ser
df = pd.DataFrame(rng.randint(0, 10, (3, 4)),
                  columns=['A', 'B', 'C', 'D'])
df

np.exp(df)
area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                  'California': 423967}, name='area')
population = pd.Series({'California': 38332521, 'Texas': 26448193,
                        'New York': 19651127}, name='population')
population / area

area.index | population.index

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
A, B, A + B

A.add(B, fill_value=0)


A = pd.DataFrame(rng.randint(0, 20, (2, 2)),
                 columns=list('AB'))
A


B = pd.DataFrame(rng.randint(0, 10, (3, 3)),
                 columns=list('BAC'))
B

A + B
fill = A.stack().mean()
A.add(B, fill_value=fill)
A.stack()


A = rng.randint(10, size=(3, 4))
A

A - A[0]
A[0]
df = pd.DataFrame(A, columns=list('QRST'))
df - df.iloc[0]

df.subtract(df['R'], axis=0)
halfrow = df.iloc[0, ::2]
halfrow
