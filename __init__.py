from flask import Flask
from flask import render_template

app = Flask(__name__);

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/teams/<schoolName>')
def dispTeam(schoolName):
    return render_template('schools/'+schoolName+'.html')
@app.route('/schedule')
def dispSchedule():
    return render_template('schedule.html')
@app.route('/results')
def dispResults():
    return render_template('results.html')
@app.route('/pics/<gender>')
def dispPics(gender):
    return render_template('pics/'+gender+'Pics.html')
@app.route('/stream/<gender>')
def dispStream(gender):
    return render_template('stream/'+gender+'Stream.html')

if __name__ == '__main__':
    app.run()