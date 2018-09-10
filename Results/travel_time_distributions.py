import numpy as np
from numpy import genfromtxt 
from scipy import stats
import matplotlib.pyplot as plt
from pylab import *

def binning( arr ):

 bins = 5
 frequency, edges, patches = hist(arr, bins)
 probden = []
 print frequency
 for i in range(len(frequency)-1):
  frequency[i+1] = frequency[i+1] + frequency[i]
 for i in range(len(frequency)):
  probden.append(frequency[i]/frequency[-1])
 #print probden
 #print edges
 return probeden, edges

filename = "1-6 ldb.csv"

my_data = genfromtxt(filename, delimiter=',')       # raw data according to link type

links = my_data[:,6]					
links = np.unique(links)							# set of links


# fits for 7-8

data7_8 = my_data[my_data[:,0] > 7]
data7_8 = data7_8[data7_8[:,0] < 8]

mean_jt = []
std_jt = []
shift_jt = []
mean_rt = []
std_rt = []
shift_rt = []
mean_st = []
std_st = []
shift_st = []

for i in links:
 data = data7_8[data7_8[:,6] == i]
 
 if (len(data) > 2):
 
  shap, loc, scale = stats.lognorm.fit(data[:,7])	   # fitting journey time
  scale = np.log(scale)
  mean_jt.append(scale)
  std_jt.append(shap)
  shift_jt.append(loc)
 
  shap, loc, scale = stats.lognorm.fit(data[:,8])     # fitting running time
  scale = np.log(scale)
  mean_rt.append(scale)
  std_rt.append(shap)
  shift_rt.append(loc)
 
  data_st_nz = data[data[:,12] != 0]					  # removing 0 stopped time values from data
  if (len(data_st_nz) > 2):
   shap, loc, scale = stats.lognorm.fit(data_st_nz[:,12])    # fitting stopped time
   scale = np.log(scale)
   mean_st.append(scale)
   std_st.append(shap)
   shift_st.append(loc)

#binning(mean_jt)
plt.hist(mean_jt)
plt.show()
print stats.kstest(mean_jt,'uniform')

plt.hist(std_jt)
plt.show()
print stats.kstest(std_jt,'uniform')

plt.hist(mean_rt)
plt.show()
print stats.kstest(mean_rt,'uniform')

plt.hist(std_rt)
plt.show()
print stats.kstest(std_rt,'uniform')

plt.hist(mean_st)
plt.show()
print stats.kstest(mean_st,'uniform')

plt.hist(std_st)
plt.show()
print stats.kstest(std_st,'uniform')

# fits for 8-9

data8_9 = my_data[my_data[:,0] > 8]
data8_9 = data8_9[data8_9[:,0] < 9]

mean_jt = []
std_jt = []
shift_jt = []
mean_rt = []
std_rt = []
shift_rt = []
mean_st = []
std_st = []
shift_st = []

for i in links:
 data = data8_9[data8_9[:,6] == i]
 
 if (len(data) > 2):
 
  shap, loc, scale = stats.lognorm.fit(data[:,7])	   # fitting journey time
  scale = np.log(scale)
  mean_jt.append(scale)
  std_jt.append(shap)
  shift_jt.append(loc)
 
  shap, loc, scale = stats.lognorm.fit(data[:,8])     # fitting running time
  scale = np.log(scale)
  mean_rt.append(scale)
  std_rt.append(shap)
  shift_rt.append(loc)
 
  data_st_nz = data[data[:,12] != 0]					  # removing 0 stopped time values from data
  if (len(data_st_nz) > 2):
   shap, loc, scale = stats.lognorm.fit(data_st_nz[:,12])    # fitting stopped time
   scale = np.log(scale)
   mean_st.append(scale)
   std_st.append(shap)
   shift_st.append(loc)

#binning(mean_jt)
plt.hist(mean_jt)
plt.show()
print stats.kstest(mean_jt,'uniform')

plt.hist(std_jt)
plt.show()
print stats.kstest(std_jt,'uniform')

plt.hist(mean_rt)
plt.show()
print stats.kstest(mean_rt,'uniform')

plt.hist(std_rt)
plt.show()
print stats.kstest(std_rt,'uniform')

