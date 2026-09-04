from flask import Flask, render_template

# app = Flask(__name__, static_url_path="/assets")     static_path_url decide karega ki tum kya likhoge url me
app = Flask(__name__, static_folder="assests", static_url_path="/static")      # static_folder decide karega ki tum konsa folder access karoge 

@app.route("/")
def home():
    # Render the HTML template named index.html and send it to the browser.
    return render_template("index.html")


# Start the Flask development server.
# debug=True enables auto-reloading when the code changes.
app.run(debug=True)
