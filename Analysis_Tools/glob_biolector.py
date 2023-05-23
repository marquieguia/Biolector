import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import os
from palette import colors as c
import curveball
from tempfile import NamedTemporaryFile
import matplotlib.font_manager as fm

###################TO CHANGE FONT TO MATCH BIORENDER POSTER####################

roboto_med = open(os.path.join('..','Fonts', 'Roboto', 'Roboto-Medium.ttf'), 'rb')
f1 = NamedTemporaryFile(delete=False, suffix='.ttf')
f1.write(roboto_med.read())
f1.close()

roboto_light = open(os.path.join('..','Fonts', 'Roboto', 'Roboto-Light.ttf'), 'rb')
f2 = NamedTemporaryFile(delete=False, suffix='.ttf')
f2.write(roboto_light.read())
f2.close()

font1 = fm.FontProperties(fname=f1.name,size=22)
font2 = fm.FontProperties(fname=f1.name,size=16)
#######################################

input_fname_giac = 'giacomo_final_may23.xlsx'
input_fname_ale = 'biolector_march23.xlsx'

wells_dic_giacomo = {'KT pMAT-KAB (transf)': ['D04' ,'D05' ,'D06', 'D07' ,'D08' ,'E01'] ,
                     'KT2440 pMATING-tphKAB':['E05','E06','E07', 'E08','F01','F02'],
                     'SWB25 pMATING-tphKAB':['F03','F04','F05','F06','F07','F08'],
                    }
wells_dic_ale =  {'SWB25 pQBR57-tphKAB':['A03','B03','C03','D03','E03','F03'],
                  'KT2440 pQBR57-tphKAB':['A04','B04','C04','D04','E04','F04'],
                  'SWB25 WT': ['A05' ,'B05' ,'C05' ,'D05' ,'E05' ,'F05'],
                  'KT2440 WT': ['A06' ,'B06' ,'C06' ,'D06' ,'E06' ,'F06'] ,
                  }


greens = ['limegreen', 'forestgreen']
reds = ['lightcoral', 'coral']
brown = '#9E6D30'
figs_params = {'fig1':
                   {'title': 'Donors SWB25 grown on M9 + 10 mM TPA' ,'ylims': (0.05 ,1) ,'xlims': (0 ,100),
                    'strains_plotted':{'SWB25 pMATING-tphKAB': reds[0], 'SWB25 WT':'lightgrey', 'SWB25 pQBR57-tphKAB':reds[1]}},
               'fig2':
                   {'title': 'Transconjugants KT2440 grown on M9 + 10 mM TPA' ,'ylims': (0.05 ,1) ,'xlims': (0 ,100) ,
                    'strains_plotted':{'KT2440 pMATING-tphKAB': greens[0], 'KT2440 WT':'lightgrey', 'KT2440 pQBR57-tphKAB':greens[1]}}}
#
# wells_dic = {'PFs_precond':['A01','B01','C01','D01','E01','F01'],
#              'PPs_precond':['A02','B02','C02','D02','E02','F02'],
#              'PFs_nocond':['A03','B03','C03','D03','E03','F03'],
#              'PPs_nocond':['A04','B04','C04','D04','E04','F04'],
#              'PFs_wt': ['A05' ,'B05' ,'C05' ,'D05' ,'E05' ,'F05'] ,
#              'PPs_wt': ['A06' ,'B06' ,'C06' ,'D06' ,'E06' ,'F06'] ,
#              'P20_PCA': ['A07' ,'B07' ,'C07'],
#              'P20_PCA_TPA': ['A08' ,'B08' ,'C08'],
#              'P20_1KB': ['D07' ,'E07' ,'F07'] ,
#              'P20_1KB_TPA': ['D08' ,'E08' ,'F08']
#              }
#
# figs_params = {'fig1': {'title': 'P. putida +- pQ-KAB' ,'ylims': (0.05 ,1) ,'xlims': (0 ,100) ,
#                         'strains_plotted': {'PPs_nocond': c['orange'], 'PPs_wt':c['grey']}},
#                'fig2': {'title': 'Adapted P. putida +- pQ-KAB' ,'ylims': (0.05 ,1) , 'xlims': (0 ,100) ,
#                         'strains_plotted': {'PPs_precond': c['red'] ,'PPs_wt': c['grey']}} ,
#                'fig3': {'title': 'P. fluorescens +- pQ-KAB' ,'ylims': (0.05 ,1) ,'xlims': (0 ,100) ,
#                         'strains_plotted': {'PFs_nocond': c['cyan'], 'PFs_wt':c['grey']}},
#                'fig4': {'title': 'Adapted P. fluorescens +- pQ-KAB' ,'ylims': (0.05 ,1) , 'xlims': (0 ,100) ,
#                         'strains_plotted': {'PFs_precond': c['green'] ,'PFs_wt': c['grey']}} ,
#                }


