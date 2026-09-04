from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def Home():
    name = 'Rohan'
    Bank_balance = 67000
    if 'name' in request.args.keys():
        name = request.args['name']
    if 'Bank_balance' in request.args.keys():
        Bank_balance = request.args['Bank_balance']
    return render_template("index.html", name=name, Bank_balance=Bank_balance)

app.run(debug=True)
