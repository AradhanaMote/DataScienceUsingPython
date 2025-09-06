from flask import Flask

#WSGI application
app = Flask(__name__) #creates an instance of the flask class, which will be your WSGI application

@app.route("/")
def welcome():
     return "Welcome to this best Flask course. This should be an amazing course."

@app.route("/index")
def index():
     return "Welcome to the index route"


if __name__ == "__main__":
    app.run(debug = True )