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
if __name__ == "__main__":
    app.run(debug=True)
