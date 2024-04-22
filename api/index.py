import hashlib
import os
import uuid
import requests
from PIL import Image
from flask import Flask, request, jsonify, make_response, send_from_directory
app = Flask(__name__)
# TMP_DIR = 'tmp/jm'
# os.makedirs(TMP_DIR, exist_ok=True)
def get_num(aid, index):
    normalCutNum = 10  # 默认切割数
    aIndex = str(aid) + str(index)  # aid 和 index
    aIndex = hashlib.md5(aIndex.encode()).hexdigest()  # MD5 加密
    aIndex = ord(aIndex[-1])  # 获取最后一位的 Unicode 码表位置
    if 268850 <= int(aid) <= 421925:
        aIndex %= 10
    elif int(aid) >= 421926:
        aIndex %= 8
    if aIndex in range(10):
        normalCutNum = 2 + 2 * aIndex
    return normalCutNum


@app.route('/', methods=["GET"])
def return_OneText():
    return "fina_res"