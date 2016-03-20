from flask import Flask, request, redirect
import os

class server(Flask):
    def __init__(self, *args, **kwargs):
        super(server, self).__init__(*args, **kwargs)

app = server(__name__)

@app.route('/reboot')
def reboot():
    os.system('( cd /root/musical-code/ && bash restart )')
