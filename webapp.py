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
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    session["1FRIENDSNAME"]=request.form['1FRIENDSNAME']
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    session["2NUMBER"]=request.form['2NUMBER']
    return render_template('page3.html')

@app.route('/page4',methods=['GET','POST'])
def renderPage3():
    session["3VEHICLE"]=request.form['3VEHICLE']
    return render_template('page4.html')

@app.route('/page5',methods=['GET','POST'])
def renderPage3():
    session["4AJECTIVE"]=request.form['4AJECTIVE']
    return render_template('page5.html')

@app.route('/page6',methods=['GET','POST'])
def renderPage3():
    session["5AJECTIVE"]=request.form['5AJECTIVE']
    return render_template('page6.html')

@app.route('/page7',methods=['GET','POST'])
def renderPage3():
    session["6INGVERB"]=request.form['6INGVERB']
    return render_template('page7.html')

@app.route('/page8',methods=['GET','POST'])
def renderPage3():
    session["7ANIMAL"]=request.form['7ANIMAL']
    return render_template('page8.html')

@app.route('/page9',methods=['GET','POST'])
def renderPage3():
    session["8AJECTIVE"]=request.form['8AJECTIVE']
    return render_template('page9.html')

@app.route('/page10',methods=['GET','POST'])
def renderPage3():
    session["9PASTTENSEVERB"]=request.form['9PASTTENSEVERB']
    return render_template('page10.html')

@app.route('/page11',methods=['GET','POST'])
def renderPage3():
    session["10AJECTIVE"]=request.form['10AJECTIVE']
    return render_template('page11.html')

@app.route('/page12',methods=['GET','POST'])
def renderPage3():
    session["11NOUN"]=request.form['11NOUN']
    return render_template('page12.html')

@app.route('/page13',methods=['GET','POST'])
def renderPage3():
    session["12PASTTENSEVERB"]=request.form['12PASTTENSEVERB']
    return render_template('page13.html')

@app.route('/page14',methods=['GET','POST'])
def renderPage3():
    session["13PASTTENSEVERB"]=request.form['13PASTTENSEVERB']
    return render_template('page14.html')

@app.route('/page15',methods=['GET','POST'])
def renderPage3():
    session["14PLACE"]=request.form['14PLACE']
    return render_template('page15.html')

    @app.route('/results',methods=['GET','POST'])
    def renderPage3():
        session["15VERB"]=request.form['15VERB']
        return render_template('results.html')

if __name__=="__main__":
    app.run(debug=False)
