from flask import Flask, jsonify, make_response
from flask import request
import socket   
import subprocess

app = Flask(__name__)

@app.route('/', methods=['POST'])
def sub_process():
   subprocess.Popen(['python3','stress_cpu.py'],shell=True)
   data = {'message': 'Done', 'code': 'SUCCESS'}
   return make_response(jsonify(data), 200)

@app.route('/', methods=['GET'])
def get_host():
   return socket.gethostname()

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=5000)
