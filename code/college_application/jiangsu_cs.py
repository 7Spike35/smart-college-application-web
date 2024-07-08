import requests
from lxml import etree
import csv

url_cs = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=4f87f27e-74b1-11e5-88bb-d43d7e6fab60&type=0&batchType=本科&province=江苏&year=2023&batch=本科批&genre="
url_kq = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=bb62aeb6-74b2-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_dq = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=450990f0-74b1-11e5-ad01-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

page = requests.get(url=url_dq, headers=headers).json()
data = page["data"]
# print(data)
dataSource_list = data["data"]["dataSource"]
# print(dataSource_list)

for dataSource in dataSource_list:
        with open('data.csv', 'a+', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["电气工程及其自动化",dataSource['college'], dataSource['low_score'], dataSource['elective_info'],dataSource['low_rank']])

