import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.
                                     #The value should be set in Heroku (Settings->Config Vars).
                                     #To run locally, set in env.sh and include that file in gitignore so the secret key is not made public.

@app.route('/')
def renderhome():
    session.clear()
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderhome')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
        return render_template('page1.html')

@app.route('/page2',methods=['POST'])
def renderPage2():
    if not "1FRIENDSNAME" in session:
        session["1FRIENDSNAME"]=request.form['1FRIENDSNAME']
        return render_template('page2.html')
    else:
        render_template('page2.html')


@app.route('/page3',methods=['POST'])
def renderPage3():
    if not "2NUMBER" in session:
        session["2NUMBER"]=request.form['2NUMBER']
        return render_template('page3.html')
    else:
        render_template('page3.html')

@app.route('/page4',methods=['POST'])
def renderPage4():
    if not "3VEHICLE" in session:
        session["3VEHICLE"]=request.form['3VEHICLE']
        return render_template('page4.html')
    else:
        render_template('page4.html')

@app.route('/page5',methods=['POST'])
def renderPage5():
    if not "4AJECTIVE" in session:
        session["4AJECTIVE"]=request.form['4AJECTIVE']
        return render_template('page5.html')
    else:
        render_template('page5.html')

@app.route('/page6',methods=['POST'])
def renderPage6():
    if not "5AJECTIVE" in session:
        session["5AJECTIVE"]=request.form['5AJECTIVE']
        return render_template('page6.html')
    else:
        render_template('page6.html')

@app.route('/page7',methods=['POST'])
def renderPage7():
    if not "6INGVERB" in session:
        session["6INGVERB"]=request.form['6INGVERB']
        return render_template('page7.html')
    else:
        render_template('page7.html')

@app.route('/page8',methods=['POST'])
def renderPage8():
    if not "7ANIMAL" in session:
        session["7ANIMAL"]=request.form['7ANIMAL']
        return render_template('page8.html')
    else:
        render_template('page8.html')

@app.route('/page9',methods=['POST'])
def renderPage9():
    if not "8AJECTIVE" in session:
        session["8AJECTIVE"]=request.form['8AJECTIVE']
        return render_template('page9.html')
    else:
        render_template('page10.html')

@app.route('/page10',methods=['POST'])
def renderPage10():
    if not "9PASTTENSEVERB" in session:
        session["9PASTTENSEVERB"]=request.form['9PASTTENSEVERB']
        return render_template('page10.html')
    else:
        render_template('page11.html')

@app.route('/page11',methods=['POST'])
def renderPage11():
    if not "10AJECTIVE" in session:
        session["10AJECTIVE"]=request.form['10AJECTIVE']
        return render_template('page11.html')
    else:
        render_template('page12.html')

@app.route('/page12',methods=['POST'])
def renderPage12():
    if not "11NOUN" in session:
        session["11NOUN"]=request.form['11NOUN']
        return render_template('page12.html')
    else:
        render_template('page13.html')

@app.route('/page13',methods=['POST'])
def renderPage13():
    if not "12PASTTENSEVERB" in session:
        session["12PASTTENSEVERB"]=request.form['12PASTTENSEVERB']
        return render_template('page13.html')
    else:
        render_template('page14.html')

@app.route('/page14',methods=['POST'])
def renderPage14():
    if not "13PASTVERB" in session:
        session["13PASTTENSEVERB"]=request.form['13PASTTENSEVERB']
        return render_template('page14.html')
    else:
        render_template('page15.html')

@app.route('/page15',methods=['POST'])
def renderPage15():
    if not "14PLACE" in session:
        session["14PLACE"]=request.form['14PLACE']
        return render_template('page15.html')
    else:
        render_template('page15.html')

@app.route('/page16',methods=['POST'])
def renderPage16():
    if not "15VERB" in session:
        session["15VERB"]=request.form['15VERB']
        return render_template('page16.html')
    else:
        render_template('page16.html')

#########

@app.route('/results',methods=['POST'])
def renderResults():
        session["RESULTS1"]=request.form['RESULTS1']
        return render_template('results.html')

@app.route('/results2',methods=['POST'])
def renderResults2():
        session["RESULTS2"]=request.form['RESULTS2']
        return render_template('results2.html')

@app.route('/results3',methods=['POST'])
def renderResults3():
        session["RESULTS3"]=request.form['RESULTS3']
        return render_template('results3.html')

@app.route('/results4',methods=['POST'])
def renderResults4():
        session["RESULTS4"]=request.form['RESULTS4']
        return render_template('results4.html')

if __name__=="__main__":
    app.run(debug=False)
