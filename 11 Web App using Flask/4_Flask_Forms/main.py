from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        with open("contact.txt", "a")as f:
           f.write(f"The name is {request.form['name']} and email is {request.form['email']}\n")
        print(request.form)
        print(request.method)
        return render_template("contact.html")

    else:
        return render_template("contact.html")

app.run(debug=True)