from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Pradeep" : 45,
        "Rahul" : 67,
        "Rohit" : 87,
        "Raju" : 89,
        "Chutki" : 45
    }
    return render_template("index.html", marks=marks)
app.run(debug=True)





