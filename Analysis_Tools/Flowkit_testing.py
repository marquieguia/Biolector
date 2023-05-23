#import bokeh
#from bokeh.plotting import show
import matplotlib.pyplot as plt

import flowkit as fk
import os

# SAMPLE CLASS
fcs_path = os.path.join('..','DATA','FlowCytometer','03052023', 'C2.fcs')
s78 = fk.Sample(fcs_path)


df_s78 = s78.as_dataframe(source='raw')

print(s78.channels)

# bokeh_fig = s78.plot_histogram('FSC-H', source='raw')
matplot_fig = s78.plot_channel('Per-H', source='raw')
#print(type(matplot_fig))
#matplot_fig.savefig('test.png')
matplot_fig.show()




