from flask import Flask
from flask import render_template

app = Flask(__name__);

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/teams/<school>')
def dispTeam(school):
    return render_template(school+'.html')
@app.route('/schedule')
def dispSchedule():
    return render_template('schedule.html')
@app.route('/results/<resultGender>')
def dispResults(resultGender):
    return render_template(resultGender+'Results.html')
if __name__ == '__main__':
    app.run()
