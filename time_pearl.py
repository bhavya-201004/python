import numpy as np
%timeit [i**4 for i in range(1,11)]
%timeit np.arange(1,11)**4