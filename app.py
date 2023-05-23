from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
  return render_template("index.html")


@app.route('/about')
def about():  # put application's code here
  return render_template("about.html")


@app.route('/user/<username>')
def show_user_profile(username):
  # show the user profile for that user
  return 'User %s' % username


if __name__ == '__main__':
  app.run()
