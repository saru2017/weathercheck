#!/data/apps/anaconda/python
# coding: utf-8 

import requests
import sys
import io
import lxml.html
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def get_weather():
    url = "https://weather.yahoo.co.jp/weather/jp/27/6200.html"
    r = requests.get(url)
    dom = lxml.html.fromstring(r.text)
    items = dom.xpath("//p[@class='pict']/img")
    weather = items[0].attrib['alt']

    items = dom.xpath("//ul[@class='temp']/li/em")
    max_t = int(items[0].text)
    min_t = int(items[1].text)
    
    return (weather, max_t, min_t)


def create_db():
    f = open("/data/config/log.csv", "r", encoding="utf-8")
    lst = list(csv.reader(f))
    return lst
    

if __name__ == "__main__":
    (weather, max_t, min_t) = get_weather()   
    print(weather, max_t, min_t)
    if max_t > 28:
        print("ポロシャツ")

    if min_t > 20:
        print("半袖T")
    elif min_t > 10:
        print("長袖T")
    else:
        print("長袖T×2")
        
    items = create_db()
        
    print("チノパン")

    d = 10000
    ret = ""

    for item in items:
        l = (max_t - int(item[0]))**2 + (min_t - int(item[1]))**2
        if l < d:
            ret = item
            d = l

    print(ret)

