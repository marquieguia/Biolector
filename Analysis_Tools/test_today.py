import matplotlib.pyplot as plt
import numpy as np
from palette import colors
import curveball
import os
font1 = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'bold',
        'size': 12,
        }
font2 = {'family': 'sans-serif',
        'weight': 'normal',
        'size': 18,
        }


t = np.array([0, 9, 12, 15, 18, 21, 24, 38])
sent = np.array([[0, 0, 0, 0, 0.1, 0, 0.1, 0], [0, 0.1, 0, 0.1, 0.1, 0.1, 0.1, 0.1], [0, 0, 0, 0, 0.2, 0.1, 0.1, 0.1]])

# FLUORESCENS OD
pf11 = np.array([[0, 0.2, 0.1, 0.2, 0.5, 1.1, 1.6, 1.3], [0, 0.1, 0.1, 0.1, 0.4, 1.2, 1.6, 1.2], [0, 0.2, 0.1, 0.1, 0.4, 1.1, 1.4, 1.1]])
pf12 = np.array([[0.1, 0.3, 0.3, 0.6, 1.7, 1.6, 1.3, 1.2], [0, 0.2, 0.4, 0.6, 1.4, 1.4, 1.3, 1.1], [0, 0.2, 0.2, 0.4, 1.3, 1.5, 1.2, 1.1]])
pf13 = np.array([[0, 0.1, 0, 0.1, 0.2, 0.3, 0.6, 1.1], [0, 0.2, 0.2, 0.2, 0.5, 1.1, 1.4, 1.1], [0, 0.2, 0.1, 0.2, 0.5, 0.9, 1.3, 1.1]])

pf81 = np.array([[0, 0.4, 0.8, 1, 1.6, 1.7, 1.5, 1.2], [0, 0.3, 0.8, 1.2, 1.5, 1.5, 1.3, 1.1], [0, 0.3, 0.8, 1.2, 1.5, 1.5, 1.3, 1.2]])
pf82 = np.array([[0, 0.3, 0.6, 0.9, 1.6, 1.6, 1.5, 1.1], [0.1, 0.2, 0.6, 1, 1.7, 1.6, 1.3, 1.1], [0, 0.3, 0.3, 0.9, 1.5, 1.5, 1.4, 1.1]])
pf83 = np.array([[0, 0.1, 0.3, 0.6, 1.4, 1.6, 1.5, 1.2], [0, 0.1, 0.3, 0.5, 1, 1.6, 1.4, 0.6], [0, 0.2, 0.2, 0.5, 1, 1.7, 1.5, 1.2]])

pfs = {'PF_1.1' : pf11, 'PF_1.2' : pf12, 'PF_1.3' : pf13,
       'PF_78.1' : pf81, 'PF_78.2' : pf82, 'PF_78.3' : pf83,
       'sent':sent}

col = ['red', 'blue', 'green', 'orange', 'yellow', 'black']
# PUTIDA OD
pp62 = np.array([[0, 0.1, 0.2, 0.3, 0.6, 1.2, 1.4, 1.2], [0, 0.1, 0.3, 0.5, 1, 1.3, 1.3, 1], [0.1, 0.1, 0.2, 0.2, 0.6, 1.3, 1.4, 1.1]])
pp63 = np.array([[0, 0.1, 0.1, 0.1, 0.3, 0.5, 1.1, 1.2], [0, 0.1, 0.2, 0.1, 0.3, 0.7, 1.2, 1.1], [0.1, 0.1, 0.2, 0.1, 0.3, 0.6, 1, 1.1]])
pp64 = np.array([[0, 0.1, 0.2, 0.5, 1.3, 1.3, 1.4, 1.1], [0, 0.1, 0.1, 0.3, 0.7, 1.1, 1.3, 1.1], [0.1, 0.2, 0.2, 0.3, 0.6, 1.3, 1.4, 0.9]])

pp31 = np.array([[0, 0.1, 0.1, 0.3, 0.6, 1.3, 1.4, 1.1], [0, 0.2, 0.2, 0.1, 0.4, 0.8, 1.2, 1], [0, 0.1, 0.2, 0.2, 0.7, 1.3, 1.5, 1.2]])
pp32 = np.array([[0.1, 0.1, 0.2, 0.2, 0.6, 1.3, 1.2, 1.1], [0, 0.1, 0.2, 0.1, 0.3, 0.7, 1.3, 1.1], [0.1, 0.1, 0.2, 0.3, 0.7, 1.3, 1.2, 1.1]])
pp33 = np.array([[0.1, 0.1, 0.1, 0.2, 0.4, 0.8, 1.3, 0.9], [0, 0.2, 0.2, 0.3, 0.7, 1.2, 1.3, 1], [0.1, 0.1, 0.2, 0.1, 0.4, 1.1, 1.1, 1.1]])

