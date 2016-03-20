from flask import Flask, request, redirect, Response
import os

f = open('index.htm','r')
indexpage = ' '.join(f.read().split())
f.close()

f = open('main.css','r')
maincsspage = ' '.join(f.read().split())
f.close()

class server(Flask):
    def __init__(self, *args, **kwargs):
        super(server, self).__init__(*args, **kwargs)

app = server(__name__)

@app.route('/')
def index():
    return indexpage

@app.route('/main.css')
def main_css():
    return Response(maincsspage,'text/css')

@app.route('/reboot')
def reboot():
    os.system('( cd /root/musical-code/ && bash restart )')
