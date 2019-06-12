#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get():
    return 'hello world again'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
