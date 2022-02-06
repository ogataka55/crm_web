from flask import Flask, render_template

app = Flask(__name__)

"""
書くこと
    /index で GETリクエスト がきたら
    index.html というテンプレートをレンダリングする
"""


@app.route("/index")
def index():
    customers = [["Bob", 15],
                 ["tom", 57],
                 ["Ken", 73]]

    return render_template("index.html", customers=customers)


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
