import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hi'


@app.route('/data')
def data_route():
    with open('../day1/example.json') as f:
        return json.load(f)
    
if __name__ =='__main__':
    app.run(debug=True)
