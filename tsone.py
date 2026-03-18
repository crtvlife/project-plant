from flask import Flask, request , jsonify , redirect
app = Flask(__name__)

latest_data = ""

@app.route("/oc", methods=["POST"])
def return1():
    global latest_data
    
    latest_data = request.get_data()
    
    return "OK", 200


@app.route("/api", methods=["GET"])
def api():
   a = latest_data
   return latest_data

app.run(host= "0.0.0.0", port=3000)