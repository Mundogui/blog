from flask import Flask, render_template  

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello world Guilherme"

@app.route("/meucontato")
def meuContato():
    return render_template('index.html')