# figs_params = {'fig1': {'title': 'Preconditioning of P. putida pQ-KAB' ,'ylims': (0.05 ,1) ,'xlims': (0 ,100) ,
#                         'strains_plotted': {'PPs_precond': c['red'] ,'PFs_nocond': c['orange']}},
#                'fig2': {'title': 'Preconditioning of  P. fluorescens pQ-KAB' ,'ylims': (0.05 ,1) , 'xlims': (0 ,100) ,
#                         'strains_plotted': {'PFs_precond': c['green'] ,'PFs_nocond': c['cyan']}} ,
#                'fig3': {'title': 'Growth on 10 mM PCA +- 10 mM TPA, P. putida pQ-KAB (P20)' ,'ylims': (0.05 ,1) , 'xlims': (0 ,100) ,
#                         'strains_plotted': {'P20_PCA': c['grey'] ,'P20_PCA_TPA': c['red']}} ,
#                'fig4': {'title': 'Growth on 1% KB +- 10 mM TPA, P. putida pQ-KAB (P20)' ,'ylims': (0.05 ,1) ,'xlims': (0 ,100) ,
#                         'strains_plotted': {'P20_1KB': c['grey'] ,'P20_1KB_TPA': c['orange']}} ,
#                }
input_path_giac = os.path.join('..', 'DATA', 'Biolector', input_fname_giac)
input_path_ale = os.path.join('..', 'DATA', 'Biolector', input_fname_ale)
df_giac = pd.read_excel(input_path_giac, sheet_name='raw_data', usecols='A:GN',
                   header=24, nrows=48)
df_giac = df_giac.set_index(['Unnamed: 0']).drop(['Unnamed: 1','Unnamed: 2','TIME [h] ->'], axis=1).T

t = np.array(df_giac.index, dtype=np.float64)

df_ale = pd.read_excel(input_path_ale, sheet_name='raw_data', usecols='A:GN',
                   header=24, nrows=48)
df_ale = df_ale.set_index(['Unnamed: 0']).drop(['Unnamed: 1','Unnamed: 2','TIME [h] ->'], axis=1).T

t_ale = np.array(df_ale.index, dtype=np.float64)
print(t_ale.shape)





markers = [ "v", ".", "o", "p"]

for k, v in figs_params.items():

    fig, ax = plt.subplots(figsize=(12, 8))

    title = v['title']

    strains_and_color = v['strains_plotted']

    count = 0

    for strain, color in strains_and_color.items():

        if strain in wells_dic_giacomo.keys():

            wells = wells_dic_giacomo[strain]

            data = np.array([df_giac[well] for well in wells])

            df_ovr = pd.DataFrame()

            for i in range(0, data.shape[0]):

                zeroed = data[i] - min(data[i])

                df_ovr[str(i)] = zeroed


            avg = df_ovr.mean(axis=1)
            std = df_ovr.std(axis=1)

            ax.scatter(t[:178] ,avg, color=color, marker=markers[count], label=strain)
            count += 1
            ax.errorbar(t[:178] ,avg, std, ls='none', marker='^', color=color, capsize=3, alpha=0.3)







        elif strain in wells_dic_ale.keys():


            wells = wells_dic_ale[strain]

            data = np.array([df_ale[well] for well in wells])

            df_ovr = pd.DataFrame()

            for i in range(0, data.shape[0]):

                zeroed = data[i] - min(data[i])

                df_ovr[str(i)] = zeroed


            avg = df_ovr.mean(axis=1)
            std = df_ovr.std(axis=1)

            ax.scatter(t_ale ,avg, color=color, marker=markers[count], label=strain)
            count += 1
            ax.errorbar(t_ale,avg, std, ls='none', marker='^', color=color, capsize=3, alpha=0.3)




        # for well in wells:
        #     data = df[well]
        #     zeroed = data - min(data)
        #     ovr += zeroed
        #     label = strain + str(count)
        # ax.scatter(t ,ovr/denom, color=color[count], marker=markers[count], label=label)
        #
        # count += 1

    plt.minorticks_on()
    ax.legend(prop=font2)
    ax.spines[['right' ,'top']].set_visible(False)
    ax.grid(True)
    ax.set_title(title ,fontproperties=font1)
    ax.set_ylabel('OD Gain 20', fontproperties=font2)
    plt.yticks(fontsize=14, fontproperties=font2)

    ax.set_xlabel('Time (h)', fontproperties=font2)
    plt.xticks(fontsize=14, fontproperties=font2)
    fig_name = title + '.png'
    out_path = os.path.join('..', 'Biolector_Figs', fig_name)
    fig.savefig(out_path)
    plt.show()
    plt.close()


# # CONTROL DATA
# input_path = os.path.join('..', 'DATA', 'Biolector', 'Dec22.xlsx')
# c_df = pd.read_excel(input_path, sheet_name='raw_data', usecols='A:GV',
#                    header=24, nrows=48)
# c_df = c_df.set_index(['Unnamed: 0']).drop(['Unnamed: 1','Unnamed: 2','TIME [h] ->'], axis=1).T
# c_t = np.array(df.index, dtype=np.float64)
# blank = c_df[['D06', 'E06', 'F06']].mean(axis=1)
# print(blank)

# # CURVEBALL, it works
# arr = df['A01'].to_numpy(dtype=np.float64)
# arr_blank = blank.to_numpy(dtype=np.float64)
# print(arr_blank)
# arr -= arr_blank
# arr = (arr - min(arr)) / max(arr)
#
# data = {'Time':t, 'OD':arr}
# curve_df = pd.DataFrame.from_dict(data)
# print(curve_df)
#
# models ,fig ,ax = curveball.models.fit_model(curve_df,PLOT=True ,PRINT=False)
#
# plt.show()
