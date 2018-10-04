from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
import json

# 呼叫Flaske 套件
app = Flask(__name__)
log = app.logger

"""
for Dialogflow webhook setting
使用 ngrok 串接 Dialogflow: http://*.ngrok.io/
"""
@app.route('/', methods=['POST'])
def root():
    print('***Processing***')
    req = request.get_json(force=True)
    print(json.dumps(req, indent=4))
    intent_name = req.get('queryResult').get('intent').get('displayName')
    fulfillmentText = req.get('queryResult').get('fulfillmentText')

    # fulfillmentText 主要回覆的內容
    #response = {
    #      "fulfillmentText": fulfillmentText + ' (' + intent_name + ')',
    #    }
    ###{
    ###    "responseId": "07215414-40e4-4760-b57b-b9fafe715498",
    ###    "queryResult": {
    ###        "queryText": "\u8acb\u554f\u6709XXL\u55ce",
    ###        "parameters": {
    ###            "size": [
    ###                "XXL"
    ###            ]
    ###        },
    ###        "allRequiredParamsPresent": true,
    ###        "fulfillmentText": "\u60a8\u8981\u7684\u662f XXL",
    ###        "fulfillmentMessages": [
    ###            {
    ###                "text": {
    ###                    "text": [
    ###                        "\u60a8\u8981\u7684\u662f XXL"
    ###                    ]
    ###                }
    ###            }
    ###        ],
    ###        "intent": {
    ###            "name": "projects/primeval-lotus-88210/agent/intents/b2ab32bf-06e8-4718-9cb8-86f74c59f613",
    ###            "displayName": "\u5927\u5c0f"
    ###        },
    ###        "intentDetectionConfidence": 0.65,
    ###        "languageCode": "zh-cn"
    ###    },
    ###    "originalDetectIntentRequest": {
    ###        "payload": {}
    ###    },
    ###    "session": "projects/primeval-lotus-88210/agent/sessions/6580049a-2ef5-b6b0-b5ca-badb014bbc41"
    ###}
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
