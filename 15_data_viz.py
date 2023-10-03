#import library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks", color_codes=True)
ds = pd.read_csv("data_set/Affairs.csv")
# print(ds)
sns.countplot(x="children" , hue="age" , data=ds)
plt.show()