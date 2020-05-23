import os
from flask import Flask, render_template, request, session
from UserInfo import UserInfo, Authority

app = Flask(__name__)
super_devloper = "imax2218@gmail.com"
accounts = {"id": 0, "imax2218@gmail.com": 1}
userInfos = [UserInfo("name", "password", "id", "authority"), UserInfo("Ryota", "ryotafuw", "imax2218@gmail.com", Authority.Super)]

@app.route("/", methods=["GET", "POST"]) 
def index():    
    if request.method == "POST": 
        # if the account is there and matched password
        accountID = request.form.get("accountID")
        if accountID in accounts:
            user = userInfos[accounts[accountID]]
            if user.password == request.form.get("password"):
                return render_template("home.html", name=user.name)
        return render_template("home.html", wrongID=True)
    else:
        return render_template("index.html", wrongID=False)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        accountID = request.form.get("accountID")
        if accountID not in accounts:
            accounts[accountID] = len(userInfos)
            userInfos.append((UserInfo(**request.form)))
    else:
        return render_template("signup.html")


@app.route("/<string:anythingelse>")
def notExistYet(anythingelse):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)