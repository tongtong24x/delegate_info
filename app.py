from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/compute")
def compute():
    
    return f"<p>my sum is 0</p>"


if __name__=="__main__":
    app.run()