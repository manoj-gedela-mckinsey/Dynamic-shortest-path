import numpy as np
from numpy import genfromtxt 
from scipy import stats
import matplotlib.pyplot as plt
from pylab import *

filename = '4-5 ludu.csv'
my_data = genfromtxt(filename, delimiter=',')

setof_links = my_data[:,6]
setof_links = np.unique(setof_links)					

vector = []

for i in setof_links:                                    
 data = my_data[my_data[:,6] == i]
 data = data[data[:,0] < 11]
 data = data[data[:,0] > 10]
  
 if (len(data) > 2) :
  vector.append(np.corrcoef(data[:,8],data[:,12])[0][1])

print (vector), len(vector)

vector = np.array(vector)
mask = np.isnan(vector)
vector[mask] = np.interp(np.flatnonzero(mask), np.flatnonzero(~mask), vector[~mask])
print (vector), len(vector)

plt.hist(vector)
plt.title("6ldb")
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

print (stats.shapiro(vector))
mu, std = stats.norm.fit(vector)
print (mu,std)




# fraction of values where stopped time = 0
'''
# 7-8
data7_8 = my_data[my_data[:,0] < 8]
data7_8 = data7_8[data7_8[:,0] > 7]

data7_8_0 = data7_8[data7_8[:,12] == 0]
print '7-8  ', float((len(data7_8_0)))/float((len(data7_8))) 

# 8-9
data8_9 = my_data[my_data[:,0] < 9]
data8_9 = data8_9[data8_9[:,0] > 8]

data8_9_0 = data8_9[data8_9[:,12] == 0]
print '8-9  ', float((len(data8_9_0)))/float((len(data8_9))) 

# 9-10
data9_10 = my_data[my_data[:,0] < 10]
data9_10 = data9_10[data9_10[:,0] > 9]

data9_10_0 = data9_10[data9_10[:,12] == 0]
print '9-10  ', float((len(data9_10_0)))/float((len(data9_10))) 

# 10-11
data10_11 = my_data[my_data[:,0] < 11]
data10_11 = data10_11[data10_11[:,0] > 10]

data10_11_0 = data10_11[data10_11[:,12] == 0]
print '10-11  ', float((len(data10_11_0)))/float((len(data10_11))) 
'''

'''
1. Using Shapiro test, the correlations follow a normal distribution, so can a normal distributin be used?
'''
 
