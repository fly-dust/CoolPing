from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get/')
def get():
    # 读取csv文件最新数据
    with open("pinglog.csv") as csvfile:
        mLines = csvfile.readlines()

    targetLine = mLines[-1]
    x = targetLine.split(',')[0]
    y = targetLine.split(',')[1]
    b = [int(x), int(y)]

    return jsonify(b)


if __name__ == '__main__':
    app.run(debug=True)

