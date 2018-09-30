from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

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
    intent_name = req.get('queryResult').get('intent').get('displayName')
    fulfillmentText = req.get('queryResult').get('fulfillmentText')

    # fulfillmentText 主要回覆的內容
    response = {
          "fulfillmentText": fulfillmentText + ' (' + intent_name + ')',
        }

    print('***Done***\n')
    return make_response(jsonify(response))

if __name__ == '__main__':
    IP, PORT = '0.0.0.0', 80
    app.run(debug=True, port=PORT, host=IP)