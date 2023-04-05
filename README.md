# 简单搜索引擎的构建

Author: 翁岳川 刘宇涵 杨瑞旭 熊浩然

利用倒排索引进行构建，实现了对中文的搜索。

其中利用了jieba进行分词，使用数据库为MongoDB

## 使用方法

1. 依赖
```bash
pip install flask
pip install jieba
pip install pymongo
pip install flask_cors
```

2. 将data当中的xlsx文件导入到数据库当中
   1. 调整script.py当中对MongoDB的地址，以及数据库名，以及collection名，账号密码等，全部需要进行调整‘
   2. 运行script.py，将数据导入数据库，完成数据集的构建

3. 运行服务器
   1. 运行app.py文件，即可使用服务
