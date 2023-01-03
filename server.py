from flask import Flask
import json
from mock_data import catalog

app = Flask("server")

@app.get("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "this is another endpoint"


@app.get("/about")
def about():
    return "Top Fun USA"

# ##############################CATALOG API#######################
# ###############################################################

@app.get("/api/version")
def version():
    version = {
        "V":"V.1.0.1",
        "name":"Candy firewall",
    }
    return json.dumps(version)

@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)

@app.get('/test/numbers')
def get_numbers():
    # create a list with numbers from 1 to 20
    # except 13 and 17
    # and return the list as json
    result = []
    for n in range(1,21):
        if n != 13 and n != 17:
            result.append(n)

    return json.dumps(result)

   

app.run(debug=True)
