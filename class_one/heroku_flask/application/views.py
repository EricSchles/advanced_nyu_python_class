from application import app
from application.models import Table
import json

@app.route("/")
def index():
    results = [elem.row for elem in Table.query.all()]
    return json.dumps(results)
        
