header = {"User-Agent" :
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

import requests as rq
from bs4 import BeautifulSoup

PATH = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=9860229&str_cat"

r = rq.get(PATH, headers=header)

soup = BeautifulSoup(r.text, "lxml")

goodsName = soup.find("span", id="osmGoodsName").text
print(goodsName)

goodsType = soup.find("a", id="webBrand").text
print(goodsType)

IMG = "https://i2.momoshop.com.tw/1693162294/goodsimg/0009/860/229/9860229_B.webp"

rImg = rq.get(IMG, headers=header).content
with open("asus.jpg","wb") as f:
    f.write(rImg)

