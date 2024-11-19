import pickle
# we are going to use the Flask micro web framework
from flask import Flask, request, jsonify

app = Flask(__name__) # pass in name of program


def load_module():
    # unpickle header and tree in tree.p 
    infile = open("tree.p", "rb")
    header, tree = pickle.load(infile) # unpack tuple back into header and tree
    infile.close()
    return header, tree

def tdidt_predict(header, tree, instance):
    info_type = tree[0]
    if info_type == "Leaf":
        return tree[1] # label
    att_index = header.index(tree[1])
    for i in range(2, len(tree)):
        value_list = tree[i]
        if value_list[1] == instance[att_index]:
            return tdidt_predict(header, value_list[2], instance)
        
# we need to add some routes!
# a "route" is a function that handles a request
# e.g for the HTML content for a home page
# or for the JSON response for a /predict API endpoint, etc
@app.route("/") # / is root page
def index(): 
    # return content and status code
    return "<h1>Welcome to the interview predictor app</h1>", 200

# lets add a route for the /predict endpoint
@app.route("/predict")
def predict(): 
    # lets parse the unseen instance values from the query string
    # they are in the request object
    level = request.args.get("level") # defaults to None
    lang = request.args.get("lang") # defaults to None
    tweets = request.args.get("tweets") # defaults to None
    phd = request.args.get("phd")# defaults to None
    instance = [level,lang,tweets,phd]
    # lets make a prediction
    header, tree = load_module()
    pred = tdidt_predict(header,tree,instance)
    if pred is not None:
        return jsonify({"prediction" : pred}), 200
    # something went wrong!!
    return "Error making a prediction", 400

if __name__ == "__main__":
    #header, tree = load_module()
    #print(header)
    #print(tree)
    app.run(host="0.0.0.0", port = 5001, debug=True) # hostname set to zeros for host to access (running on docker container)
    # TODO: when deploy app to "production", set debug=False
    # and check host and port values 
