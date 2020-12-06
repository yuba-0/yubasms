#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s

import os

os.system("apt-get install figlet")

os.system("clear")

os.system("figlet YUBA - SMS GONDERME ARACI")

banner = """
                             >Coder By Yuba
|> İstediginiz telefon adresine hergun 1 defa mesaj atma hakkınız var>
|> Mesajınızdaki karakter sayısı sınırlıdır.
|> Tel adresinizi Doğru girmezseniz hata vericektir.
|> Çalıştığını kendinizde deneyebilirsiniz.
"""

print(banner)

sor = input("Tel adresi Örn:+905555555555 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek kısmı aşagıdaki gibidir.\n"+a>

drlm = input("\n| Mesajınız Gönderilsinmi?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hata yaptınız.")
