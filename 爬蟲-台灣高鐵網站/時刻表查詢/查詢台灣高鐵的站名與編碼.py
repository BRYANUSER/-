#爬取台灣高鐵站名與編碼
import requests, bs4

url = 'https://www.thsrc.com.tw/ArticleContent/a3b630bb-1066-4352-a1ef-58c7b4e8ef7c'
htmlFile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
stations = objSoup.find('select', id='select_location01').find_all('option')

print("高鐵站名與編碼:")
for station in stations:
    print (station.text.strip(), " : ", station['value'])
    