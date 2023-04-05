from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 23
    return {"station": station, "date": date, "temperature": 23}


@app.route("/contact-us/")
def contact_us():
    return render_template("contact_us.html")


@app.route("/store/")
def store():
    return render_template("store.html")


if __name__ == "__main__":
    app.run(debug=True)
