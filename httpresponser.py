import requests
import os

from requests.models import Response
#EmreZeriX

print("""
 _   _ _   _        ______                                          
| | | | | | |       | ___ \                                         
| |_| | |_| |_ _ __ | |_/ /___  ___ _ __   ___  _ __  ___  ___ _ __ 
|  _  | __| __| '_ \|    // _ \/ __| '_ \ / _ \| '_ \/ __|/ _ \ '__|
| | | | |_| |_| |_) | |\ \  __/\__ \ |_) | (_) | | | \__ \  __/ |   
\_| |_/\__|\__| .__/\_| \_\___||___/ .__/ \___/|_| |_|___/\___|_|   
              | |                  | |                              
              |_|                  |_|
""")


link = input("İstek atılacak link giriniz :")
istek = requests.get(link, stream=True)
yanıt = Response.ok
print("Get atılan link : {0}".format(link))
print("Sunucudan gelen response.ok yanıtı :{0}".format(yanıt))
print("Sunucudan gelen durum kodu : {0}".format(istek))