plt.hist(mean_st)
plt.show()
print (stats.kstest(mean_st,'uniform'))

plt.hist(std_st)
plt.show()
print stats.kstest(std_st,'uniform')


# fits for 9-10

data9_10 = my_data[my_data[:,0] > 9]
data9_10 = data9_10[data9_10[:,0] < 10]

mean_jt = []
std_jt = []
shift_jt = []
mean_rt = []
std_rt = []
shift_rt = []
mean_st = []
std_st = []
shift_st = []

for i in links:
 data = data9_10[data9_10[:,6] == i]
 
 if (len(data) > 2):
 
  shap, loc, scale = stats.lognorm.fit(data[:,7])	   # fitting journey time
  scale = np.log(scale)
  mean_jt.append(scale)
  std_jt.append(shap)
  shift_jt.append(loc)
 
  shap, loc, scale = stats.lognorm.fit(data[:,8])     # fitting running time
  scale = np.log(scale)
  mean_rt.append(scale)
  std_rt.append(shap)
  shift_rt.append(loc)
 
  data_st_nz = data[data[:,12] != 0]					  # removing 0 stopped time values from data
  if (len(data_st_nz) > 2):
   shap, loc, scale = stats.lognorm.fit(data_st_nz[:,12])    # fitting stopped time
   scale = np.log(scale)
   mean_st.append(scale)
   std_st.append(shap)
   shift_st.append(loc)

#binning(mean_jt)
plt.hist(mean_jt)
plt.show()
print stats.kstest(mean_jt,'uniform')

plt.hist(std_jt)
plt.show()
print stats.kstest(std_jt,'uniform')

plt.hist(mean_rt)
plt.show()
print stats.kstest(mean_rt,'uniform')

plt.hist(std_rt)
plt.show()
print stats.kstest(std_rt,'uniform')

plt.hist(mean_st)
plt.show()
print stats.kstest(mean_st,'uniform')

plt.hist(std_st)
plt.show()
print stats.kstest(std_st,'uniform')


# fits for 10-11

data10_11 = my_data[my_data[:,0] > 10]
data10_11 = data10_11[data10_11[:,0] < 11]

mean_jt = []
std_jt = []
shift_jt = []
mean_rt = []
std_rt = []
shift_rt = []
mean_st = []
std_st = []
shift_st = []

for i in links:
 data = data10_11[data10_11[:,6] == i]
 
 if (len(data) > 2):
 
  shap, loc, scale = stats.lognorm.fit(data[:,7])	   # fitting journey time
  scale = np.log(scale)
  mean_jt.append(scale)
  std_jt.append(shap)
  shift_jt.append(loc)
 
  shap, loc, scale = stats.lognorm.fit(data[:,8])     # fitting running time
  scale = np.log(scale)
  mean_rt.append(scale)
  std_rt.append(shap)
  shift_rt.append(loc)
 
  data_st_nz = data[data[:,12] != 0]					  # removing 0 stopped time values from data
  if (len(data_st_nz) > 2):
   shap, loc, scale = stats.lognorm.fit(data_st_nz[:,12])    # fitting stopped time
   scale = np.log(scale)
   mean_st.append(scale)
   std_st.append(shap)
   shift_st.append(loc)

#binning(mean_jt)
plt.hist(mean_jt)
plt.show()
print stats.kstest(mean_jt,'uniform')

plt.hist(std_jt)
plt.show()
print stats.kstest(std_jt,'uniform')

plt.hist(mean_rt)
plt.show()
print stats.kstest(mean_rt,'uniform')

plt.hist(std_rt)
plt.show()
print stats.kstest(std_rt,'uniform')

plt.hist(mean_st)
plt.show()
print stats.kstest(mean_st,'uniform')

plt.hist(std_st)
plt.show()
print stats.kstest(std_st,'uniform')

'''
Questions:

1. What to do with links that do not have lane type?
2. Should I take the free flow speed of the link or of the lane type?
3. What to do for running time and stopped time?
4. The mean of running time is higher than the mean of journey time because of the shift. Is it okay?
5. Because of the shift, some of the means are negative. Is it okay?
6. Using shaprio test for normailty, distributions do not fit normal distributions, so discrete distribution should be used.
'''
