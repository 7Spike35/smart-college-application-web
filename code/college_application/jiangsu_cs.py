import requests
from lxml import etree
import csv

url_cs = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=4f87f27e-74b1-11e5-88bb-d43d7e6fab60&type=0&batchType=本科&province=江苏&year=2023&batch=本科批&genre="
url_kq = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=bb62aeb6-74b2-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_dq = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=450990f0-74b1-11e5-ad01-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_hy = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=1abcb2ca-74af-11e5-88bb-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_zdh = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=4e334d6a-74b1-11e5-ad01-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_fx = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=3242caee-74b2-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_lc = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=ee753ad8-74b4-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_rg = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=50d1ec5c-74b1-11e5-9532-d43d7e6fab60&type=0&batchType=本科&province=江苏&year=2023&batch=本科批&genre="
url_dz = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=46511154-74b1-11e5-ad01-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_hl = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=d44b8278-74b1-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_kj = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=d898a8be-74b2-11e5-aea7-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_ai = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=3bc61548-c508-11ea-9b21-f8f21e345750&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_xx = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=1493ea30-74af-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_jx = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=2db21f8a-74b1-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_tx = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=48fc3532-74b1-11e5-88bb-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_sz = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=d58f1eac-76ef-11e5-951b-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_zy = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=be9d65ee-74b2-11e5-88bb-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_yx = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=fbc385a0-74b4-11e5-9370-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_yy = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=211b0900-74af-11e5-9532-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_dw = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=ff1b8a64-76ed-11e5-9a86-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

page = requests.get(url=url_dw, headers=headers).json()
data = page["data"]
dataSource_list = data["data"]["dataSource"]


for dataSource in dataSource_list:
        with open('data.csv', 'a+', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["动物医学",dataSource['college'], dataSource['low_score'], dataSource['elective_info'],dataSource['low_rank']])

