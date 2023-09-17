import pandas as pd
import numpy as np
from entendendo_series_pandas import serie_1, serie_2, serie_3

# UFuncs
print("\n", np.amin(serie_1), np.amax(serie_1), sep="\n")
print("\n", np.ptp(serie_1))
print("\n", np.percentile(serie_1, 25))
print("\n", np.mean(serie_1))
print("\n", np.median(serie_1))
print("\n", np.std(serie_1))
print("\n", np.var(serie_1))
print("\n", np.average(serie_1))

print(np.info(np.amin))