from ClarioStar_extractor import extractor
import numpy as np
import matplotlib.pyplot as plt
from palette import colors as c
import os

ft = 24
# '-ve_KB':['A8' ,'B8' ,'C8', 'D8' ,'E8' ,'F8']},
# figs_params = {
#                 #Putida, adapted to KB
#                 'fig1': {'title': 'Media KB, adapted KB SWB25' ,'ylims': (0.05 ,2.8) ,'xlims': (0 ,ft) ,
#                         'strains_data': {'KB_PF+K_1': ['A7' ,'B7'], 'KB_PF+K_2': ['A8' ,'B8', 'H2'],
#                                          'KB_PF+K_3': ['A9' ,'B9'] ,'sent':['G1', 'G2', 'G3']},
#                         'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
#                                           'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}},
#                'fig2':  {'title': 'Media M9 + TPA, adapted KB SWB25' ,'ylims': (0.05 ,1.5) ,'xlims': (0 ,ft) ,
#                         'strains_data': {'KB_PF+K_1': ['C7' ,'D7'], 'KB_PF+K_2': ['C8' ,'D8', 'H4'],
#                                          'KB_PF+K_3': ['C9' ,'D9'] ,'sent':['G4', 'G5', 'G6']},
#                         'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
#                                           'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}},
#                'fig3':  {'title': 'Media M9, adapted KB SWB25' ,'ylims': (0.05 ,1.5) ,'xlims': (0 ,ft) ,
#                         'strains_data': {'KB_PF+K_1': ['E7' ,'F7'], 'KB_PF+K_2': ['E8' ,'F8', 'H6'],
#                                          'KB_PF+K_3': ['E9' ,'F9'] ,'sent':['G7', 'G8', 'G9']},
#                         'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
#                                           'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}},
#
#
#                #Putida adapted to TPA
#                'fig4': {'title': 'Media KB, adapted M9 + TPA SWB25' ,'ylims': (0.05 ,2.8) ,'xlims': (0 ,ft) ,
#                         'strains_data': {'KB_PF+K_1': ['A1' ,'B1'], 'KB_PF+K_2': ['A2' ,'B2', 'H1'],
#                                          'KB_PF+K_3': ['A3' ,'B3'] ,'sent':['G1', 'G2', 'G3']},
#                         'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
#                                           'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}},
#                'fig5':  {'title': 'Media M9 + TPA, adapted M9 + TPA SWB25' ,'ylims': (0.05 ,1.5) ,'xlims': (0 ,ft) ,
#                         'strains_data': {'KB_PF+K_1': ['C1' ,'D1'], 'KB_PF+K_2': ['C2' ,'D2', 'H3'],
#                                          'KB_PF+K_3': ['C3' ,'D3'],'sent':['G4', 'G5', 'G6']},
#                         'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
#                                           'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}},
#                'fig6':  {'title': 'Media M9, adapted M9 + TPA SWB25' ,'ylims': (0.05 ,2.8) ,'xlims': (0 ,ft) ,
#                         'strains_data': {'KB_PF+K_1': ['E1' ,'F1'], 'KB_PF+K_2': ['E2' ,'F2', 'H5'],
#                                          'KB_PF+K_3': ['E3' ,'F3'], 'sent':['G7', 'G8', 'G9']},
#                         'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
#                                           'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}}
#                 }


