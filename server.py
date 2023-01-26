from flask import Flask, request
import json
from mock_data import catalog
from config import db
from flask_cors import CORS
# db is a variable that reflects the database

app = Flask("server")
CORS(app) #disable CORS to allow requests from any origin


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
    cursor = db.products.find({})
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"]) #fix _id issue
        results.append(prod)

    return json.dumps(results)



#save products
@app.post("/api/catalog")
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

    product["_id"] = str(product["_id"]) # clean the ObjectId('asd') from the obj

    return json.dumps(product)


# get all products that belong to a category
@app.get("/api/catalog/<category>")
def get_by_category(category):
    cursor = db.products.find({"category": category})
    #create a list, travel the cursor fix the _id, add it to the list
    #return th list as json
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        results.append(prod)

    return json.dumps(results)


@app.get("/api/catalog/search/<title>")
def search_by_title(title):
    cursor = db.products.find({"title": {"$regex": title,"$options": "i"}})
    results = []
    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        results.append(prod)

    return json.dumps(results)

@app.get('/api/product/cheaper/<price>')
def search_by_price(price):
    # travel the cursor instead of catalog
    cursor = db.products.find({})
    result = []
    for prod in cursor:
        if prod["price"] < float(price):
            prod["_id"] = str(prod["_id"])
            result.append(prod)

    return json.dumps(result)

@app.get("/api/product/cheapest")
def get_cheapest():
    cursor = db.products.find({})
    answer = cursor[0]
    for prod in cursor:
        if prod["price"] < answer["price"]:
            answer = prod

    answer["_id"] = str(answer["_id"])
    return json.dumps(answer)

# create a get endpoint that returns the number of products in the catalog 
@app.get("/api/product/count")
def count_products():
    count = db.products.count_documents({})
    return json.dumps(count)
  
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
