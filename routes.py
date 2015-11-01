from flask import Flask

app = Flask(__name__);

@app.route('/')
def hello():
    return render_template("nav.html")

if __name__ == '__main__':
    app.run()
