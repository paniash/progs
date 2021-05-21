import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%%
confirmed_data = pd.read_csv("confirmed.csv")

#%% Seeing your data
confirmed_data.head()

#%%
confirmed_data.columns

#%% Removing stuff
confirmed_data = confirmed_data.drop(["Lat", "Long", "Province/State"], axis=1)

confirmed_data[confirmed_data['Country/Region'] == "Algeria"]

#%%
confirmed_data["Country/Region"].unique()


#%% Random
confirmed_data[confirmed_data['Country/Region'] == "Australia"].sum(axis=0)
confirmed_data[confirmed_data.duplicated(["Country/Region"])]

#%%
duplicated_countries = confirmed_data[confirmed_data.duplicated(["Country/Region"])]["Country/Region"].unique
confirmed_data[confirmed_data["Country/Region"] == duplicated_countries]
