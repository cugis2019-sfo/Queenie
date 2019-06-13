# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:33:16 2019

@author: admin
"""

import pandas as pd
import plotly, plot
#import plot

import pandas as pd
import plotly, plot
#import plot

studentlist = [["steve", 32,"male"], ["lia", 28,"female"], ["vin",45,"male"], ["katie",38,"female"]]
print(studentlistdf)

studentlistdf = pandas.DataFrame(studentlist,columns=["name", "age", "gender"],index= ["1","2","3","4"]
print(studentlistdf)




#graph our data
dir(plotly)
from plotly.offline import plot 
import plotly.graph_objs as go

agename =go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])

plot(agename)
