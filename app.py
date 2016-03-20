from flask import Flask, request, redirect, Response
import os, random

f = open('index.htm','r')
indexpage = ' '.join(f.read().split())
f.close()

f = open('main.css','r')
maincsspage = ' '.join(f.read().split())
f.close()

f = open('instructions.htm','r')
instructionspage = ' '.join(f.read().split())
f.close()

f = open('create.htm','r')
createpage = ' '.join(f.read().split())
f.close()

f = open('join.htm','r')
joinpage = ' '.join(f.read().split())
f.close()

f = open('instructions.htm','r')
instructionspage = ' '.join(f.read().split())
f.close()

class server(Flask):
    def __init__(self, *args, **kwargs):
        super(server, self).__init__(*args, **kwargs)

app = server(__name__)

@app.route('/')
def index():
    return indexpage

@app.route('/instructions')
def instructions():
    return instructionspage

@app.route('/create')
def create():
    return createpage

@app.route('/join')
def join():
    return joinpage

@app.route('/getcode')
def getcode():
    code = ''
    for i in range(6):
        code += random.choice('QWERTYUIOPASDFGHJKLZXCVBNM')
    return code

@app.route('/getcodelong')
def getcodelong():
    code = ''
    for i in range(6):
        code += getcode()
    return code

@app.route('/getplayercount')
def getplayercount():
    return '1'

@app.route('/favicon.ico')
def favicon():
    f = open('favicon.ico','rb')
    c = f.read()
    f.close()
    return Response(c, mimetype='image/x-icon')

@app.route('/main.css')
def main_css():
    return Response(maincsspage, mimetype='text/css')

@app.route('/reboot')
def reboot():
    os.system('( cd /root/musical-code/ && bash restart )')
