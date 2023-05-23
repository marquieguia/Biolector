import pandas as pd
import os
import re
import numpy as np


def extractor(fname ,t_step=30):

    """INPUT -> ClarioStar generated .xlsx
       OUTPUT -> well_dic, a dict with wells as keys
       and their respective values are the ODs across cycles.
       E.g. well_dic['A1'] = pd.Series([0.087, 0.089, ...., 0.566])"""

    # INPUT DATA
    rows = list('ABCDEFGH')
    cols = [col for col in range(1 ,13)]
    input_path = os.path.join('..', 'DATA', 'ClarioStar', fname)
    df = pd.read_excel(input_path, usecols='A:M', header=14,
                        names=[x for x in range(0, 13)], index_col=0)

    tf = str(df.iloc[[-9], [0]].index.values[0])
    if len(tf) == 3:
        tf = str(df.iloc[[-11] ,[0]].index.values[0])
    else: pass

    hours = int(re.search(r'\((\d*)', tf).groups(0)[0])
    if re.search(r'h (\d*)', tf):
        mins = int(re.search(r'h (\d*)' ,tf).groups(0)[0])

    else:
        mins = 0
    total_mins = hours * 60 + mins
    t = np.array([x for x in range(0, total_mins+1, t_step)]) / 60

    # EXTRACT WELLS' DATA
    well_dic = {}
    print(df)
    for row in rows:
        for col in cols:
            well_dic[row+str(col)] = df.loc[row, col]

    return well_dic, t

# extractor(os.path.join('Matt_hypo', 'Matt_hypo.xlsx'))