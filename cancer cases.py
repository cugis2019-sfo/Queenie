import pandas as pd 
import plotly 
from plotly.offline import plot
import plotly.graph_objs as go  

df = pd.read_excel("GISdata.xlsx", sheet_name = "cancercases")

print(df)

#we use the Bar graph option of the graph_objs function from the plotly library
cancer = go.Bar(x = df["CancerType"], y = df["Number"],
                      marker = {"color": df["Number"], "colorscale" : "Portland"}
                    
              
              )

plot ([cancer])

titles = go.Layout(
                   #Define title of the graph
                   title ="Cancer Cases" ,
                   
                   #Define title for x-axis
                   xaxis=go.layout.XAxis(
                           title=go.layout.xaxis.Title(
                           text="Cancer Types",  
                       )   
                   ), 
                           
                    #Define title for y-axis       
                    yaxis=go.layout.YAxis(
                             title=go.layout.yaxis.Title( 
                             text="Numbers of people" ,
                             )
                      )       
                   )
                             
#we use Figure option of the graph_objs function from the plotly library
fig = go.Figure(data=[cancer], layout=titles)
                
#we call the plot function from the plotly,offline library
plot(fig)













