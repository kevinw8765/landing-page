from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about-me')
def about_me():
    return render_template("aboutMe.html")
 

if __name__ == '__main__':
    app.run(debug=True) # Runs only on main.py so it doesn't run on every other, starts up a webserver with automatically rerun with debug=True

