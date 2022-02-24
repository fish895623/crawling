from pickle import LIST
import winsound
from collections import Counter

import numpy as np
import pandas as pd
from konlpy.tag import Okt
from wordcloud import WordCloud

exclude_words = ["두", "년", "곳", "은", "습", "점", "게", "듯"]


def create(product_number: str):
    df = pd.read_csv(f"{product_number}.csv", encoding="utf-8")
    okt = Okt()
    LISTS = []
    for i in df["reviewContent"]:
        if i is np.nan:
            continue
        else:
            nouns = okt.nouns(i)
            for j in nouns:
                LISTS.append(j)

    c = Counter(LISTS)
    words = dict(c)
    for s in exclude_words:
        del words[s]

    wc = WordCloud(
        font_path="C:/WINDOWS/FONTS/D2CODING-VER1.3.2-20180524.TTF",
        width=800,
        height=400,
        scale=2.0,
        max_font_size=250,
        background_color='white',
    )
    wc.generate_from_frequencies(words)
    wc.to_file(f"{product_number}.png")


create(product_number="5174410691")

winsound.Beep(
    frequency=440,
    duration=1000,
)  # Hz  # milliseconds
