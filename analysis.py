import pandas as pd
import numpy as np

drinks = pd.read_csv('./data/drinks_dataset.csv')
asia = drinks.loc[drinks['continent'] == 'Asia']
print(asia.head())


print(f"Spirit are best correlation with beer consumption: 0.694\n The correlation of wine with beer consumption is: 0.437.\n As we can see below:")
print(asia.corr())

north_america = drinks.loc[drinks['continent'] == 'North America']
print(north_america.head())

print(north_america.corr())
print(f'It is not the same in North America. The wine are best: 0.40\n The correltion of spirit with beer is -0.073')
