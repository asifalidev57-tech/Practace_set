from flask import Flask, render_template , request, jsonify

app=Flask(__name__)
items = [

    {
        "id":1,
        "name":"Ali"
    },
    {
        "id":2,
        "name":"Asif"
    }

    ]
@app.route("/")
def home():
    return "welcome to the home page"

@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)



#creating new task
@app.route("/items", methods=['POST'])
def creat_item():
    if not request.json or 'name'not in request.json:
        return jsonify({"error": "error not found"})
    new_item={
        "id":items[-1]['id'] +1 if items else 1,
        "name":request.json["name"]
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route("/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id), None)
    if item is None:
        return jsonify({"error":"Item not found"})
    else:
        return jsonify(item)



if __name__== '__main__':
    app.run(debug=True)