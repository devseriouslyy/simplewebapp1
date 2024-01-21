# Import the Flask library
from flask import Flask, render_template, request

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route("/")
def home():
    # Render the home.html template
    return render_template("home.html")

# Define a route for the hello page
@app.route("/hello")
def hello():
    # Get the name parameter from the request
    name = request.args.get("name", "world")
    # Render the hello.html template with the name variable
    return render_template("hello.html", name=name)

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
