import pandas as pd
import plotly.express as px


df_read = pd.read_csv("bimodal_distribution.csv")

# Step 4: Plot the Bimodal Distribution using Plotly Express
fig = px.histogram(df_read, x="Seed Yield", color="Category", marginal="rug",
                   hover_data=df_read.columns, title="Bimodal Distribution of Seed Yield")

fig.show()
