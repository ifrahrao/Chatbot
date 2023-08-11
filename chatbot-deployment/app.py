from flask import Flask,render_template,request,jsonify
from chat import get_response,get_response_2

app= Flask(__name__)
@app.get("/")
def index_get():
    return render_template("base.html")

@app.get("/ifrah_bot")
def index():
    return render_template("new_base.html")
@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message={"answer":response}
    return jsonify(message)

@app.post("/predict_2")
def predict_2():
    text = request.get_json().get("message")
    response = get_response_2(text)
    message={"answer":response}
    return jsonify(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
