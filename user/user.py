# from flask import render_template,Blueprint,redirect
# from app import app
# from flask import Flask

# html = Blueprint("html",_name_)
#
# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'nickname': 'Miguel'}  # fake user
#     return render_template("index.html",
#                            title='Home',
#                            user=user)


from flask import Blueprint, render_template, redirect

user = Blueprint('user', __name__)


@user.route('/index')
def index():
    return render_template('user/index.html')

