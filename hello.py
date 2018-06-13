from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return '''
    <html>
    <head><title> This is my flask app (/title></head>
    <body><h1> Hello From Flask </h1>
    </html>
    '''
if __name__ == "__main__":
    app.run(debug=True)
