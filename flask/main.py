from flask import Flask, render_template

#WSGI application
app = Flask(__name__) #creates an instance of the flask class, which will be your WSGI application

@app.route("/")
def welcome():
     return "<html><H1>Welcome to my home.</H1></html>"

@app.route("/index")
def index():
     return render_template('index.html')

@app.route("/about")
def about():
     return render_template('about.html')


if __name__ == "__main__":
    app.run(debug = True )