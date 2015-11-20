from flask import Flask
from flask import render_template

app = Flask(__name__);

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/teams/<school>')
def showTeam(school):
    return 'Welcome to JIS '+ str(school)


if __name__ == '__main__':
    app.run()
