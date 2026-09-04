from flask import Flask, jsonify

app = Flask(__name__)
character = (
    'Tuntun mausi',
    'Raju',
    'Bheem',
    'Jaggu',
    'Chutki',
    'Indumati'
)
age = (
    45,
    4,
    9,
    "Not_specified",
    7,
    7
)
city = ("Dholakpur")

Chota_Bheem = [character, age, city]

@app.route("/")
def Cartoon():
    return jsonify(Chota_Bheem)


if __name__ == "__main__":
    app.run(debug=True)