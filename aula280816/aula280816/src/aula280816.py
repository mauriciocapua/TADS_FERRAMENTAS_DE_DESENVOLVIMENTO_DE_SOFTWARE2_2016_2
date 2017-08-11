# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! <a href='http://localhost/5000/horadoshow/'> Ir para hora do show>"



@app.route("/horadoshow")
def horadoshow():
    return "como eh que nao vai da"

if __name__ == "__main__":
    app.run()
