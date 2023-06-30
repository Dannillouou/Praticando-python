import pandas as pd
import matplotlib.pyplot as plt

# import os
# os.chdir("usando_pandas")

mtcars = pd.read_csv("mtcars.csv")

mtcars.plot.scatter(x = "mpg", y = "cyl")

plt.show()