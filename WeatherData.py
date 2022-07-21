import csv
import time
import datetime
import bs4
import urllib.request

csvName =  'C:/CSV/sokcho_weather.csv'
with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초', '온도', '습도', '강수량', '풍향'])

nateUrl = "https://news.nate.com/weather?areaCode=11D20401"
while True :
    htmlObject = urllib.request.urlopen(nateUrl)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
    tag = bsObject.find('div', {'class': 'right_today'})
    temper = tag.find('p', {'class': 'celsius'}).text #섭씨 온도
    humi = tag.find('p', {'class': 'humidity'}).text #습도
    rain = tag.find('p', {'class': 'rainfall'}).text #강수량
    wind = tag.find('p', {'class': 'wind'}).text #풍향

    now = datetime.datetime.now()
    yymmdd = now.strftime('%Y-%m-%d') # 연도, 월, 일
    hhmmss = now.strftime('%H:%M:%S') # 시, 분, 초

    weather_list = [yymmdd, hhmmss, temper, humi, rain, wind] #리스트 생성 및 초기화
    with open(csvName, 'a', newline='') as csvFp: 
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(weather_list)
        print(weather_list) #리스트 출력 

    time.sleep(3600)
