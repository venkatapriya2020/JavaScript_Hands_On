import requests 
from flask import Flask , render_template,request
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/convert",methods=["POST"])
def convert():
    currency = request.form.get("currency")#
    print(currency)
    res = requests.get("http://data.fixer.io/api/latest?access_key=089650790f130aabee9475bc90832522")
                        
    if res.status_code != 200:
        return jsonify({"success": False})
            
    data = res.json()
    rate = data["rates"][currency]
    print(data)
    if currency not in data["rates"]:
        return jsonify({"success" : False})
    #rate = data["rates"][other]
    return jsonify({"success":True, "rate": data["rates"][currency]})