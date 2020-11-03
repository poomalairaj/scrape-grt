import plotly
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("grt.csv")

data = [go.Scatter(
              x=df.date,
                        y=df['price'])]

plotly.offline.plot(data, filename='gold_price.html')
