import pandas as pd
import numpy as np
import matplotlib as plt

# reading the data
jee = pd.read_csv('JEEDemographics.csv')
state = pd.read_csv('StateInfo.csv')

dataframe = pd.DataFrame(jee, columns=['Origin','cpi','rank'])
matrix = dataframe.corr()