# The code was taken from Python Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/02.06-boolean-arrays-and-masks.html\

import numpy as np
import pandas as pd

# use pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv('ds_handbook/data/Seattle2014.csv')['PRCP'].values
inches = rainfall / 254.0  # 1/10mm -> inches
inches.shape

rainfall = pd.read_csv('C:/Users/Daniel/Dropbox/Py_projects/myPy/ds_handbook/data/Seattle2014.csv')
pwd
rainfall.head
