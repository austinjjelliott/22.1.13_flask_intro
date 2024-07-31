from flask import Flask
app = Flask(__name__)

@app.route("/welcome")
def test_welcome():
    return "welcome"

@app.route("/welcome/home")
def test_welcome_home():
    return "welcome home"

@app.route("/welcome/back")
def test_welcome_back():
    return "welcome back"


if __name__ == '__main__':
    app.run(debug=True)