import requests
from lxml import etree
import csv

url = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=4f87f27e-74b1-11e5-88bb-d43d7e6fab60&type=0&batchType=本科&province=江苏&year=2023&batch=本科批&genre="

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

page = requests.get(url=url, headers=headers).json()
data = page["data"]
# print(data)
dataSource_list = data["data"]["dataSource"]
# print(dataSource_list)

for dataSource in dataSource_list:
        with open('data.csv', 'a+', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["计算机科学与技术",dataSource['college'], dataSource['low_score'], dataSource['elective_info'],dataSource['low_rank']])

