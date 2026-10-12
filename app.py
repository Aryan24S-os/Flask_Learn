from flask import Flask,render_template
 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/user/<passion>")
def user(passion):
    return f"my passion is {passion}"
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/teach")
def teach():
    grade = 80
    is_logged_in = True
    return render_template("ifteach.html" , is_logged_in = is_logged_in , grade = grade)
if __name__ == "__main__":
    app.run(debug=True)
