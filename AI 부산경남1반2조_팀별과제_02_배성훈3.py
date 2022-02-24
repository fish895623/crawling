#%%
import pandas as pd
import matplotlib.pyplot as plt
import gc
import datetime

gc.set_threshold(2000, 100, 100)

# %%time
a = pd.read_csv("data.csv")
b = a.sort_values(by="createDate")
print(b["createDate"][:300])
# %%
b["Date"] = pd.to_datetime(b["createDate"], format="%Y-%m-%d")
b[b["Date"] > datetime.date(2020, 7, 21)]
a = b[b["createDate"] < datetime.date(2020, 7, 21)]
# %% [markdown]
# 헤헤
plt.plot(b["createDate"][:300], b["reviewScore"][:300])
plt.show()
