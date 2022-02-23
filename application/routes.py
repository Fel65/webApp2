from application import app, db
from application.models import Chore
from flask import render_template, request,url_for, redirect
from application.forms import ChoreForm

@app.route('/')
def home():
    all_chores = Chore.query.all()
    return render_template("index.html", all_chores = all_chores, title="Home")


@app.route('/create_chore', methods= ["GET","POST"])
def create_chore():
    form = ChoreForm()
    
    if request.method == "POST":
    
        new_chore = Chore(
            description=form.description.data,
            charge=form.description.data, 
            address=form.description.data,
            Job_done=form.description )
        
        db.session.add(new_chore)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("layout.html", title="Add a Chore", form=form)


