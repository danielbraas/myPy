# This is taken from: https://jakevdp.github.io/PythonDataScienceHandbook/03.05-hierarchical-indexing.html

import numpy as np
import pandas as pd

index = [('California', 2000), ('California', 2010),
         ('New York', 2000), ('New York', 2010),
         ('Texas', 2000), ('Texas', 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
pop = pd.Series(populations, index=index)
pop

index = pd.MultiIndex.from_tuples(index)
index

pop = pop.reindex(index)
pop

pop[:, 2010]
type(pop)

pop_df = pop.unstack()
pop_df
pop_df.stack()

pop_df = pd.DataFrame({'total': pop,
                       'under18': [9267089, 9284094,
                                   4687374, 4318033,
                                   5906301, 6879014]})
pop_df

f_u18 = pop_df['under18'] / pop_df['total']
f_u18.unstack()

df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])
df

data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102}
pd.Series(data).unstack()

pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])

pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])

pd.MultiIndex.from_product([['a', 'b'], [1, 2]])

pd.MultiIndex(levels=[['a', 'b'], [1, 2]],
              labels=[[0, 0, 1, 1], [0, 1, 0, 1]]) # Does not work for some reason

pop.index.names = ['state', 'year']
pop

# hierarchical indices and columns
index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                   names=['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names=['subject', 'type'])

# mock some data
data = np.round(np.random.randn(4, 6), 1)
data[:, ::2] *= 10
data += 37

# create the DataFrame
health_data = pd.DataFrame(data, index=index, columns=columns)
health_data

health_data['Guido']

pop['California', 2010]
pop['California', ]

pop.loc['California':'New York']
pop.loc['California':'New York', 2000]
pop[pop > 22000000]

pop[['California', 'Texas']]

health_data['Guido', 'HR']

health_data.iloc[:2, :2]

health_data.loc[:, ('Bob', 'HR')]

index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]]) # Index is not sorted
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
data

data = data.sort_index()
data

pop.unstack(level=0)
pop.unstack(level=1)

pop_flat = pop.reset_index(name='population')
pop_flat

pop_flat.set_index(['state', 'year'])

pop_flat['bla']=[1,2,1,2,1,2]
pop_flat.set_index(['state','year','bla'])
pop_flat.set_index(['state','year','bla']).unstack(level=2)

data_mean = health_data.mean(level='year')
data_mean

data_mean.mean(axis=1, level='type')