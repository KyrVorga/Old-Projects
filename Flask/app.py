from flask import Flask, render_template, request, redirect, url_for
import classes.accounts
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("home.html")

@app.route('/accounts')
def Accounts(method=["GET", "POST"]):

    form = classes.accounts.AccountForm(request.form)

    return render_template("accounts.html", form=form)




app.run(debug=True)