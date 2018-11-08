#!/usr/bin/env python
# coding: utf-8 

import requests
import sys
import io
import bs4
import lxml.html

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def get_weather():
    url = "https://weather.yahoo.co.jp/weather/jp/27/6200.html"
    r = requests.get(url)
#    print(vars(r))
#    html = r.text
#    start = html.find('<div class="forecastCity">')
#    end = html.find('</div>', start)
#    html = html[start : end]
#    print(html)
#    soup = bs4.BeautifulSoup(r.text, "html.parser")
#    items = soup.select(".forecastCity")
#    print(items)
    dom = lxml.html.fromstring(r.text)
#    items = dom.xpath("//div[@class='forecastCity']/table/tr/td/div/p")
    items = dom.xpath("//p[@class='pict']/img")
#    print(items[0].attrib['alt'])
#    print(items[1].attrib['alt'])
    weather = items[0].attrib['alt']

    items = dom.xpath("//ul[@class='temp']/li/em")

#    print(items[0].text)
#    print(items[1].text)
    max_t = int(items[0].text)
    min_t = int(items[1].text)
    
    return (weather, max_t, min_t)

    

if __name__ == "__main__":
    (weather, max_t, min_t) = get_weather()   
    print(weather, max_t, min_t)
    if max_t > 28:
        print("ポロシャツ")

    print("チノパン")


