from flask import Flask, request, redirect, url_for, render_template
app = Flask('app', root_path='./')

placeholderList = {"userOld": "", "userError": "", "pwdError": "", "emailOld": "", "emailError": ""}


@app.route("/", methods=['POST'])
def checkInput():

    inUsername = request.form['username']

    inPwdA = request.form['pworda']

    inPwdB = request.form['pwordb']

    inEmail = request.form['email']

    userMsg = ""
    pwdMsg = ""
    emailMsg = ""

    # Flask seems to do validation for input length, and displays related errors

    if (inUsername.find(' ') != -1):
      userMsg = "Usernames cannot contain spaces"

    if (inPwdA != inPwdB):
      pwdMsg += "Passwords must match"
    elif (inEmail.find(' ') != -1):
      if (pwdMsg != ""):
          pwdMsg += "; "
      pwdMsg = "Passwords cannot contain spaces"

    if (inEmail != ""):
        if ((inEmail.find('@') != inEmail.rfind('@'))
                or (inEmail.find('@') == -1)):
            emailMsg += "Emails must have an '@'"
        elif ((inEmail.find('.') != inEmail.rfind('.'))
              or (inEmail.find('.') == -1)):
            if (emailMsg != ""):
                emailMsg += "; "
            emailMsg += "Emails must have a '.'"
        elif (inEmail.find(' ') != -1):
            if (emailMsg != ""):
                emailMsg += "; "
            emailMsg += "Emails cannot contains spaces"
        elif ((len(inEmail) < 3) or (len(inEmail) > 20)):
            if (emailMsg != ""):
                emailMsg += "; "
            emailMsg += "Emails must be between 3 and 20 characters"

    if (userMsg == "" and pwdMsg == "" and emailMsg == ""):
        return render_template('welcome.html', userNm=inUsername)
    else:
        placeholderList['userOld'] = inUsername
        placeholderList['userError'] = userMsg
        placeholderList['pwdError'] = pwdMsg
        placeholderList['emailOld'] = inEmail
        placeholderList['emailError'] = emailMsg

        return render_template('index.html', plcList=placeholderList)


@app.route('/welcome/<username>')
def welcome(username):

    return render_template('welcome.html', userNm=username)


@app.route("/")
def index():

    return render_template('index.html', plcList=placeholderList)


app.run()