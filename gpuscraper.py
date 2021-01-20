#! /usr/bin/env python3
"""Obter o preço do Iphone"""
import requests
import bs4
from datetime import datetime
import time


article_Dict={'Biostar Radeon RX 570 Gaming Dual Cooling OC 8GB':'https://www.pcdiga.com/placa-grafica-biostar-radeon-rx-570-gaming-dual-cooling-oc-8gb-va5705rv82?search=rx%20570', 
'Asus ROG Strix Radeon RX 570 8GB OC':'https://www.pcdiga.com/placa-grafica-asus-rog-strix-radeon-rx-570-8gb-oc-90yv0aj8-m0na00?search=rx%20570',
'Sapphire Radeon RX 570 PULSE 4GB OC': 'https://www.pcdiga.com/placa-grafica-sapphire-radeon-rx-570-pulse-4gb-oc-11266-67-20g?search=rx%20570',
'Powercolor Radeon RX 570 Red Dragon 8GB OC':'https://www.pcdiga.com/placa-grafica-powercolor-radeon-rx-570-red-dragon-8gb-oc-axrx-570-8gbd5-dhdv3-oc?search=rx%20570',
'Sapphire Radeon RX 570 PULSE 8GB G5 Lite': 'https://www.pcdiga.com/placa-grafica-sapphire-radeon-rx-570-pulse-8gb-g5-lite-11266-75-20g?search=rx%20570',
'XFX Radeon RX 570 RS 8GB XXX Edition':'https://www.pcdiga.com/placa-grafica-xfx-radeon-rx-570-rs-8gb-xxx-edition-rx-570p8dfd6?search=rx%20570',
'Sapphire Radeon RX 570 PULSE ITX 8GB G5':'https://www.pcdiga.com/placa-grafica-sapphire-radeon-rx-570-pulse-itx-8gb-g5-11266-37-20g?search=rx%20570',
'MSI Radeon RX 5700 XT Evoke 8G':'https://www.pcdiga.com/placa-grafica-msi-radeon-rx-5700-xt-evoke-8g-912-v381-204?search=5700%20xt',
'MSI GeForce RTX 3060 Ti Ventus 2X 8GB GDDR6 OC':'https://www.pcdiga.com/placa-grafica-msi-geforce-rtx-3060-ti-ventus-2x-8gb-gddr6-oc-912-v390-009'}


while True:
    stock=False
    output=''
    for k,v in article_Dict.items():
        site = requests.get(v)
        to_parse=bs4.BeautifulSoup(site.text,features="html.parser")

        css_class=to_parse.select(".price")
        css_class2=to_parse.select(".box-tocart")
        
        price=css_class[0].getText()
        try:
            if css_class2[0].getText().split()[-1]=='carrinho':
                stock=True
        except:
            stock=False

        now = datetime.now()
        current_time=f'{now.day}/{now.month}/{now.year}%{now.hour}:{now.minute}'

        if stock:
            output=current_time+'*DISPONÍVEL*'+k+'@'+price
        else:
            output=current_time+'&NÃO-DISPONÍVEL&'+k+'@'+price
        
        
        store="precos.txt"
        with open(store,"a") as store_obj:
            store_obj.write(output+"\n")


    time.sleep(60)
