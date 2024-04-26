import tkinter as tk
from PIL import Image, ImageTk
import requests
from datetime import datetime

# WeatherAPI key
API_KEY = '0ecbe2465cff4104bf204722241604'  # Replace with your API key

# Function to fetch weather data
def get_weather(city):
    url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no'
    response = requests.get(url)
    data = response.json()
    return data

# Function to update weather information
def update_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    if 'error' not in weather_data:
        weather_desc = weather_data['current']['condition']['text']
        temperature = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']
        icon_url = weather_data['current']['condition']['icon']

        # Update weather label
        weather_label.config(text=f"Weather: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%")

        # Display weather icon
        icon_data = requests.get("http:" + icon_url, stream=True).content
        icon_image = Image.open(icon_data).resize((100, 100), Image.ANTIALIAS)
        icon_photo = ImageTk.PhotoImage(icon_image)
        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo

        # Display background image based on weather condition
        bg_image_path = get_background_image(weather_desc)
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((400, 400), Image.ANTIALIAS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label.config(image=bg_photo)
        bg_label.image = bg_photo
    else:
        weather_label.config(text="City not found")

# Function to get background image based on weather condition
def get_background_image(weather_desc):
    if 'cloud' in weather_desc.lower():
        return 'cloudy_bg.jpg'
    elif 'rain' in weather_desc.lower():
        return 'rainy_bg.jpg'
    elif 'snow' in weather_desc.lower():
        return 'snowy_bg.jpg'
    elif 'clear' in weather_desc.lower():
        return 'sunny_bg.jpg'
    else:
        return 'default_bg.jpg'

# Create GUI
root = tk.Tk()
root.title("Jon's Weather App")
root.geometry("400x400")

# Background image
default_bg_image = Image.open('default_bg.jpg')  # Default background image
default_bg_photo = ImageTk.PhotoImage(default_bg_image)
bg_label = tk.Label(root, image=default_bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# City entry
city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.place(relx=0.5, rely=0.1, relwidth=0.4, anchor='n')

# Weather information
weather_label = tk.Label(root, font=("Helvetica", 14), bg='white', padx=10, pady=10)
weather_label.place(relx=0.5, rely=0.3, anchor='n')

# Weather icon
icon_label = tk.Label(root)
icon_label.place(relx=0.5, rely=0.45, anchor='n')

# Update weather button
update_button = tk.Button(root, text="Weather!", command=update_weather, font=("Helvetica", 14))
update_button.place(relx=0.5, rely=0.2, anchor='n')

# Current time
time_label = tk.Label(root, font=("Helvetica", 12), bg='white')
time_label.place(relx=0.5, rely=0.9, anchor='s')


# Update time label
def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=f"Current Time: {current_time}")
    time_label.after(1000, update_time)  # Update time every second


update_time()

root.mainloop()
