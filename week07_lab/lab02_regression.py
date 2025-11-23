# This code analysis the tips dataset for regressions analysis
# Lab 7.02
# Author: Orla Woods

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
dataset =  sns.load_dataset("tips")

# print(dataset.head())

''' 
# regression plot for total bill vs tip
sns.set_style('whitegrid')
sns.lmplot(x='total_bill', y='tip',order=4, data=dataset)
plt.title('Regression Plot: Total Bill vs Tip')
plt.show()
'''

# regression plot for size vs tip
sns.lmplot(x='size', y='tip', data=dataset)

# put in a jitter to make it easier to see
sns.lmplot(x='size', y='tip', data=dataset, x_jitter=0.05)

# use estimator to estimate the mean tip for each size
sns.lmplot(x='size', y='tip', data=dataset, x_estimator=np.mean)
plt.title('Regression Plot: Size vs Tip')
plt.show()
