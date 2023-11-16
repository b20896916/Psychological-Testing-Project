import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

file = "cleaned_data.csv"
df = pd.read_csv(file)


try:
    os.mkdir("histograms")
except FileExistsError:
    pass

for i in df.columns[3:-1]:
    plt.ylim(0, 250)
    plt.hist(df[i], bins=[1,2,3,4,5,6], color='lightblue', align='left', edgecolor='black', linewidth=1.2)
    plt.title(f"item {i}")
    plt.savefig(f"histograms/hist_{i}png")
    plt.clf()
