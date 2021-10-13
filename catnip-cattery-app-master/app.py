from functools import wraps

from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)

import classes.forms
from classes.cat import Cat
from classes.user import User
from config import Config

config = Config()

app = Flask(__name__)

app.secret_key = config.secret_key






def is_logged_in(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:  
            return f(*args,**kwargs)
        else:
            flash('Unauthorised access. Please log in.', 'danger')
            return redirect(url_for('login'))
                 
    return wrap







# Endpoint name: Current cats
# Parameters received: None
# Purpose of function: displays the page of cats currently in the cattery
# Parameters returned: render_template

@app.route('/currentCats')
@is_logged_in   
def currentCats():
    
    cat = Cat()

    currentCats = cat.retrieveCurrentCats()

    if currentCats:
        return render_template("currentCats.html", currentCats = currentCats)
    else:
        flash('Something went wrong or there were no cats',"danger")
        return render_template('home.html')

    return render_template('currentCats.html')






# Endpoint name: Home
# Parameters received: None
# Purpose of function: Display home page
# Parameters returned: render_template

@app.route('/')
@is_logged_in   
def home():

    return render_template('home.html')







# Endpoint name: All cats
# Parameters received: None
# Purpose of function: Display all cats page
# Parameters returned: render_template

@app.route('/allCats')
@is_logged_in   
def allCats():
    
    cat = Cat()

    allCats = cat.retrieveAllCats()

    if allCats:
        return render_template("allCats.html", allCats = allCats)
    else:
        flash('Something went wrong or there were no cats',"danger")
        return render_template('home.html')

    return render_template('allCats.html')






# Endpoint name: All owners
# Parameters received: None
# Purpose of function: Display all owners page
# Parameters returned: render_template

@app.route('/allOwners')
@is_logged_in   
def allOwners():
    
    cat = Cat()
    allOwners = cat.retrieveAllOwners()
    
    if allOwners:
        return render_template("allOwners.html", allOwners = allOwners)
    else:
        flash('Something went wrong or there were no Owners',"danger")
        return render_template('home.html')

    return render_template('allOwners.html')







# Endpoint name: Delete cat
# Parameters received: catId
# Purpose of function: deletes cat from database
# Parameters returned: redirect

@app.route("/deleteCat/<string:catId>")
def catDelete(catId):

    cat = Cat()

    success = cat.deleteCat(catId)
    if success:
        flash('The Cat has been deleted', "success")

    else:
        flash("A problem occured. Unable to delete", "danger") 
    
    return redirect(url_for('allCats'))







# Endpoint name: delete owner
# Parameters received: ownerId
# Purpose of function: Deletes owner from database
# Parameters returned: redirect

@app.route("/deleteOwner/<string:ownerId>")
def ownerDelete(ownerId):

    cat = Cat()

    success = cat.deleteOwner(ownerId)
    if success:
        flash('The Owner and their cats have been deleted', "success")

    else:
        flash("A problem occured. Unable to delete", "danger") 
    
    return redirect(url_for('allOwners'))








# Endpoint name: remove cat
# Parameters received: catId
# Purpose of function: removes cat from current cats page
# Parameters returned: redirect

@app.route("/removeCat/<string:catId>")
def catremove(catId):

    cat = Cat()

    success = cat.removeCat(catId)
    if success:
        flash('The Cat has been removed from the cattery', "success")

    else:
        flash("A problem occured. Unable to remove from the cattery", "danger") 
    
    return redirect(url_for('currentCats'))








# Endpoint name: add cat
# Parameters received: catId
# Purpose of function: adds cat into the current cats page
# Parameters returned: redirect

@app.route("/addCat/<string:catId>")
def catAdd(catId):
    cat = Cat()

    success = cat.addCat(catId)
    if success:
        flash('The Cat has been added to the cattery', "success")

    else:
        flash("A problem occured. Unable to add to cattery", "danger") 
    
    return redirect(url_for('allCats'))









# Endpoint name: edit cat
# Parameters received: catId, new cat form
# Purpose of function: display edit cat page
# Parameters returned: render_template, redirect

@app.route("/editCat/<string:catId>", methods=["GET", "POST"])
def catEdit(catId):

    cat = Cat()
    owners = cat.getOwners()

    form = classes.forms.NewCatForm(request.form)
    form.catOwner.choices = owners

    if request.method == "POST" and form.validate():
         
        catName = form.catName.data
        catOwner = form.catOwner.data
        catMedication = form.catMedication.data
        catMedicationDetails = form.catMedicationDetails.data
        catDiet = form.catDiet.data
        catLikesDislikes = form.catLikesDislikes.data
        catBehaviour = form.catBehaviour.data
        catBehaviourDetails = form.catBehaviourDetails.data
        catOther = form.catOther.data
        catDepatureDate = form.catDepatureDate.data

        cat = Cat()
        success = cat.editCat(catName, catOwner, catMedication, catMedicationDetails, catDiet, catLikesDislikes, catBehaviour, catBehaviourDetails, catOther, catDepatureDate, catId) #ownerName, ownerAddress, ownerPhoneNumber, ownerEmail, 

        if success:
            flash('Cat updated',"success")
        else:
            flash("something went wrong", 'danger')

    else:

        catDetails = cat.retrieveSingleCat(catId)

        if catDetails:

            form.catName.data = catDetails['Name']
            form.catOwner.data = catDetails['Owner']
            form.catMedication.data = catDetails['medicationYN']
            form.catMedicationDetails.data = catDetails['MedicationDetails']
            form.catDiet.data = catDetails['Diet']
            form.catLikesDislikes.data = catDetails['LikesDislikes']
            form.catBehaviour.data = catDetails['BehaviourYN']
            form.catBehaviourDetails.data = catDetails['BehaviourDetails']
            form.catOther.data = catDetails['Other']
            form.catDepatureDate.data = catDetails['DateLeaving']

            return render_template('newCat.html', form=form)
        else:
            flash("there was a problem","danger")

    return redirect(url_for('allCats'))








# Endpoint name: Edit owner
# Parameters received: ownerId, Register form
# Purpose of function: display edit owner page
# Parameters returned: render_template, redirect

@app.route("/editOwner/<string:ownerId>", methods=["GET", "POST"])
def ownerEdit(ownerId):
    
    form = classes.forms.NewOwnerForm(request.form)
    cat = Cat()
    if request.method == "POST" and form.validate():
               
        ownerName = form.ownerName.data
        ownerAddress = form.ownerAddress.data
        ownerPhoneNumber = form.ownerPhoneNumber.data
        ownerEmail = form.ownerEmail.data

        cat = Cat()
        success = cat.editOwner(ownerName, ownerAddress, ownerPhoneNumber, ownerEmail,ownerId) 
        
        if success:
            flash('Owner updated',"success")
        else:
            flash("something went wrong", 'danger')

    else:

        ownerDetails = cat.retrieveSingleOwner(ownerId)
        
        if ownerDetails:

            form.ownerName.data = ownerDetails['name']
            form.ownerAddress.data = ownerDetails['address']
            form.ownerPhoneNumber.data = ownerDetails['phoneNumber']
            form.ownerEmail.data = ownerDetails['email']

            return render_template('newOwner.html', form=form)
        else:
            flash("there was a problem","danger")

    return redirect(url_for('allOwners'))






# Endpoint name: Register
# Parameters received: Register form
# Purpose of function: Diplay register page
# Parameters returned: render_template, redirect

@app.route("/register", methods=["GET", "POST"])
def register():

    form = classes.forms.RegisterForm(request.form)

    if request.method == "POST" and form.validate():

        username = form.username.data
        email = form.email.data
        password = form.password.data

        user= User()
        success = user.insertUser(username,password,email)

        if success:
            flash("You have now registered.","success")
            return redirect(url_for("login"))
        else:
            flash("This user already exists.", "danger")
            return redirect(url_for("register"))

    
    return render_template("register.html", form=form)






# Endpoint name: Login
# Parameters received: Login form
# Purpose of function: Display Login page
# Parameters returned: render_template, redirect

@app.route("/login", methods=["GET", "POST"])
def login():
    
    form = classes.forms.LoginForm(request.form)

    if request.method == "POST" and form.validate():

        username = form.username.data
        passwordAttempt = form.password.data

        user = User()
        auth = user.authenticateUser(username, passwordAttempt)

        if auth:

            session['logged_in'] = True
            session['username'] = username
            session['user_id'] = auth       



            flash("You are now logged in "+username+".","success")
            return redirect(url_for("home", name=username))

        else:

            error = "Incorrect username or password."
            return render_template("login.html",form=form, error=error)

    return render_template("login.html", form=form)








# Endpoint name: New cat
# Parameters received: new cat form
# Purpose of function: displays a page to allow user to enter new cats into database
# Parameters returned: render_template, redirect

@app.route("/newCat", methods=["GET", "POST"])
@is_logged_in
def newCat():


    cat = Cat()
    owners = cat.getOwners()

    form = classes.forms.NewCatForm(request.form)
    form.catOwner.choices = owners


    if request.method == "POST" and form.validate():

        catName = form.catName.data
        catOwner = form.catOwner.data
        catMedication = form.catMedication.data
        catMedicationDetails = form.catMedicationDetails.data
        catDiet = form.catDiet.data
        catLikesDislikes = form.catLikesDislikes.data
        catBehaviour = form.catBehaviour.data
        catBehaviourDetails = form.catBehaviourDetails.data
        catOther = form.catOther.data
        catDepatureDate = form.catDepatureDate.data


        cat = Cat()
        success = cat.addNewCat(catName, catOwner, catMedication, catMedicationDetails, catDiet, catLikesDislikes, catBehaviour, catBehaviourDetails, catOther, catDepatureDate)

        if success:

            flash("Cat entered", "success")            
            return redirect(url_for("home"))

            
        else:
            flash("A problem occured.", "danger")

    
    return render_template("newCat.html", form=form)








# Endpoint name: 
# Parameters received: new owner form
# Purpose of function: Display a page for entering new owners into Database
# Parameters returned: render_template, redirect

@app.route("/newOwner", methods=["GET", "POST"])
@is_logged_in
def newOwner():

    form = classes.forms.NewOwnerForm(request.form)

    if request.method == "POST" and form.validate():

        ownerName = form.ownerName.data
        ownerAddress = form.ownerAddress.data
        ownerPhoneNumber = form.ownerPhoneNumber.data
        ownerEmail = form.ownerEmail.data

        
        cat = Cat()
        success = cat.addNewOwner(ownerName, ownerAddress, ownerPhoneNumber, ownerEmail)

        if success:
            flash("Owner entered", "success")
            return redirect(url_for("home"))
        else:
            flash("A problem occured.", "danger")

    
    return render_template("newOwner.html", form=form)








# Endpoint name: Logout
# Parameters received: None
# Purpose of function: Logs user out
# Parameters returned: redirect
 
@app.route("/logout")
@is_logged_in   
def logout():

    session.clear()
    flash("You are now logged out", "success")
    return redirect(url_for("login"))




@app.errorhandler(404)
def page_not_found(e):

    #app.logger.info(e) #"404 encountered"
    return render_template("errors/404.html")





if __name__ == "__main__":

    app.run(debug=True)
