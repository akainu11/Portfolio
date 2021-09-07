#use 'source venv/bin/activate' to start virtual environment
#use 'flask run' to test on local server
from flask import Flask, render_template, url_for

app = Flask(__name__)
app.debug = True
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/videos")
def videos():
    return render_template('videos.html')

if __name__ == '__main__':
   app.run(debug=True) 