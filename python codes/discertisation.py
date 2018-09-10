
#from __future__ import print_function
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import math


file_name = "Draw1.csv"
fp = open(file_name,'wb')
duration = int(raw_input())																					# input duration of each time interval 		
mean_tt = np.genfromtxt('sampleinput1.csv',delimiter=',',dtype = None)										# input mean travel times for each time interval

def is_posdef(x):																							# function to check if covariance matrix is positive definite 
  return np.all(np.linalg.eigvals(x) > 0)
  
eps = 0.0001																								# minimum value of identity matrix
num_intervals = len(mean_tt[0]) - 2
dt = np.dtype([('st', np.str_, 16), ('en', np.str_, 16), ('intervals', np.float64, (num_intervals,))])
mean_tt1 = np.genfromtxt('sampleinput1.csv',delimiter=',',dtype = dt)
num_links = len(mean_tt)

cnt = 0
dic = {}																									# dictionary to store network information
for i in range(len(mean_tt1)):
  if (dic.get( mean_tt1[i]['st'] ) == None):
    dic[mean_tt1[i]['st']] = cnt + 1
    cnt = cnt + 1
  if (dic.get(mean_tt1[i]['en'])  == None):
    dic[mean_tt1[i]['en']] = cnt + 1
    cnt = cnt + 1
adj_lis = [[] for x in xrange(cnt+1)]
for i in range(len(mean_tt1)):
  adj_lis[dic[mean_tt1[i]['st']]].append(i)
cov_fil_name = 'covariance'
csv_extn = '.csv'
covariance = []
dep_cov = []
ind_cov = []
draw = []
num_draws = 5
dep_tt = []

for i in range(num_intervals):			# input covariance matrix and decomposition																														
  file_name = cov_fil_name + str(i) + csv_extn
  tmp_cov = np.genfromtxt(file_name,delimiter=',')
  covariance.append(tmp_cov)
  max_val = min(tmp_cov[x][x] for x in range(len(tmp_cov)))
  min_val = 0.0001
  while (max_val - min_val > eps):
    mid = (max_val + min_val)/2.0
    
    for x in range(num_links):
      tmp_cov[x][x] = tmp_cov[x][x] - mid
    if (is_posdef(tmp_cov)):
      min_val = mid
    else:
      max_val = mid
    for x in range(num_links):
      tmp_cov[x][x] = tmp_cov[x][x] + mid
  ind_cov.append(min_val)
  for x in range(num_links):
    tmp_cov[x][x] = tmp_cov[x][x] - min_val
  dep_cov.append(tmp_cov)
  mean = np.zeros(num_links)
  tmp_draws = np.random.multivariate_normal(mean,tmp_cov,num_draws)		# draws from monte carlo simulation
  draw.append(tmp_draws)
  _tmp = []
  for j in range(num_draws):
    gg = []
    for k in range(num_links):
      gg.append(int((mean_tt1[k]['intervals'][i] + tmp_draws[j][k])*10))
    _tmp.append(gg)
  dep_tt.append(_tmp)

split_tt = []															# splitting independent component
cdf = [0.166,0.5,0.833]
probability = [0.333,0.334,0.333]

for i in range(num_intervals):
  value = norm.ppf(cdf,loc = 0,scale = ind_cov[i])
  length_of_value = len(value)
  for j in range(length_of_value):
  	value[j] = int((value[j])*10)
  split_tt.append( value )

def dfs (cur,arr_time,prob,draw,fp):										# function to print output file
  with open(fp,'a') as outfile:
    idx = dic[cur]
    int_id = int(arr_time/(duration*10))
    if (int_id >= num_intervals):
      int_id = num_intervals - 1
    for j in adj_lis[idx]:
      ss = []
      string = str(mean_tt1[j]['st']) + ' ' + str(mean_tt1[j]['en']) + ' ' + str(int(arr_time)) + ' '
      for k in range(len(cdf)):
        string = string + str(int((dep_tt[int_id][i][j]) + (split_tt[int_id][k]) + (arr_time)) ) + '<>' + str(probability[k]) + ' '
      print >> outfile,string
      print string
      for k in range(len(cdf)):
        dfs(mean_tt1[j]['en'], (dep_tt[int_id][draw][j]) + (split_tt[int_id][k]) + (arr_time)  ,probability[k], i, fp) # dep_tt[i][j][k] ith interval, jth draw, kth link


for i in range(num_draws):												# printing output file
  file_name = "Draw" + str(i) + ".csv"
  with open(file_name,'a') as outfile:
    header = "tnode,hnode,ts,arrival<>probability"
    print >> outfile, header
  dfs(mean_tt1[0]['st'],0,1,i,file_name)


'''
  for j in adj_lis[1]:
    print mean_tt1[j]['st'],mean_tt1[j]['en'],0,
    for k in range(len(cdf)):
      print ' ',
      print dep_tt[0][i][j] + split_tt[0][k],probability[k],
    print ' '
    for k in range(len(cdf)):
      dfs(mean_tt1[j]['en'], dep_tt[0][i][j] + split_tt[0][k]  ,probability[k], i)
'''
 
''' 
1. Input length of each time interval, means for each time interval and co variance matrix for each time interval
2. Decomposte co variance matrix into dependent and independent matrices so that lambda is max and dependent matrix is invertible
3. Draw from muti variate normal distribution and set discretise the independent component

Questions 

4. How to discretise in log normal distribution

Arun??

1. How to discretise
'''

'''
Tasks to be done :
If the covariance matrix is for a log normal distribution - take exponential of the draws
Discretisation rule:
Length of discretisation interval should be less than lenght of time window 
'''
