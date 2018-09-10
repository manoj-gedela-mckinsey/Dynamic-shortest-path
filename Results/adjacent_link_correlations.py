import numpy as np
from numpy import genfromtxt 
from scipy import stats
import matplotlib.pyplot as plt
from pylab import *

filename = 'Network information.csv'
my_data = genfromtxt(filename, delimiter=',')

number_of_links = len(my_data)

tailnodes = my_data[:,0]					# set of tail nodes
headnodes = my_data[:,1]					# set of head nodes
linktype = my_data[:,5]

d_links = []								# downstream link
u_links = []								# upstream link
code = []									# type of downstream and upstream link


for i in range(number_of_links):			# finding adjacent links
 for j in range(number_of_links):
  if ( tailnodes[i] == headnodes[j] ):		# index j contains the upsteram link and index i contains the downstream link
   
   u_links.append( int(str(int(tailnodes[j])) + str(int(headnodes[j]))))
   d_links.append( int(str(int(tailnodes[i])) + str(int(headnodes[i]))))
   code.append( int(str(int(my_data[j][5])) + str(int(my_data[i][5]))))  
   
# creating a set of master data

type1_data = genfromtxt('1-6 ldb.csv', delimiter=',')
type2_data = genfromtxt('2-4 ldb.csv', delimiter=',')
type3_data = genfromtxt('3-4 ludu.csv', delimiter=',')
type4_data = genfromtxt('4-5 ludu.csv', delimiter=',')
type5_data = genfromtxt('5-2 ludb.csv', delimiter=',')

masterdata = np.vstack((type1_data, type2_data))
masterdata = np.vstack((masterdata, type3_data))
masterdata = np.vstack((masterdata, type4_data))
masterdata = np.vstack((masterdata, type5_data))

# finding correlations from 7-8 am

data7_8 = masterdata[masterdata[:,0] < 8]
data7_8 = data7_8[data7_8[:,0] > 7]
final_code = []              				# type of upstream and downstream link
correlations = []							# final list of correlations

for i in range(len(u_links)):
 u_link = data7_8[data7_8[:,6] == u_links[i]]
 d_link = data7_8[data7_8[:,6] == d_links[i]]
 
 max_length = min(len(u_link),len(d_link))
 
 if (max_length > 2):
  np.random.shuffle(u_link)
  np.random.shuffle(d_link)
  correlations.append(np.corrcoef(u_link[0:max_length,7],d_link[0:max_length,7])[0][1])
  final_code.append(code[i])

correlations = np.array(correlations)
final_code = np.array(final_code)

#for i in [11,12,13,14,15,21,22,23,24,25,31,32,33,34,35,41,42,43,44,45,51,52,53,54,55]:
for i in [22,25,55]: 
 vector = []								# vector contanining correlations of similar type
 for j in range(len(final_code)):
  if ( final_code[j] == i ):
   vector.append(correlations[j])
 mean, std = stats.norm.fit(vector)
 if (len(vector) > 2):
  print i, len(vector), 'mean = ', mean, 'std = ', std
  #print stats.shapiro(vector)
  plt.hist(vector)
  plt.xlabel('Correlation')
  plt.ylabel('Frequency')
  plt.show()
 elif (0<len(vector)<3):
  print i, len(vector),'mean = ', mean, 'std = ', std 
  
'''
1. Is binning okay in case of correlations between adjacent links also?
2. Road length need not be taken because they will cancel out when correlations are calculated.
3. What about links that do not have link type defined?
4. Except for 1 type. Everything else is normal distribution. Is it okay to assume normal distributions for all?
'''
