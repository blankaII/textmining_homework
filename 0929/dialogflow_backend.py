#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import imports
from settings import *

import json

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, JSON
class Messages(Base):
    __tablename__ = 'messages'
    msg = Column(JSON)

    def __repr__(self):
        return self.msg

# 呼叫Flaske 套件
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
app = Flask(__name__)
log = app.logger

"""
for Dialogflow webhook setting
使用 ngrok 串接 Dialogflow: http://*.ngrok.io/
"""
@app.route('/', methods=['POST'])
def root():
    print('***Processing***')
    engine = create_engine('sqlite:///./dialogflow.sqlite3', echo=False)
    req = request.get_json(force=True)
    print(json.dumps(req, indent=4))
    intent_name = req.get('queryResult').get('intent').get('displayName')
    fulfillmentText = req.get('queryResult').get('fulfillmentText')

    if intent_name == "大小":
        size=req.get('queryResult').get('parameters').get('size')[0]
        response = {
            "fulfillmentText": "請問您要的是"+size+"嗎?"
        }

    print('***Done***\n')
    return make_response(jsonify(response))

if __name__ == '__main__':
    IP, PORT = '0.0.0.0', 80
    app.run(debug=True, port=PORT, host=IP)
