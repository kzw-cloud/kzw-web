from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/about')
def about():
  return render_template("about.html")


@app.route('/user/<username>')
def show_user(username):
  # show the user name for that user
  return render_template("user.html", username=username)


if __name__ == '__main__':
  app.run()
