from application import db 
from application.models import Chore

db.drop_all()
db.create_all() 

testuser = Chore(
chore_description='Hoovering',
charge= 40,job_done='completed') #This is extra section 
#to populates with an example
db. session. add(testuser)
db. session. commit()