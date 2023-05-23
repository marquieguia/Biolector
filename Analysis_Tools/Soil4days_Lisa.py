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



df = pd.read_excel(os.path.join('..', 'DATA', 'Soil', 'soil4days_Lisa.xlsx'), sheet_name='Sheet2', usecols='I:R').dropna()
t = df['Time']
TPA0 = df[['A0', 'B0', 'C0']]
TPA25 = df[['A25', 'B25', 'C25']]
TPA50 = df[['A50', 'B50', 'C50']]

l = [TPA0, TPA25, TPA50]
colors = ['lightgrey', 'limegreen', 'forestgreen']
labels = ['0 mM TPA', '25 mM TPA', '50 mM TPA']
markers = [ ".", "v", "p"]

fig ,ax = plt.subplots(figsize=(12 ,8))

for i, elem in enumerate(l):
    avg = elem.mean(axis=1)
    std = elem.std(axis=1)
    ax.plot(t, avg, color=colors[i], markersize=15, marker=markers[i], label=labels[i])
    ax.errorbar(t ,avg ,std ,ls='none' ,marker='^' ,color=colors[i] ,capsize=6 ,alpha=0.3)

# ax.scatter(t, avg, color=colors[i], markersize=20)




ax.legend(prop=font2)
ax.spines[['right' ,'top']].set_visible(False)
ax.grid(True)
title = 'Growth on soil SWB25 pQBR57-tphKAB'
ax.set_title(title, fontproperties=font1)
ax.set_ylabel('CFU ' ,fontproperties=font2)
plt.yticks(fontsize=14 ,fontproperties=font2)
plt.yscale('log')

ax.set_xlabel('Time (h)' ,fontproperties=font2)
plt.xticks(fontsize=14 ,fontproperties=font2)
fig_name = title + '.png'
out_path = os.path.join('..' ,'Soil_Figs' ,fig_name)
fig.savefig(out_path)
plt.show()
plt.close()