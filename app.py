from flask import Flask, request , jsonify, redirect
app = Flask(__name__)



@app.route("/oc", methods=["POST, GET"])
def return1():
    oc = request.args.get("oc")  #網址傳參數
    print(oc)

    request.form.get("oc")  #請求體


    print(request.json)
    
    



@app.route("/api", methods=["GET"])
def api():
    return jsonify(         #.json檔案
        {
            "溫度":"oc",
            "土壤含水量":"wat",
            "光照度":"lm",
        }
    )

#發送東西
@app.route("/Hello", methods=["GET"])# 網址列
def hello():
    return "<H1>Hello word.</H1>"#輸出的內容
    

#接收東西
@app.route("/post", methods=["POST"])#接收請求
def hello_post():

    return f"ok{request.get_data()}"

app.run(host= "0.0.0.0", port=3000)#啟動用


"""
ip -> 家
port (端口) -> 窗戶

http (網路協議) -> 語言
    (打嘴砲的方式)
    get -> 請求 -> 敲門
    post -> 有事相求，具體內容在封包內寫入

"""