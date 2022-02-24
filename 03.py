# %%
import pandas as pd
import requests
from bs4 import BeautifulSoup

# %%
URL = "https://flixpatrol.com/top10/"
DATA = {
    "title": [],
    "score": [],
}

sources = BeautifulSoup(markup=requests.get(url=URL).text, features="html.parser")
# %%
elements = sources.select(
    "#netflix-1 > div.-mx-content > div > div > table > tbody > tr"
)
for i in elements:
    DATA["title"].append(
        i.select_one(
            ".-mx-content > div > div > table > tbody > tr > td > a > div:nth-child(2)",
        ).text.strip()
    )
    DATA["score"].append(
        i.select_one(
            ".-mx-content > div > div > table > tbody > tr > td.table-td.w-12.text-right.text-gray-400.font-semibold",
        ).text.strip()
    )

# %%
TOP_10_df = pd.DataFrame(DATA)

TOP_10_df.to_csv(path_or_buf="top10.csv", encoding="UTF-8")

# %%
