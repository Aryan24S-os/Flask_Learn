from flask import Flask,render_template
 
app = Flask(__name__)

@app.route("/")
def Home():
    name = "aryan"
    course = ["python" , "Flask" , "Django" , "Java"]
    city = "Faridabad"
    price = 5000
    return render_template("index.html" , 
                           name = name,
                           course = course,
                           city = city,
                           price = price
                           )
@app.route("/user/<passion>")
def user(passion):
    return f"my passion is {passion}"

@app.route("/teach")
def teach():
    grade = 80
    is_logged_in = True
    return render_template("ifteach.html" , is_logged_in = is_logged_in , grade = grade)
if __name__ == "__main__":
    app.run(debug=True)
