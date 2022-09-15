import re
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def top(): 
    return render_template('index.html')

@app.route("/result", methods=["POST"])
def result():
    if re.fullmatch("(070|080|090)-[0-9]{4}-[0-9]{4}", request.form.get("tell")):
        result = "完了"
    else:
        result = "失敗" 
    return render_template("index2.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
