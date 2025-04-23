#imports
import tkinter 
import requests
from PIL import Image, ImageTk


def get_city():
    city=city_name_entry.get()
    
    # get the city coordinates
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=tr&format=json"
    geo_response=requests.get(geo_url)
    geo_data = geo_response.json()
    print(geo_data)
    
    try:
        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]
        
        #Get Weather data
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&timezone=auto"
        )
        weather_response=requests.get(weather_url)
        weather_data=weather_response.json()
        print(weather_data)
        
        
        temperature = weather_data["current_weather"]["temperature"]
        windspeed = weather_data["current_weather"]["windspeed"]
        
        weather_code = weather_data["current_weather"]["weathercode"]
        icon_path = get_icon_path(weather_code)
        
        # Resize to weather icons 
        image = Image.open(icon_path)
        image = image.resize((100, 100), Image.LANCZOS)  
        photo = ImageTk.PhotoImage(image)
        
        icon_label.config(image=photo)
        icon_label.image = photo  
        
        result_label.config(text=f"{city.title()}:\nTemperature: {temperature}°C\nWind Speed: {windspeed} km/h")
        
    except Exception as e:
        result_label.config(text="City not found or data not retrieved.")
        print("Hata:", e)

        
        
def get_icon_path(weathercode):
    if weathercode == 0:
        return "icons/sun.png"
    elif weathercode in [1, 2]:
        return "icons/partly_cloudy.png"
    elif weathercode == 3:
        return "icons/clouds.png"
    elif 61 <= weathercode <= 65:
        return "icons/rainy.png"
    else:
        return "icons/unknown.png"





window=tkinter.Tk()
window.title("Weather Application")
window.geometry("400x400")

icon_label = tkinter.Label(window)
icon_label.pack(pady=10)

city_label1=tkinter.Label(text="Enter to city name: ",font=("Arial",20,"italic"))
city_label1.pack(pady=10)

city_name_entry = tkinter.Entry()
city_name_entry.pack(pady=10)

submit_button=tkinter.Button(text="Submit",font=("Arial",10,"italic"),command=get_city)
submit_button.pack(pady=10)

result_label = tkinter.Label(text="", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()
