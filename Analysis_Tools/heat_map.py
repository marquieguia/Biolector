import pandas as pd
import os
import numpy as np
import math
import matplotlib.pyplot as plt

def extractor(fname ,t_step=30):

    """INPUT -> ClarioStar generated .xlsx
       OUTPUT -> well_dic, a dict with wells as keys
       and their respective values are the ODs across cycles.
       E.g. well_dic['A1'] = pd.Series([0.087, 0.089, ...., 0.566])"""

    # INPUT DATA
    rows = list('ABCDEF')
    cols = [col for col in range(1 ,9)]
    input_path = os.path.join('..', 'DATA', 'ClarioStar', fname)
    df = pd.read_excel(input_path, usecols='A:I', header=13,
                        names=[x for x in range(0, 9)], index_col=0)

    #print(df)


    # EXTRACT WELLS' DATA
    well_dic = {}
    for row in rows:
        for col in cols:
            well_dic[row+str(col)] = df.loc[row, col]

    return well_dic

d1 = extractor('1day_KB-TPA_gradient.xlsx')
d2 = extractor('2day_KB-TPA_gradient.xlsx')
d3 = extractor('3day_KB-TPA_gradient.xlsx')
d4 = extractor('4day_KB-TPA_gradient.xlsx')
d5 = extractor('5day_KB-TPA_gradient.xlsx')
ds = [d1, d2, d3, d4, d5]

d1_diff, d2_diff, d3_diff, d4_diff, d5_diff = {}, {}, {}, {}, {}
diffs = [d1_diff, d2_diff, d3_diff, d4_diff, d5_diff]

for i in range(len(ds)):
    d = ds[i]
    diff = diffs[i]
    for key in d.keys():
        init, end = d[key].values
        diff[key] = end - init

def assign(d_diff):
    out_dic = {}
    out_dic['A100'] = np.array([d_diff['A1'], d_diff['B1'], d_diff['C1']]).mean()
    out_dic['A10'] = np.array([d_diff['A2'], d_diff['B2'], d_diff['C2']]).mean()
    out_dic['A1'] = np.array([d_diff['A3'] ,d_diff['B3'] ,d_diff['C3']]).mean()
    out_dic['A0'] = np.array([d_diff['A4'] ,d_diff['B4'] ,d_diff['C4']]).mean()

    out_dic['B100'] = np.array([d_diff['A5'] ,d_diff['B5'] ,d_diff['C5']]).mean()
    out_dic['B10'] = np.array([d_diff['A6'] ,d_diff['B6'] ,d_diff['C6']]).mean()
    out_dic['B1'] = np.array([d_diff['A7'] ,d_diff['B7'] ,d_diff['C7']]).mean()
    out_dic['B0'] = np.array([d_diff['A8'] ,d_diff['B8'] ,d_diff['C8']]).mean()

    out_dic['C100'] = np.array([d_diff['D1'] ,d_diff['E1'] ,d_diff['F1']]).mean()
    out_dic['C10'] = np.array([d_diff['D2'] ,d_diff['E2'] ,d_diff['F2']]).mean()
    out_dic['C1'] = np.array([d_diff['D3'] ,d_diff['E3'] ,d_diff['F3']]).mean()
    out_dic['C0'] = np.array([d_diff['D4'] ,d_diff['E4'] ,d_diff['F4']]).mean()

    out_dic['D100'] = np.array([d_diff['D5'] ,d_diff['E5'] ,d_diff['F5']]).mean()
    out_dic['D10'] = np.array([d_diff['D6'] ,d_diff['E6'] ,d_diff['F6']]).mean()
    out_dic['D1'] = np.array([d_diff['D7'] ,d_diff['E7'] ,d_diff['F7']]).mean()
    out_dic['D0'] = np.array([d_diff['D8'] ,d_diff['E8'] ,d_diff['F8']]).mean()


    return list(out_dic.values())

