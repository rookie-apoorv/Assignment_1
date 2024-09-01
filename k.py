import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import statistics
data = pd.read_csv('JEEDemographics.csv')

#print(data.head())

def firstKfromStart(k,rep) :
    frac = []
    top33 = pd.DataFrame()
    for i in range(rep) :
        firstkrows = data.head(k)
        state_count = firstkrows['Origin'].value_counts()
        #print(state_count)
        state_count_df = state_count.reset_index()
        state_count_df.columns = ['origin','count']
        top3 = state_count_df.head(3)
        top33 = state_count_df
        fractop3 = (top3['count'].sum())/k
        frac.append(fractop3)
    top33.to_excel('Top3.xlsx')
    return frac

k = 1000
rep = 50
xaxis = list(range(1,51))

way1 = firstKfromStart(k,rep)
'''
#print(way1)
plt.scatter(xaxis,way1)
plt.show()
'''
def firstKfromRand(k,rep) :
    frac = []
    data_to_append  = pd.read_csv('JEEDemographics.csv')
    data_combined = pd.concat([data,data_to_append],ignore_index = True)
    for i in range(rep) :
        start = random.randint(1,1500)
        krowfromrand = data_combined[start : start+k]
        state_count = krowfromrand['Origin'].value_counts()
        state_count_df = state_count.reset_index()
        state_count_df.columns = ['Origin','Count']
        top3 = state_count_df.head(3)
        fractop3 = (top3['Count'].sum())/k
        frac.append(fractop3)
    return frac
'''
way2 = firstKfromRand(k,rep)
plt.scatter(xaxis,way2)
plt.show()
'''
def randomk(k,rep) :
    frac = []
    for i in range(rep) :
        new_data = data.sample(n=k)
        state_count = new_data['Origin'].value_counts()
        state_count_df = state_count.reset_index()
        state_count_df.columns = ['Origin','Count']

        top3 = state_count_df.head(3)
       
        fractop3 = (top3['Count'].sum())/k
        frac.append(fractop3)
    return frac


way3 = randomk(k,rep)
plt.scatter(xaxis,way3)
plt.show()
print(f"Expected value :  {np.sum(way3)/50}")
print(f"Standard deviation :  {statistics.stdev(way3)}")