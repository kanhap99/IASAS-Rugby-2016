from flask import Flask
from flask import render_template

app = Flask(__name__);

@app.route('/')
def home():
    return render_template('template.html')
@app.route('/teams/<school>')
def showTeam(school):
    return render_template(school+'.html')
if __name__ == '__main__':
    app.run()
