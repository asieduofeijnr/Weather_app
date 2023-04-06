from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["TG0"] = df["   TG"].mask(df["   TG"] == -9999, np.nan)
    df["real_TG"] = df["TG0"] / 10
    temperature = df.loc[df["    DATE"] == date]["real_TG"].squeeze()
    result_temperature = {"station": station, "date": date, "temperature": temperature}
    return result_temperature


@app.route("/contact-us/")
def contact_us():
    return render_template("contact_us.html")


@app.route("/store/")
def store():
    return render_template("store.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
