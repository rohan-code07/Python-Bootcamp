from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")

    if name:
        flash("Welcome, " + name + "!", "success")
        return redirect(url_for("home"))
    else:
        flash("Please enter your name.", "danger")
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)