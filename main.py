from flask import Flask, render_template


app = Flask(__name__)


# Create an index page
@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


#  Create about page
#@app.route('/about')
#def about():
#    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
