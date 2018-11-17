import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns



FM86 = pd.read_csv("FM86.csv")


FM86.plot.scatter("Day_GC", "O2_mmol_hr")

plt.show()

