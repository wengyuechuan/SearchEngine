"""
    构建一个简单的搜索引擎
"""
import jieba
import pymongo
import re

client = pymongo.MongoClient()
db = client['searchEngine']
collection = db['paper']
Collection_data = list(collection.find())


class SearchEngineBase:
    def __init__(self):
        self.index = {}  # 构建一个空索引
        self.data = []  # 构建一个空数据集

    def split_words(self):
        self.split_sentence_to_words()
        self.split_key_words()
        self.split_institute()

    def split_sentence_to_words(self):
        """ 分词功能 """
        for item in self.data:
            item['title'] = list(jieba.cut(item['title']))
            item['abstract'] = list(jieba.cut(item['abstract']))

    def split_key_words(self):
        """ 对数据库当中每一项的keywords进行处理 """
        for item in self.data:
            item['keywords'] = item['keywords'].split(';')

    def split_institute(self):
        """ 对数据库当中的每一项的institute进行处理 """
        for item in self.data:
            item['institute'] = re.findall(r'(?:\d+\.)?([a-zA-Z]+)', item['institute'])

    def create_index(self):
        """ 创建索引 """
        # 2. 建立索引
        for item in self.data:
            for word in item['title']:
                if word not in self.index:
                    self.index[word] = []
                self.index[word].append(item['id'])
            for word in item['abstract']:
                if word not in self.index:
                    self.index[word] = []
                self.index[word].append(item['id'])
            for word in item['keywords']:
                if word not in self.index:
                    self.index[word] = []
                self.index[word].append(item['id'])
            for word in item['institute']:
                if word not in self.index:
                    self.index[word] = []
                self.index[word].append(item['id'])

    def search(self, query):
        """ 搜索功能 """
        # 1. 分词
        query_words = list(jieba.cut(query))
        # 2. 查询
        result = set()
        for word in query_words:
            if word in self.index:
                result.update(self.index[word])
        # 3. 返回结果
        result1 = []

        for index in result:
            result1.append(collection.find({'id': index})[0])

        return result1


if __name__ == '__main__':
    search_engine = SearchEngineBase()
    search_engine.data = Collection_data
    search_engine.split_words()
    search_engine.create_index()

    query1 = "广东"
    result1 = search_engine.search(query1)

    result = []

    for index in result1:
        result.append(collection.find({'id': index})[0])

    for i in result:
        print(result)