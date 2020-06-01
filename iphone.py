#! /usr/bin/env python3
"""Obter o preço do Iphone"""
import requests
import bs4
import time


site = requests.get('https://www.worten.pt/telemoveis-e-pacotes-tv/telemoveis-e-smartphones/iphone/iphone-11-apple-6-1-128-gb-preto-7016626')
to_parse=bs4.BeautifulSoup(site.text,features="html.parser")
css_class=to_parse.select(".w-product-price__main")

store="precos.txt"
with open(store,"a") as store_obj:
    store_obj.write(css_class[1].getText()+"\n")

print(time.time()/60/60/24/365+1970)
print(type(site))
print(type(to_parse))
