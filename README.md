# Weather Application 🌤️

This is a simple and user-friendly Python GUI application to display the current weather of any city you enter. It fetches real-time weather data using the Open-Meteo API and shows an appropriate weather icon based on the current conditions.

## Features
- Search for the current weather of any city.
- Displays:
  - Temperature (°C)
  - Wind Speed (km/h)
  - Weather condition icon (sunny, cloudy, rainy, etc.)
- Clean and responsive GUI built with Tkinter.
- Lightweight and fast.

## Technologies Used
- Python
- Tkinter (GUI)
- PIL (Pillow) for image handling
- Requests for API communication

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/weather-application.git
   ```
2. Navigate to the project directory:
   ```bash
   cd weather-application
   ```
3. Install the required Python libraries:
   ```bash
   pip install requests Pillow
   ```
4. Make sure you have an `icons/` folder with the following images:
   - `sun.png`
   - `partly_cloudy.png`
   - `clouds.png`
   - `rainy.png`
   - `unknown.png`

## How to Use
1. Run the application:
   ```bash
   python weather_app.py
   ```
2. Enter the name of a city in the input field.
3. Click the "Submit" button.
4. View the current weather data and icon for the selected city.

## Weather Icon Mapping
| Weather Code | Icon            |
|--------------|-----------------|
| 0            | Sunny            |
| 1, 2         | Partly Cloudy     |
| 3            | Cloudy           |
| 61-65        | Rainy            |
| Other        | Unknown Condition |

## APIs Used
- **Geocoding API**: To convert city names to latitude and longitude.  
- **Open-Meteo API**: To fetch the current weather data.

## Notes
- The application uses free public APIs, so rate limits may apply.
  
## Screenshots
*(You can add a screenshot here by uploading an image and linking it.)*

## License
This project is open-source and available under the [MIT License](LICENSE).

