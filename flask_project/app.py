from flask import Flask, render_template , url_for
app = Flask(__name__)


#@app.route("/")
@app.route("/layout")
def layout():
     return render_template('layout.html')

@app.route("/")
@app.route("/home")
def home():
   return render_template('home.html')

@app.route("/Resources")
def Resources():
   return render_template('Resources.html')


if __name__ == '__main__':
    app.run(host='localhost', port='5006',debug=True)
