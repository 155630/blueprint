from werkzeug.routing import BaseConverter
import datetime

"""
1>第一步 定义自定义转化器类 继承BaseConverter
2>第二步 注册自定义转化器 app.url_map.converters['re']=RegexConverter
3>第三步 使用
"""

class RegexConverter(BaseConverter):

    def __init__(self,url_map,*args):
        super().__init__(url_map)
        self.regex=args[0]

    def to_python(self,value):
        print(value)
        return datetime.datetime.strptime(value,'%Y')