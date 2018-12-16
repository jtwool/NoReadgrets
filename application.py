from flask import Flask, render_template, url_for

application = Flask(__name__)

@application.route("/")
def home():
    return render_template("coming_soon.html")

if __name__ == "__main__":
    application.run()
