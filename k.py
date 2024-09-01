import pandas as pd
import matplotlib.pyplot as plt
import numpy as np                                 #importing all important libraries
import random
import statistics


data = pd.read_csv('JEEDemographics.csv')         #reading the demographic file
 
#print(data.head())

# define 3 functions each of which returns a list of 50 top 3 fractions for each each way of selecting the k people
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

#define lists over which we will iterate the for loop
k_list = [10,20,50,100,200]
way_list = [firstKfromStart,firstKfromRand,randomk]

rep = 50  # no. of repetitions for each way of choosing k

xaxis = list(range(1,rep+1))         # defining the xaxis for scatter plot
i= 1



for way in way_list :
    for k in k_list :
        fig = way(k,rep)

        #print(way1)
        plt.scatter(xaxis,fig)
        plt.title(f'{i} with k={k}')
        plt.xlabel('Repition')
        plt.ylabel('Fraction of students from top3 states')
        plt.savefig(f'{i}_k={k}.jpeg',format = 'jpeg')
        plt.clf()
    i+=1

    





'''way3 = randomk(k,rep)
plt.scatter(xaxis,way3)
plt.show()
print(f"Expected value :  {np.sum(way3)/50}")
print(f"Standard deviation :  {statistics.stdev(way3)}")
'''
        
        
        
       



