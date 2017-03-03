#!/usr/bin/env python3
from flask import Flask, request

import subprocess

app = Flask(__name__)
default = ["firejail", "--net=none", "--quiet", "--private=/sandbox"]


@app.route('/c++', methods=['POST', 'PUT'])
def cpp():
    f = subprocess.run(default + ["g++", "-xc++", "-"],
                       input=request.form["code"],
                       stdout=subprocess.PIPE,
                       universal_newlines=True,
                       stderr=subprocess.PIPE)
    if f.returncode != 0:
        return (f.stderr, {'Access-Control-Allow-Origin': '*'})
    else:
        g = subprocess.run(default + ["./a.out"],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
        return (g.stdout, {'Access-Control-Allow-Origin': '*'})


@app.route("/python", methods=['POST', 'PUT'])
def python():
    f = subprocess.run(default + ["python3"],
                       input=request.form["code"],
                       stdout=subprocess.PIPE,
                       universal_newlines=True,
                       stderr=subprocess.STDOUT)
    return (f.stdout, {'Access-Control-Allow-Origin': '*'})


@app.route('/js', methods=['POST', 'PUT'])
def node():
    f = subprocess.run(default + ["nodejs"],
                       input=request.form["code"],
                       stdout=subprocess.PIPE,
                       universal_newlines=True,
                       stderr=subprocess.STDOUT)
    return (f.stdout, {'Access-Control-Allow-Origin': '*'})


@app.route('/bash', methods=['POST', "PUT"])
def bash():
    f = subprocess.run(default + ["bash", "--"],
                       input=request.form["code"],
                       stdout=subprocess.PIPE,
                       universal_newlines=True,
                       stderr=subprocess.STDOUT)
    return (f.stdout, {'Access-Control-Allow-Origin': '*'})


@app.route("/", methods=['GET'])
def help():
    return "http[ie] -f POST /lang-id/ code=@input.py"


application = app

if __name__ == "__main__":
    app.run("0.0.0.0", "8000")