figs_params = {
                #Putida, adapted to KB
                'fig1': {'title': '0.1% KB + 10 mM TPA, 2 daysB' ,'ylims': (0.05 ,2.8) ,'xlims': (0 ,ft) ,
                        'strains_data': {'KB_PF+K_1': ['A7' ,'B7'], 'KB_PF+K_2': ['A8' ,'B8', 'H2'],
                                         'KB_PF+K_3': ['A9' ,'B9'] ,'sent':['G1', 'G2', 'G3']},
                        'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
                                          'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}},
               'fig2':  {'title': 'Media M9 + TPA, adapted KB SWB25' ,'ylims': (0.05 ,1.5) ,'xlims': (0 ,ft) ,
                        'strains_data': {'KB_PF+K_1': ['C7' ,'D7'], 'KB_PF+K_2': ['C8' ,'D8', 'H4'],
                                         'KB_PF+K_3': ['C9' ,'D9'] ,'sent':['G4', 'G5', 'G6']},
                        'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
                                          'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}},
               'fig3':  {'title': 'Media M9, adapted KB SWB25' ,'ylims': (0.05 ,1.5) ,'xlims': (0 ,ft) ,
                        'strains_data': {'KB_PF+K_1': ['E7' ,'F7'], 'KB_PF+K_2': ['E8' ,'F8', 'H6'],
                                         'KB_PF+K_3': ['E9' ,'F9'] ,'sent':['G7', 'G8', 'G9']},
                        'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
                                          'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}},


               #Putida adapted to TPA
               'fig4': {'title': 'Media KB, adapted M9 + TPA SWB25' ,'ylims': (0.05 ,2.8) ,'xlims': (0 ,ft) ,
                        'strains_data': {'KB_PF+K_1': ['A1' ,'B1'], 'KB_PF+K_2': ['A2' ,'B2', 'H1'],
                                         'KB_PF+K_3': ['A3' ,'B3'] ,'sent':['G1', 'G2', 'G3']},
                        'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
                                          'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}},
               'fig5':  {'title': 'Media M9 + TPA, adapted M9 + TPA SWB25' ,'ylims': (0.05 ,1.5) ,'xlims': (0 ,ft) ,
                        'strains_data': {'KB_PF+K_1': ['C1' ,'D1'], 'KB_PF+K_2': ['C2' ,'D2', 'H3'],
                                         'KB_PF+K_3': ['C3' ,'D3'],'sent':['G4', 'G5', 'G6']},
                        'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
                                          'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}},
               'fig6':  {'title': 'Media M9, adapted M9 + TPA SWB25' ,'ylims': (0.05 ,2.8) ,'xlims': (0 ,ft) ,
                        'strains_data': {'KB_PF+K_1': ['E1' ,'F1'], 'KB_PF+K_2': ['E2' ,'F2', 'H5'],
                                         'KB_PF+K_3': ['E3' ,'F3'], 'sent':['G7', 'G8', 'G9']},
                        'strains_color': {'KB_PF+K_1': c['orange'][1] ,'KB_PF+K_2': c['orange'][2],
                                          'KB_PF+K_3': c['orange'][3],'sent':c['grey'][3]}}
                }


font1 = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'bold',
        'size': 20,
        }
font2 = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'bold',
        'size': 15,
        }

def triplicating(replicates, well_dic):


    trip = [well_dic[k] for k in well_dic.keys() if k in replicates]
    arr = np.array(trip, dtype=np.float64).T
    avg = arr.mean(axis=1)
    std = arr.std(axis=1)
    return avg, std

def plotting(fname, figs_params):

    well_dic ,t = extractor(fname)

    for key in figs_params.keys():

        fig, ax = plt.subplots(figsize=(8, 6))

        # unroll the figs_params
        title = figs_params[key]['title']
        ylims = figs_params[key]['ylims']
        xlims = figs_params[key]['xlims']
        strains_data = figs_params[key]['strains_data']
        strains_color = figs_params[key]['strains_color']

        for strain_label, strain_wells in strains_data.items():

            color = strains_color[strain_label]

            if len(strain_wells)> 1:

                avg, std = triplicating(strain_wells, well_dic)


                plt.fill_between(t ,avg - std ,avg + std ,alpha=0.4 ,color=color)


            else:

                avg = well_dic[strain_wells[0]]


            ax.scatter(t, avg, label=strain_label, color=color, linewidth=0.5)



        ax.spines[['right' ,'top']].set_visible(False)
        plt.title(title, fontdict=font1)
        ax.legend()
        plt.ylim(ylims)
        plt.xlim(xlims)
        ax.set_ylabel('OD' ,fontdict=font2)
        ax.set_xlabel('Time (h)' ,fontdict=font2)
        plt.show()
        plt.close()
        outname = title + '.png'
        out_path = os.path.join('..', 'ClarioStar_Figs', outname)
        fig.savefig(out_path)


plotting(os.path.join('Matt_hypo', 'Matt_hypo.xlsx'), figs_params)
