from flask import Flask, request
import os

import subprocess

app = Flask(__name__)

@app.route('/c++', methods=['POST', 'PUT'])
def cpp():
    code = request.form["code"]
    name = str(hash(code))

    f = subprocess.run(["g++", "-xc++", "-o", name, "-"], input=code, stdout=subprocess.PIPE, encoding="utf-8", stderr=subprocess.PIPE)
    if f.returncode != 0:
        return (f.stderr, {'Access-Control-Allow-Origin': '*'})
    else:
        g = subprocess.run(["./{}".format(name)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return (g.stdout, {'Access-Control-Allow-Origin': '*'})

@app.route("/python", methods=['POST', 'PUT'])
def python():
    f = subprocess.run(["python"], input=request.form["code"], stdout=subprocess.PIPE, encoding="utf-8", stderr=subprocess.STDOUT)
    if f.returncode != 0:
        return (f.stderr, {'Access-Control-Allow-Origin': '*'})
    else:
        return (f.stdout, {'Access-Control-Allow-Origin': '*'})

@app.route("/", methods=['GET'])
def help():
    return "http[ie] -f POST /lang-id/ code=@input.py"

app.run(host='0.0.0.0', port=int(os.getenv("PORT")))
