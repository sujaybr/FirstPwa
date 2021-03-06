from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/err")
def error():
    return app.send_static_file("error.html")

@app.route('/sw.js')
def sw():
    return app.send_static_file('sw.js')

if __name__ == "__main__":
    app.run(debug = True)
