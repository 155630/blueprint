from flask import render_template, Blueprint

search=Blueprint('search',__name__)

def init_search_blue(app):
    app.register_blueprint(search,url_prefix='/search')
    #自定义过滤器
    app.add_template_filter(add,'add')


#自定义过滤器
def add(param1, param2):
    return param1 + param2

class Shop:
    def __init__(self,title,name):
        self.name=name
        self.title=title

@search.route('/temp/')
def temp1():
    return render_template('search/search.html',hello='world',
    li=[1,2,3],dt={'name':'小明','age':18},shop=Shop('手机','华为'))

@search.route('/filt/')
def filter():
    return render_template('search/filter.html')

@search.route('/extend/')
def extends():
    return render_template('extend/extends.html')