from flask import Blueprint, render_template

from app.ext import db
from .models import User

user=Blueprint('user',__name__,static_folder='static',template_folder='templates')

def init_user_blue(app):
    app.register_blueprint(user,url_prefix='/user')

@user.route('/index/')
def index():
    #user=User(name='老王',)
    # db.session.add(user)
    # db.session.commit()
    return render_template('index.html',msg='东京热还是武汉热')

@user.route('/find')
def find():
    # user=User.query.get(1)
    # User.query.all()
    # User.query.filter(User.name=='老王').first()
    return render_template('index.html', msg='东京热还是武汉热')