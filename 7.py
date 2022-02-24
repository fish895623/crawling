import gc
import json

from selenium import webdriver
from selenium.webdriver.common.by import By

gc.set_threshold(1000, 100, 100)

FILE = "7.json"
DATA = []
URL = "https://www.netflix.com/kr/browse/genre/839338"

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("disable-gpu")

driver = webdriver.Chrome(options=options)

driver.get(url=URL)
elements = driver.find_elements(
    by=By.CSS_SELECTOR,
    value=".nm-collections-page > main > section > div > ul > li",
)
for element in elements:
    DATA.append(element.text)
with open(file=FILE, mode="w", encoding="UTF-8") as file:
    json.dump(DATA, file, ensure_ascii=False)

driver.quit()
