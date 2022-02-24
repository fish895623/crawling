# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DATAFRAME = pd.read_excel("movie1.xlsx")

DATAFRAME.to_csv("ff.csv")
# %%
RATE = 0.2
TOP_RATE = int(len(DATAFRAME) * RATE)
a = DATAFRAME.loc[DATAFRAME["provocative"] == 1]
#%%
datas_kaggle = pd.read_csv("netflix_titles.csv")
datas_kaggle["rating"] = datas_kaggle["rating"].map(
    {
        "TV-PG": "Older Kids",
        "TV-MA": "Adults",
        "TV-Y7-FV": "Older Kids",
        "TV-Y7": "Older Kids",
        "TV-14": "Teens",
        "R": "Adults",
        "TV-Y": "Kids",
        "NR": "Adults",
        "PG-13": "Teens",
        "TV-G": "Kids",
        "PG": "Older Kids",
        "G": "Kids",
        "UR": "Adults",
        "NC-17": "Adults",
    }
)
datas_kaggle["provocative"] = np.where(datas_kaggle['rating'] == "Adults", 1,0)
datas_kaggle["rank"] = (datas_kaggle.index + 1)
