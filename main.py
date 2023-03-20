import requests  # 发送请求
import pandas as pd  # 存入excel数据
from time import sleep  # 等待间隔,防止反爬
import random  # 随机等待

# 循环请求1-15页
for page in range(1, 16):
    # 胡润百富榜地址
    sleep_seconds = random.uniform(1, 2)
    print('开始等待{}秒'.format(sleep_seconds))
    sleep(sleep_seconds)
    print('开始爬取第{}页'.format(page))
    offset = (page - 1) * 200
    url = 'https://www.hurun.net/zh-CN/Rank/HsRankDetailsList?num=YUBAO34E&search=&offset={}&limit=200'.format(offset)
    # 构造请求头
    headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br',
        'content-type': 'application/json',
        'referer': 'https://www.hurun.net/zh-CN/Rank/HsRankDetails?pagetype=rich'
    }
    # 发送请求
    r = requests.get(url, headers=headers)

    # 解析JSON数据
    json_data = r.json()

    Fullname_Cn_list = []  # 全名_中文
    Fullname_En_list = []  # 全名_英文
    Age_list = []  # 年龄
    BirthPlace_Cn_list = []  # 出生地_中文
    BirthPlace_En_list = []  # 出生地_英文
    Gender_list = []  # 性别
    Photo_list = []  # 照片
    ComName_Cn_list = []  # 公司名称_中文
    ComName_En_list = []  # 公司名称_英文
    ComHeadquarters_Cn_list = []  # 公司总部地_中文
    ComHeadquarters_En_list = []  # 公司总部地_英文
    Industry_Cn_list = []  # 所在行业_中文
    Industry_En_list = []  # 所在行业_英文
    Ranking_list = []  # 排名
    Ranking_Change_list = []  # 排名变化
    Relations_list = []  # 组织结构
    Wealth_list = []  # 财富值_人民币_亿
    Wealth_Change_list = []  # 财富值变化
    Wealth_USD_list = []  # 财富值_美元
    Year_list = []  # 年份

    print("开始解析json数据")
    item_list = json_data['rows']
    for item in item_list:
        print(item['hs_Character'][0]['hs_Character_Fullname_Cn'])

        # item['hs_Character'][0]['']
        Fullname_Cn_list.append(item['hs_Character'][0]['hs_Character_Fullname_Cn'])  # 全名_中文
        Fullname_En_list.append(item['hs_Character'][0]['hs_Character_Fullname_En'])  # 全名_英文
        Age_list.append(item['hs_Character'][0]['hs_Character_Age'])  # 年龄
        BirthPlace_Cn_list.append(item['hs_Character'][0]['hs_Character_BirthPlace_Cn'])  # 出生地_中文
        BirthPlace_En_list.append(item['hs_Character'][0]['hs_Character_BirthPlace_En'])  # 出生地_英文
        Gender_list.append(item['hs_Character'][0]['hs_Character_Gender'])  # 性别
        Photo_list.append(item['hs_Character'][0]['hs_Character_Photo'])  # 照片

        # item['']
        ComName_Cn_list.append(item['hs_Rank_Rich_ComName_Cn'])  # 公司名称_中文
        ComName_En_list.append(item['hs_Rank_Rich_ComName_En'])  # 公司名称_英文
        ComHeadquarters_Cn_list.append(item['hs_Rank_Rich_ComHeadquarters_Cn'])  # 公司总部地_中文
        ComHeadquarters_En_list.append(item['hs_Rank_Rich_ComHeadquarters_En'])  # 公司总部地_英文
        Industry_Cn_list.append(item['hs_Rank_Rich_Industry_Cn'])  # 所在行业_中文
        Industry_En_list.append(item['hs_Rank_Rich_Industry_En'])  # 所在行业_英文
        Ranking_list.append(item['hs_Rank_Rich_Ranking'])  # 排名
        Ranking_Change_list.append(item['hs_Rank_Rich_Ranking_Change'])  # 排名变化
        Relations_list.append(item['hs_Rank_Rich_Relations'])  # 组织结构
        Wealth_list.append(item['hs_Rank_Rich_Wealth'])  # 财富值_人民币_亿
        Wealth_Change_list.append(item['hs_Rank_Rich_Wealth_Change'])  # 财富值变化
        Wealth_USD_list.append(item['hs_Rank_Rich_Wealth_USD'])  # 财富值_美元
        Year_list.append(item['hs_Rank_Rich_Year'])  # 年份#

    df = pd.DataFrame(  # 拼装爬取到的数据为DataFrame
            {
                '排名': Ranking_list,
                '排名变化': Ranking_Change_list,
                '全名_中文': Fullname_Cn_list,
                '全名_英文': Fullname_En_list,
                '年龄': Age_list,
                '出生地_中文': BirthPlace_Cn_list,
                '出生地_英文': BirthPlace_En_list,
                '性别': Gender_list,
                '照片': Photo_list,
                '公司名称_中文': ComName_Cn_list,
                '公司名称_英文': ComName_En_list,
                '公司总部地_中文': ComHeadquarters_Cn_list,
                '公司总部地_英文': ComHeadquarters_En_list,
                '所在行业_中文': Industry_Cn_list,
                '所在行业_英文': Industry_En_list,
                '组织结构': Relations_list,
                '财富值_人民币_亿': Wealth_list,
                '财富值变化': Wealth_Change_list,
                '财富值_美元': Wealth_USD_list,
                '年份': Year_list
            }
        )
    if page == 1:
        header = True
    else:
        header = False

# 保存结果数据
    df.to_csv('2022胡润百富榜.csv', mode='a+', index=False, header=header, encoding='utf_8_sig')
