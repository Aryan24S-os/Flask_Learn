from flask import Flask
 
app = Flask(__name__)

@app.route("/")
def Home():
    return "Hello Flask"
@app.route("/math/<int:number>")
def sqr(number):
    return str(number*number)
@app.route("/contact")
def contact():
    return "contact us"
@app.route("/user/<name>")
def user(name):
    return f"hello {name}"
@app.route("/student/<name>/<course>")
def des(name , course):
    return f"{name} is learning {course}"
@app.route("/about")
def about():
    return "welcome to about"
if __name__ == "__main__":
    app.run(debug=True)
