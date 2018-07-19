from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
def get(page):
    html=urlopen("http://stock.10jqka.com.cn/agcbsj_list/index_"+str(page)+".shtml")
    soup=BeautifulSoup(html,"lxml")
    Lists=soup.find_all("span",class_="arc-title")
    for name in Lists:
        title=name.find("a").get_text()
        print(title.strip()+"\n")
for page in range(1,50):
    get(page)