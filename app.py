from flask import Flask,jsonify
import requests

app = Flask(__name__)

@app.route("/stocks/<string:n>")

def getoptionchain(n):
    url = "https://www.nseindia.com/api/option-chain-equities?symbol="+n
    headers = {"User-Agent": "Mozilla/5.0"}
    with requests.Session() as ssn:
        ssn.get('https://www.nseindia.com/',headers=headers)
        data = ssn.get(url,headers=headers).json()
    
    return data



if __name__=="__main__":
    app.run(debug=True)