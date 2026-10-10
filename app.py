from flask import Flask
 
app = Flask(__name__)

@app.route("/")
def Home():
    return "Hello Flask"
@app.route("/contact")
def contact():
    return "contact us"
@app.route("/about")
def about():
    return "welcome to about"
if __name__ == "__main__":
    app.run(debug=True)
