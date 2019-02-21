from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, world."

@app.route("/blog")
def blog():
    return "blog page"
    
if __name__ == "__main__":
    app.run()
