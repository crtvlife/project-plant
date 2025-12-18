from typing import Literal
from flask import Flask, request, jsonify, redirect
import httpx


app = Flask(__name__)
"""
    TODO:
    1. 主統輪尋 GET ESP32 (30s)並暫存資料
    2. 處理資料並 發送POST封包回 
    
    待議:
    1. 是否使用 WebSocket 獲取連線？
    2. 使否是用 async 框架？

"""


def get_esp32() -> tuple[bool, str]:
    """獲取 ESP32 資料"""
    esp_url = "http://exp_esp32.test"
    with httpx.Client(timeout=5.0) as client:
        req = client.get(esp_url)
        if req.status_code == httpx.codes.OK:
            ...  # 處理資料
            return (True, "Ok")
        else:
            return (False, f"status_code = {req.status_code}")


# 發送東西
@app.route("/Hello", methods=["GET"])  # 網址列
def hello():
    return "<H1>Hello word.</H1>"  # 輸出的內容


# 接收東西
@app.route("/post", methods=["POST"])  # 接收請求
def hello_post():

    return f"ok{request.get_data()}"


app.run(host="0.0.0.0", port=3000)  # 啟動用


"""
ip -> 家
port (端口) -> 窗戶

http (網路協議) -> 語言
    (打嘴砲的方式)
    get -> 請求 -> 敲門
    post -> 有事相求，具體內容在封包內寫入

"""
