from flask import Flask
from flask import render_template
from barrel import Store
import json


app = Flask(__name__)
db = Store('http://localhost:8080/source')


@app.template_filter('to_pretty_json')
def to_pretty_json(value):
    return json.dumps(value, sort_keys=True,
                      indent=4, separators=(',', ': '))


@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/source/<docid>')
def get(docid):
    doc = db.get(docid)
    return render_template('get.html', doc=doc)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
