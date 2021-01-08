from flask import Flask

app = Flask(__name__)

@app.route('/')
def label_home():
    return "Time to print some labels"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

