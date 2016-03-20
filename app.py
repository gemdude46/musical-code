from flask import Flask, request, redirect
import os

f = open('index.htm','r')
indexpage = f.read()
f.close()


class server(Flask):
    def __init__(self, *args, **kwargs):
        super(server, self).__init__(*args, **kwargs)

app = server(__name__)

@app.route('/')
def index():
    return indexpage

@app.route('/reboot')
def reboot():
    os.system('( cd /root/musical-code/ && bash restart )')