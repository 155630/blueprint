from flask import Blueprint, render_template, abort, request
import logging

home=Blueprint('home',__name__)

def init_home_blue(app):
    app.register_blueprint(home,url_prefix='/home')

@home.route('/')
def index():
    return '默认首页'

# post 增, get 查, put 更新, delete 删除
@home.route('/method/',methods=['post','get','put','delete'])
def method(year):
    return '限制请求方式'

@home.route('/<re("\d{4}"):year>/')
def converter(year):
    logging.info(year)
    print(year)
    return '自定义转化器'

@home.route('/test/ ')
def test1():
    return '带/ 和 不带/ 的区别'


"""
#全局错误处理
"""

@home.route('/1/')
def test2():
    if request.method=='POST':
        pass  #添加正确代码
    else:
        return abort(404)
        #return abort(400)

#定义两个路由,由abort后面参数匹配对应参数
@home.errorhandler(404)
@home.errorhandler(400)
def error(e):
    if e.code==404:
        return render_template('error/404.html')
    elif e.code==400:
        return render_template('error/400.html')