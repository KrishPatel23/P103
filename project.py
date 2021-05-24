import pandas as pd 
import plotly.express as px 
df = pd.read_csv("project.csv")
figure=px.scatter(df, x="date", y="cases", color="country")
figure.show()