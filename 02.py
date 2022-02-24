# %% [markdown]
# # Essential packages & Base DataFrame Structure

# %%
import gc
from itertools import count
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

gc.set_threshold(2000, 100, 100)

URL = "https://flixpatrol.com/top10/netflix/world/2021/full/#netflix-1"
MOVIES = {
    "title": [],
    "points": [],
    "countries": [],
    "percountries": [],
    "days": [],
    "perdays": [],
    "total": [],
}
SERIES = {
    "title": [],
    "points": [],
    "countries": [],
    "percountries": [],
    "days": [],
    "perdays": [],
    "total": [],
}
file_name = {
    "top10": "top10.csv",
    "movie": "movie.csv",
    "series": "series.csv",
}
source = BeautifulSoup(requests.get(url=URL).text, features="html.parser")

# %% [markdown]
# # Movie

# %%
movies = source.select("#netflix-1 > div.-mx-content > div > div > table > tbody > tr")
# %%
def get_info(href: str):
    val = []
    # netflix-1 > div.-mx-content > div > div > table > tbody > tr:nth-child(1) > td.table-td.w-1\/2 > a
    url = f"https://flixpatrol.com/{href}"
    source = BeautifulSoup(markup=requests.get(url=url).text, features="html.parser")
    a = source.select_one(
        ".content.mt-4 > div > div.flex-grow > div.mb-6 > div.flex.flex-wrap.text-gray-500 > div"
    ).find_all("span", text=True)

    for i in a:
        if i.get("title"):
            continue
        elif i.get("class"):
            continue
        else:
            val.append(i.get_text())
    return val


# %% [markdown]
# 각 요소별로 저장
for movie in movies:
    title = movie.select_one(
        "#netflix-1 > div.-mx-content > div > div > table > tbody > tr > td:nth-child(3)"
    ).text.strip()
    points = int(
        movie.select_one(
            ".-mx-content > div > div > table > tbody > tr > td:nth-child(4)"
        )
        .text.strip()
        .replace(",", "")
    )
    countries = int(
        movie.select_one(
            "#netflix-1 > div.-mx-content > div > div > table > tbody > tr > td:nth-child(6)"
        )
        .text.strip()
        .replace(",", "")
    )
    MOVIES["title"].append(title)
    MOVIES["points"].append(points)
    MOVIES["countries"].append(countries)
    MOVIES["percountries"].append(
        int(
            movie.select_one(
                "#netflix-1 > div.-mx-content > div > div > table > tbody > tr > td:nth-child(7)"
            )
            .text.strip()
            .replace(",", "")
        )
    )
    MOVIES["days"].append(
        int(
            movie.select_one(
                "#netflix-1 > div.-mx-content > div > div > table > tbody > tr > td:nth-child(8)"
            )
            .text.strip()
            .replace(",", "")
        )
    )
    MOVIES["perdays"].append(
        int(
            movie.select_one(
                "#netflix-1 > div.-mx-content > div > div > table > tbody > tr > td:nth-child(9)"
            )
            .text.strip()
            .replace(",", "")
        )
    )
    MOVIES["total"].append(
        int(
            movie.select_one(
                "#netflix-1 > div.-mx-content > div > div > table > tbody > tr > td:nth-child(10)"
            )
            .text.strip()
            .replace(",", "")
        )
    )
    # MOVIES["genre"].append(
    #     get_info(
    #         movie.select_one(
    #             "#netflix-1 > div.-mx-content > div > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > a"
    #         ).get("href")
    #     )
    # )

# %% [markdown]
# # TV series

# %% [markdown]
# # Export to csv
MOVIES_DF = pd.DataFrame(MOVIES)
MOVIES_DF.to_csv(path_or_buf=file_name["movie"], encoding="utf-8")
