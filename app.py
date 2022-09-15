import re
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def top(): 
    return render_template('index.html')

@app.route("/result", methods=["POST"])
def result():
    
    if re.fullmatch("(070|080|090)[0-9]{4}[0-9]{4}", request.form.get("tell")):
        tell_result = "電話番号登録完了"
    else:
        tell_result = "電話番号失敗"
    if  re.fullmatch("[1-9]{3}-([1-9]{4})|([1-9]{2})", request.form.get("addressnumber")):
        address_result = "郵便番号登録完了"
    else:
        address_result ="郵便番号登録失敗"
    if re.fullmatch(".+@.+", request.form.get("mail")):
        mail_result = "メールアドレス登録完了"
    else:
        mail_result = "メールアドレス登録失敗"
    return render_template("index2.html", tell_result = tell_result, address_result = address_result, mail_result = mail_result)

if __name__ == '__main__':
    app.run(debug=True)
