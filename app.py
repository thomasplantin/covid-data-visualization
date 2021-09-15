from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    req = requests.get('http://apps.who.int/gho/athena/api/GHO/WHOSIS_000001?format=json')
    json_data = json.loads(req.content)
    return render_template("cases.html", data=json_data)

@app.route('/cases', methods=['GET'])
def cases():
    req = requests.get('http://apps.who.int/gho/athena/api/GHO/WHOSIS_000001?format=json')
    json_data = json.loads(req.content)
    return render_template("cases.html", data=json_data)

@app.route('/deaths')
def deaths():
    return render_template("deaths.html")

if __name__ == "__main__":
    app.run(debug=True)