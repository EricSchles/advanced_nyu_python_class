from app import app
from app.models import Table
import json
from app import db
from flask import request #this is better

#this should not accept both get and post
@app.route("/", methods=["GET","POST"])
def pull(): #not exactly
    results = [elem.row for elem in Table.query.all()]
    return json.dumps(results)

#this might work?
#request is better
@app.route("/second_route/<code>", methods=["GET","POST"]) #this should not accept both get and post
def push(code):
    table = Table(code)
    db.session.add(table)
    db.session.commit()
    return "success!"
