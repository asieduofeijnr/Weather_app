from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

stations_filename = "data_small\stations.txt"
stations = pd.read_csv(stations_filename, skiprows=17)
stations = stations[["STAID", "STANAME                                 "]].to_html()


@app.route("/")
def home():
    return render_template("home.html", data=stations)


@app.route("/api/v1/<station>/<date>")
def station_date_data(station, date):
    filename = "data_small\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["TG0"] = df["   TG"].mask(df["   TG"] == -9999, np.nan)
    df["real_TG"] = df["TG0"] / 10
    temperature = df.loc[df["    DATE"] == date]["real_TG"].squeeze()
    result_temperature = {"station": station, "date": date, "temperature": temperature}
    return result_temperature


@app.route("/api/v1/yearly/<station>/<year>")
def station_year(station, year):
    filename = "data_small\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["TG0"] = df["   TG"].mask(df["   TG"] == -9999, np.nan)
    df["real_TG"] = df["TG0"] / 10
    df["    DATE"] = df["    DATE"].astype(str)
    result = df.loc[df["    DATE"].str.startswith(str(year))]
    return result.to_dict(orient="records")


@app.route("/api/v1/<station>")
def station_data(station):
    filename = "data_small\TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df["TG0"] = df["   TG"].mask(df["   TG"] == -9999, np.nan)
    result = df["real_TG"] = df["TG0"] / 10
    return df.to_dict(orient="records")


@app.route("/contact-us/")
def contact_us():
    return render_template("contact_us.html")


@app.route("/store/")
def store():
    return render_template("store.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