pps = {'PP_69.2' : pp62, 'PP_69.3' : pp63, 'PP_69.4' : pp64,
       'PP_73.1' : pp31, 'PP_73.2' : pp32, 'PP_73.3' : pp33,
       'sent':sent}

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(22, 12))
fit = np.polynomial.polynomial.Polynomial.fit

#pf_c = colors['green'] + ['black']
#pp_c = colors['orange'] + ['black']
strains = [pfs, pps]
for strain in strains:
    i ,j = 0 ,0
    for k, v in strain.items():
        avg = v.mean(axis=0)
        std = 0.5* v.std(axis=0)
        if k.startswith('PF'):

            #FOR INDIVIDUAL LINES
            # for i in range(0, 3):
            #     ax1.plot(t, v[i],  label=k, color=colors['green'][i], linewidth=4)

            #FOR AVERAGE LINES
            # print(len(avg))
            # print(k)
            #ax1.plot(t, avg,  label=k, color=colors['green'][i], linewidth=4)
            ax1.plot(t, avg,  label=k, color=colors['green'][i], linewidth=4)

            # # model = fit(t ,avg ,deg=4)
            # # coeff = model.convert().coef
            # # t_smooth = np.linspace(0, 32, num=64)
            # # pred_y = [coeff[4] * t ** 4 +coeff[3] * t ** 3 + coeff[2] * t ** 2 + coeff[1] * t + coeff[0] for t in t_smooth]
            # # ax1.plot(t_smooth ,pred_y ,color=colors['green'][i])
            ax1.errorbar(t ,avg, std, ls='none', marker='^', color='black', capsize=3, alpha=0.3)
            #
            # #ax1.fill_between(t ,avg-(0.5*std),avg+(0.5*std) ,alpha=0.2 ,color=colors['green'][i])
            i += 1
        elif k.startswith('PP'):

            #FOR INDIVIDUAL LINES
            # for i in range(0, 3):
            #     ax2.plot(t, v[i],  label=k, color=colors['orange'][i], linewidth=4)

            #FOR AVERAGED LINES
            #ax2.plot(t ,avg ,label=k ,color=colors['orange'][j] ,linewidth=4)
            ax2.plot(t ,avg ,label=k ,color=colors['orange'][j] ,linewidth=4)

            # model = fit(t ,avg ,deg=4)
            # coeff = model.convert().coef
            # t_smooth = np.linspace(0 ,32 ,num=64)
            # pred_y = [coeff[4] * t ** 4 + coeff[3] * t ** 3 + coeff[2] * t ** 2 + coeff[1] * t + coeff[0] for t in
            #           t_smooth]
            #ax2.plot(t_smooth ,pred_y ,color=colors['orange'][i])
            ax2.errorbar(t ,avg, std, ls='none', marker='^', color='black', capsize=3, alpha=0.3)
            j += 1

ax1.plot(t, sent.mean(axis=0), color='lightgrey', linewidth=4, label='sent')
#ax1.errorbar(t ,sent.mean(axis=0) ,sent.std(axis=0) ,ls='none' ,marker='^' ,color='black' ,capsize=3)
ax1.legend()
ax1.set_ylabel('OD',fontdict=font1)
ax1.set_xlabel('Time (h)',fontdict=font1)
ax1.set_xlim(-2, 40)
ax1.set_ylim(-0.1, 1.8)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_ylabel('OD600', fontdict=font2)
ax1.set_yticks([round(x, 1) for x in list(np.linspace(0, 1.5, 5))], fontsize=14)
ax1.set_xlabel('Time (h)' ,fontdict=font2)
ax1.set_xticks(list(range(0, 40, 5)), fontsize=20)


ax2.plot(t, sent.mean(axis=0), color='lightgrey', linewidth=4, label='sent')
#ax2.errorbar(t ,sent.mean(axis=0) ,sent.std(axis=0) ,ls='none' ,marker='^' ,color='black' ,capsize=3)
ax2.legend()
ax2.set_ylabel('OD',fontdict=font1)
ax2.set_xlabel('Time (h)',fontdict=font1)
ax2.set_xlim(-2, 40)
ax2.set_ylim(-0.1, 1.8)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_ylabel('OD600', fontdict=font2)
ax2.set_yticks([round(x, 1) for x in list(np.linspace(0, 1.5, 5))], fontsize=14)
ax2.set_xlabel('Time (h)' ,fontdict=font2)
ax2.set_xticks(list(range(0, 40, 5)), fontsize=20)

title = 'Processed Data Timecourses of SWB25 and KT2440'
fig.suptitle(title ,fontdict=font1)
outname = title + '.png'
out_path = os.path.join('..' ,'Timecourse_Figs' ,outname)
fig.savefig(out_path)

plt.show()
plt.close()
