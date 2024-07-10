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

url_sx = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=044964c8-74b1-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_wlw = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=538727dc-74b1-11e5-9370-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_kqz = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=bb62aeb6-74b2-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_tm = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=561da516-74b1-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_yxy = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=0cd01c66-74b3-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_sj = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=0b862b28-60e3-11e9-a1c1-f8f21e345dfc&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_jr = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=2d05f290-74b2-11e5-9370-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_wl = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=4a4739cc-74b2-11e5-bdc1-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_xxa = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=7c22d302-74b2-11e5-88e2-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_sw = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=aa6c2214-74b1-11e5-a987-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_hx = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=0adf7200-74b1-11e5-88bb-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_gs = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=d6fdd52e-74b2-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_xq = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=59722210-74b5-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_sp = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=9eada5ce-74b1-11e5-88bb-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_cl = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=341f9e24-74b1-11e5-ad01-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_mz = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=0b877750-74b3-11e5-88bb-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_dzs = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=f807834c-74b1-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_xl = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=240e33b0-74b1-11e5-a987-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_sjx = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=e1f26112-74b1-11e5-a987-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_jz = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=a52ec284-74b1-11e5-88bb-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_ly = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=e90a2a88-74b2-11e5-9532-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_lcy = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=ee753ad8-74b4-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_zc = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=dc73f732-74b1-11e5-ad01-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_xny = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=68b2e3fc-74b2-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_tj = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=26976b9c-74b1-11e5-b379-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="
url_ls = "https://gk.quark.cn/api/fractional/precedence/getPrecedenceScoreData?guid=ff0507e2-74b0-11e5-bdc1-d43d7e6fab60&type=0&batchType=%E6%9C%AC%E7%A7%91&province=%E6%B1%9F%E8%8B%8F&year=2023&batch=%E6%9C%AC%E7%A7%91%E6%89%B9&genre="

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

page = requests.get(url=url_ls, headers=headers).json()
data = page["data"]
dataSource_list = data["data"]["dataSource"]

for dataSource in dataSource_list:
    with open('data.csv', 'a+', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["历史学", dataSource['college'], dataSource['low_score'], dataSource['elective_info'],
                         dataSource['low_rank']])
