#/usr/bin/env python
#coding:utf-8

from bottle import route,run
from bottle import template

@route('/login')
def login():
    return template('login')
###这里的login是一个login.tpl前端页面，这里加载不用去加后缀名
run(host='127.0.0.1',port=8080,debug=True)


