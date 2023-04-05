"""
    将一个文件夹当中的数据全部存储到mongoDB数据库
"""
import os
from pymongo import MongoClient
import pandas as pd

# 连接MongoDB数据库（默认主机和端口，无密码认证）
client = MongoClient()

# 选择要存储数据的数据库和集合
db = client['searchEngine']
collection = db['paper']

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
# 待处理文件夹路径
folder_path = 'data'

path = os.path.join(dir_path, folder_path)

# 遍历文件夹中的所有XLSX文件，读取数据并存入MongoDB数据库
count = 1
for filename in os.listdir(path):
    if filename.endswith('.xlsx'):
        # 读取XLSX文件数据
        filepath = os.path.join(folder_path, filename)
        data = pd.read_excel(filepath)
        # 将数据转换为字典格式，并插入MongoDB数据库
        records = data.to_dict('records')
        for record in records:
            record['id'] = count
            count += 1
        collection.insert_many(records)