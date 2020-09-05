import numpy as np
import pandas as pd

area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
data
data['area']

data.area is data['area']

data['density'] = data['pop'] / data['area']
data

data.values

data.T

df = pd.DataFrame(range(1, 5)) # How can I supply an index after I created the dataframe?

# This is coming from the Pandas Doc website: https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html

titanic = pd.read_csv('data/titanic.csv')
titanic.dtypes # Corresponds to sapply(titanic, class)

titanic.to_excel('data/titanic.xlsx', sheet_name='passengers', index=False)

titanic.info()

titanic['Age']