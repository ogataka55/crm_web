import flask as Flask

app = Flask(__name__)

if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
