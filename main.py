from flask import Flask, request, redirect, url_for, render_template
app = Flask('app', root_path='./')

placeholderList = {"userOld": "", "userError": "", "pwdError": "", "emailOld": "", "emailError": ""}

userForm = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 60%;
                font: 16px sans-serif;
                border-radius: 10px;
                text-align: center;
            }}
            label {{
                display:inline-block;
                float: left;
                padding-top: 5px;
                text-align: right;
                width: 35%;
            }}
            input {{
                margin-top: 5px;
                display:inline-block;
                width: 45%
            }}      
        </style>
    </head>
    <body>
      <h1 style="text-align: center"> User Signup </h1>
      <form method="post">
        <label> Username*: </label>
        <input type="text" name="username" minlength="3" maxlength="20" required value="{userOld}"/>
        </br>
        <i>{userError}</i>

        <label> Password*:</label>
        <input type="password" name="pworda" minlength="8" required/>
        </br>
        <i>{pwdError}</i>

        <label> Retype Password*:</label>
        <input type="password" name="pwordb" minlength="8" required/>
        </br>

        <label> Email Address: </label>
        <input type="text" name="email" value="{emailOld}"/>
        </br>
        <i>{emailError}</i>
        </br>

        <input type="submit" value="Signup"/>
      </form>
    </body>
</html>
"""


@app.route("/", methods=['POST'])
def checkInput():

    inUsername = request.form['username']

    inPwdA = request.form['pworda']

    inPwdB = request.form['pwordb']

    inEmail = request.form['email']

    userMsg = ""
    pwdMsg = ""
    emailMsg = ""

    if (inUsername.find(' ') != -1):
      userMsg = "Usernames cannot contain spaces"

    if (inPwdA != inPwdB):
      print("Mismatched Passwords Error")
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

    print(username)

    return render_template('welcome.html', userNm=username)
    #return welcomeForm.format(userNm=username)


@app.route("/")
def index():

    return render_template('index.html', plcList=placeholderList)
    #return userForm.format(userOld="", userError="", pwdError="", emailOld="", emailError="")


app.run()