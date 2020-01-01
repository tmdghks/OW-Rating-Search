#-*- coding: utf-8 -*-
import requests
import json
headers = {'User-Agent':'Chrome/66.0.3359.181'}
battletag = input("battletag를 입력하십시오. (단, #은-로 대체합니다.)")
req = requests.get('https://ow-api.com/v1/stats/pc/asia/' + battletag + "/profile")
jsondata = req.json()

if jsondata == {'error': 'Player not found'}:
    print("ERR_배틀태그 정보가 잘못되었습니다.")
else:
    with open("Data/OW Data of " + battletag + ".json", "w") as file:
        file.write(req.text)
    print("총합 : " + str(jsondata['rating']))
    
    for i in range(len(jsondata['ratings'])):
        try:
            print(str(jsondata['ratings'][i]['role']) + " : " + str(jsondata['ratings'][i]['level']))
        except IndexError or TypeError:
            print(str(jsondata['ratings'][i]['role']) + " : 배치중")