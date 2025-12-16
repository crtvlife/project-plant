from flask import Flask, request , jsonify , redirect
app = Flask(__name__)

@app.route("/oc", methods=["POST"])
def return1():
    #oc = request.args.get("oc")  #網址傳參數
   # print(oc)
    
    xx = request.form.get("xx")
    print(xx)

    print(request.form)


@app.route("/api", methods=["GET"])
def api():
    return jsonify(     #.json檔案
        {
            "氣溫":"oc",
            "土壤含水量":"wat",
            "光照度":"lm",
        }
    )

app.run(host= "0.0.0.0", port=3000)