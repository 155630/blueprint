from flask import Flask
from app.ext import config_db, init_ext
from app.home.converter import RegexConverter
from app.home.views import home, init_home_blue
from app.search.views import init_search_blue
from app.user.views import user, init_user_blue

#实例化flask对象
app=Flask(__name__)
app.debug=True
#注册自定义转化器
app.url_map.converters['re']=RegexConverter

def get_app():
    register_blue()
    init_ext(app)
    return app

def register_blue():
    init_user_blue(app)
    init_home_blue(app)
    init_search_blue(app)
