# %%[markdown]
### 개별과제
# - 리뷰데이터 수집
# - 그외 관심있는 텍스트 수집
### 조별과제
# - 워드 클라우드 만들기
# - 수집한 데이터에 대한 형태소 분석

import gc
import re

# %%
from json import JSONDecodeError
from multiprocessing import Pool

import pandas as pd
import requests

gc.set_threshold(1000, 100, 100)
# %%[markdown]
# ### Wordcloud, Konlpy를 위한 문자열 Preprocessing
def clean_text(inputString: str):
    special = re.compile(r"[^ A-Za-z가-힣+]")
    result = special.sub("", inputString)
    return result


# %%
def gendate(url: str, merchantNo: str, originProductNo: str):
    DATA = {
        "id": [],
        "reviewContent": [],
        "createDate": [],
        "reviewScore": [],
    }
    # %%
    PAGE = 1
    while True:
        try:
            PAGE += 1
            reviews = requests.get(
                f"https://brand.naver.com/n/v1/reviews/paged-reviews?page={PAGE}&pageSize=30&merchantNo={merchantNo}&originProductNo={originProductNo}&sortType=REVIEW_RANKING"
            ).json()
            reviews["contents"]
            for review in reviews["contents"]:
                DATA["id"].append(review["id"])
                DATA["reviewContent"].append(
                    clean_text(review["reviewContent"].replace("\n", " "))
                )
                DATA["createDate"].append(review["createDate"].strip())
                DATA["reviewScore"].append(review["reviewScore"])
        except JSONDecodeError:
            break
    # %%
    df = pd.DataFrame(DATA)

    # %%
    df.to_csv(path_or_buf=f"{url}.csv", encoding="utf-8")


# %%
if __name__ == "__main__":
    a = [
        ["5174410691", "500030812", "5154861564"],
        ["474589013", "500196931", "474589013"],
        ["2146095417", "500031227", "2145160507"],
        ["5088641128", "500176670", "5070282749"],
        ["3327518275", "500176670", "3322560121"],
        ["3917009354", "500176670", "3910143421"],
        ["5754878048", "500176670", "5729053371"],
    ]
    for i in a:
        gendate(i[0], i[1], i[2])
