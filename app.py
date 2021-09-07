#use 'source venv/bin/activate' to start virtual environment
#use 'flask run' to test on local server
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.debug = True
@app.route("/")
def index():
    return render_template('home.html')
if __name__ == '__main__':
   app.run(debug=True) 

