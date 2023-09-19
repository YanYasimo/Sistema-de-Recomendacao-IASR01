#%%
import pandas as pd 
import numpy as np

#create a dataframe
df = pd.DataFrame([1, 2, 3, 65], columns=["coluna1"])
df

# %%

df["coluna2"] = [4, 5, 6, 7]
df

# %%
#creating dataframe from a json file
df = pd.read_json("https://api.bcb.gov.br/dados/serie/bcdata.sgs.16121/dados?formato=json")
df

# %%
#creating dataframe from a csv file
#df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
df = df[df["location"] == "Brazil"]
df
# %%
