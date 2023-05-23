import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import curveball
import os
font1 = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'bold',
        'size': 12,
        }



#### Fluorescens #######
title = '#78_timecourse'
t = np.array([0, 8.5, 10.5, 12.5, 14.5, 18, 30])
pf81_od = np.array([0.05, 0.36, 0.60, 0.77, 1.08, 1.42, 1.29])
pf82_od = np.array([0.06, 0.23, 0.39, 0.71, 0.86, 1.50, 1.37])
pf83_od = np.array([0.06, 0.33, 0.59, 0.88, 1.15, 1.47, 1.40])
pfs_od = np.array([pf81_od, pf82_od, pf83_od])

pf81_mM = np.array([16.12, 8.58, 6.10, 1.63, 0.39, 0, 0])
pf82_mM = np.array([16.12, 7.51, 7.54, 5.14, 1.37, 0, 0])
pf83_mM = np.array([16.12, 7.57, 6.97, 1.37, 0.75, 0, 0])
pfs_mM = np.array([pf81_mM, pf82_mM, pf83_mM])

pf_avg_od = pfs_od.mean(axis=0)
pf_std_od = pfs_od.std(axis=0)

pf_avg_mM = pfs_mM.mean(axis=0)
pf_std_mM = pfs_mM.std(axis=0)



fig, ax1 = plt.subplots()

ax1.scatter(t, pf_avg_od, color='forestgreen')
ax1.set_ylabel('OD',fontdict=font1)
plt.fill_between(t ,pf_avg_od- (0.5*pf_std_od),pf_avg_od+(0.5*pf_std_od) ,alpha=0.4 ,color='green')

ax2 = ax1.twinx()
ax2.scatter(t, pf_avg_mM, color='blue')
ax2.set_ylabel('TPA (mM)',fontdict=font1)
plt.fill_between(t,pf_avg_mM-(0.5*pf_std_mM),pf_avg_mM+(0.5*pf_std_mM) ,alpha=0.4 ,color='blue')

ax1.spines[['top']].set_visible(False)
ax2.spines[['top']].set_visible(False)
fig.legend(labels=('OD', 'TPA'))
# plt.ylim(0, 1.5)
# plt.xlim(0, 31)
ax1.set_xlabel('Time (h)' ,fontdict=font1)
plt.title(title, fontdict=font1)
plt.show()
plt.close()
outname = title + '.png'
out_path = os.path.join('..' ,'Timecourse_Figs' ,outname)
fig.savefig(out_path)

#### Putida #######
title = '#73_timecourse'
pp31_od = np.array([0.04, 0.28, 0.37, 0.68, 1.02, 1.35, 1.19])
pp32_od = np.array([0.04, 0.46, 0.57, 0.98, 1.32, 1.26, 1.15])
pp33_od = np.array([0.04, 0.35, 0.60, 1.30, 1.30, 1.25, 1.15])
pps_od = np.array([pp31_od, pp32_od, pp33_od])

pp31_mM = np.array([12.65, 7.05, 7.88, 5.80, 5.89, 0, 0])
pp32_mM = np.array([12.65, 7.93, 1.35, 0.23, 0, 0, 0])
pp33_mM = np.array([12.65, 6.55, 0.97, 0.24, 0, 0, 0])
pps_mM = np.array([pp31_mM, pp32_mM, pp33_mM])

pp_avg_od = pps_od.mean(axis=0)
pp_std_od = pps_od.std(axis=0)

pp_avg_mM = pps_mM.mean(axis=0)
pp_std_mM = pps_mM.std(axis=0)

fig, ax1 = plt.subplots()

ax1.scatter(t, pp_avg_od, color='forestgreen')
ax1.set_ylabel('OD',fontdict=font1)
plt.fill_between(t ,pp_avg_od- (0.5*pp_std_od),pp_avg_od+(0.5*pp_std_od) ,alpha=0.4 ,color='green')

ax2 = ax1.twinx()
ax2.scatter(t, pp_avg_mM, color='blue')
ax2.set_ylabel('TPA (mM)',fontdict=font1)
plt.fill_between(t ,pp_avg_mM-(0.5*pp_std_mM),pp_avg_mM+(0.5*pp_std_mM) ,alpha=0.4 ,color='blue')

ax1.spines[['top']].set_visible(False)
ax2.spines[['top']].set_visible(False)
fig.legend(labels=('OD', 'TPA'))
# plt.ylim(0, 1.5)
# plt.xlim(0, 31)
ax1.set_xlabel('Time (h)' ,fontdict=font1)
plt.title(title, fontdict=font1)
plt.show()
plt.close()
outname = title + '.png'
out_path = os.path.join('..' ,'Timecourse_Figs' ,outname)
fig.savefig(out_path)