def assign2(d_diff):
    out_dic = {}
    out_dic['A100'] = np.array([d_diff['A1'], d_diff['C1'], d_diff['E1']]).mean()
    out_dic['A10'] = np.array([d_diff['A2'], d_diff['C2'], d_diff['E2']]).mean()
    out_dic['A1'] = np.array([d_diff['A3'] ,d_diff['C3'] ,d_diff['E3']]).mean()
    out_dic['A0'] = np.array([d_diff['A4'] ,d_diff['C4'] ,d_diff['E4']]).mean()

    out_dic['B100'] = np.array([d_diff['A5'] ,d_diff['C5'] ,d_diff['E5']]).mean()
    out_dic['B10'] = np.array([d_diff['A6'] ,d_diff['C6'] ,d_diff['E6']]).mean()
    out_dic['B1'] = np.array([d_diff['A7'] ,d_diff['C7'] ,d_diff['E7']]).mean()
    out_dic['B0'] = np.array([d_diff['A8'] ,d_diff['C8'] ,d_diff['E8']]).mean()

    out_dic['C100'] = np.array([d_diff['B1'] ,d_diff['D1'] ,d_diff['F1']]).mean()
    out_dic['C10'] = np.array([d_diff['B2'] ,d_diff['D2'] ,d_diff['F2']]).mean()
    out_dic['C1'] = np.array([d_diff['B3'] ,d_diff['D3'] ,d_diff['F3']]).mean()
    out_dic['C0'] = np.array([d_diff['B4'] ,d_diff['D4'] ,d_diff['F4']]).mean()

    out_dic['D100'] = np.array([d_diff['B5'] ,d_diff['D5'] ,d_diff['F5']]).mean()
    out_dic['D10'] = np.array([d_diff['B6'] ,d_diff['D6'] ,d_diff['F6']]).mean()
    out_dic['D1'] = np.array([d_diff['B7'] ,d_diff['D7'] ,d_diff['F7']]).mean()
    out_dic['D0'] = np.array([d_diff['B8'] ,d_diff['D8'] ,d_diff['F8']]).mean()


    return list(out_dic.values())

d1_list = list(d1_diff.values())
d1_avg =  [value for value in d1_list if not math.isnan(value)]
d2_avg = assign(d2_diff)
d3_avg = assign(d3_diff)
d4_avg = assign2(d4_diff)
d5_avg = assign(d5_diff)


TPA_grad = ["100 mM TPA", "10 mM TPA", "1 mM TPA", "0 mM TPA"]#,
           #   "10% KB + 100 mM TPA", "10% KB + 10 mM TPA", "10% KB + 1 mM TPA", "10% KB + 0 mM TPA",
            #  "1% KB + 100 mM TPA", "1% KB + 10 mM TPA", "1% KB + 1 mM TPA", "1% KB + 0 mM TPA",
             # "0% KB + 100 mM TPA", "0% KB + 10 mM TPA", "0% KB + 1 mM TPA", "0% KB + 0 mM TPA"]
days = ["Day1", "Day2", "Day3", "Day4", "Day5"]


KB100 = np.array([d1_avg[:4], d2_avg[:4], d3_avg[:4], d4_avg[:4], d5_avg[:4]]).T
KB10 = np.array([d1_avg[4:8], d2_avg[4:8], d3_avg[4:8], d4_avg[4:8], d5_avg[4:8]]).T
KB1 = np.array([d1_avg[8:12], d2_avg[8:12], d3_avg[8:12], d4_avg[8:12], d5_avg[8:12]]).T
KB0 = np.array([d1_avg[12:], d2_avg[12:], d3_avg[12:], d4_avg[12:], d5_avg[12:]]).T
KBs = [KB100, KB10, KB1, KB0]

titles = ['KB 100%', 'KB 10%', 'KB 1%', 'No KB']




fig, ax = plt.subplots()
data = KB0
title = 'No KB'
im = ax.imshow(data)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(days)), labels=days)
ax.set_yticks(np.arange(len(TPA_grad)), labels=TPA_grad)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

#Loop over data dimensions and create text annotations.

for i in range(len(TPA_grad)):
    for j in range(len(days)):
        text = ax.text(j, i, round(data[i, j], 2),
                       ha="center", va="center", color="w")

ax.set_title(title)
fig.tight_layout()
plt.show()
plt.close()
out_name = title + '.png'
fig.savefig(out_name)
print('next')