from application import app, db
from os import getenv
from flask import Flask
#from flask_sqlalchemy import SQLALchemy

#app = Flask(__name__)
if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=5000)

#app. config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"


#db=SQLALchemy(app)


    # Recreate the table schema in the database if environment variable
    # CREATE_SCHEMA is set to "true". Any other value will not recreate
    # the schema.
    #
    # To set the CREATE_SCHEMA value on Linux, run:
    #   export CREATE_SCHEMA=true
    # Recreate the table schema in the database if environment variable
    # CREATE_SCHEMA is set to "true". Any other value will not recreate
    # the schema.
    #
    # To set the CREATE_SCHEMA value on Linux, run:
    #   export CREATE_SCHEMA=true
    
@app.route('/')    
def index():
    session.pop('name', None)
    return '<h1>Chores Home Page!</h1>'


@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['POST', 'GET'])

def chore_home(name):
    session['name'] = name
    db = get_db()
    cur = db.execute('select id, chore_name, location, email from users')
    results = cur.fetchall()

    return render_template('index.html', name=name, display=False,
                           mylist=['one', 'two', 'three', 'four'])  # listofdictionaries=[{'name' :
    # 'Zach'}, {'name' : 'Zoe'}], results=results))


@app.route('/add_chore')
def add_chore():
    if 'name' in session:
        name = session['name']
    else:
        name = 'NotinSession!'
    return add_chore({'key': 'value', 'listkey': [1, 2, 3], 'name': name})


@app.route('/query page')
def Chore_query():
    chore = request.args.get('chore')
    location = request.args.get('location')
    owner_email  =  request.args.get('owner_email')
    return '<h1>chore {}. You are from {}. You are on the Chore page!</h1>'.format(name, location)


@app.route("/theform", methods=['GET', 'POST'])

def theform():
    if getenv("CREATE_SCHEMA") != None:
        if getenv("CREATE_SCHEMA").lower() == "true":
            db.drop_all()
            db.create_all()

    
    
    
    
    
@app.route("/theform",methods=['Get', 'Post'])   
def theform():
    if getenv("CREATE_SCHEMA") != None:
        if getenv("CREATE_SCHEMA").lower() == "true":
            db.drop_all()
            db.create_all()
            
    
    
    
    
    
    
    
    
    
    