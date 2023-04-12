# 🐍 Python Flask Weather App
Welcome to the Python Flask Weather App! This web app provides weather data for different stations based on date and year.

# 📝 Installation
Clone the repository: git clone https://github.com/yourusername/your-repo.git <br>
Navigate to the project directory: cd your-repo <br>
Install the dependencies: pip install -r requirements.txt <br>

# 💻 Usage
To run the app, execute the following command in the terminal: python app.py. <br>

Once the server is up and running, open your web browser and navigate to http://localhost:5000/. <br>

# Endpoints
The following endpoints are available:<br>

/ - Home page that displays a list of weather stations.<br>
/api/v1/<station> - Returns all available data for a specific weather station.<br>
/api/v1/<station>/<date> - Returns the temperature for a specific weather station on a given date.<br>
/api/v1/yearly/<station>/<year> - Returns all available data for a specific weather station for a given year.<br>
/contact-us/ - Contact us page.<br>
/store/ - Store page.<br>

# 📂 Project Structure
The project structure is as follows:<br>

Copy code
├── app.py
├── data_small
│   ├── stations.txt
│   ├── TG_STAID123456.txt
│   ├── TG_STAID234567.txt
│   └── TG_STAID345678.txt
├── README.md
├── requirements.txt
└── templates
    ├── contact_us.html
    ├── home.html
    └── store.html
    
main.py - The main Flask application file.<br>
data_small/ - Directory that contains weather data for different stations.<br>
templates/ - Directory that contains the HTML templates used to render the pages.<br>
