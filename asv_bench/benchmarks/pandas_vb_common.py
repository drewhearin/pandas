from pandas import *
import pandas as pd
from datetime import timedelta
from numpy.random import randn
from numpy.random import randint
from numpy.random import permutation
import pandas.util.testing as tm
import random
import numpy as np
import threading
from importlib import import_module

try:
    from pandas.compat import range
except ImportError:
    pass

np.random.seed(1234)

# try em until it works!
for imp in ['pandas_tseries', 'pandas.lib', 'pandas._libs.lib']:
    try:
        lib = import_module(imp)
        break
    except:
        pass

# didn't add to namespace until later
try:
    from pandas.core.index import MultiIndex
except ImportError:
    pass
