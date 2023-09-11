import tkinter
from tkinter import PhotoImage
from tkinter import ttk
import requests
import datetime
import config

# main window
root = tkinter.Tk()

root.geometry("500x600")
root.title("Weather Widget")

def func_get_weather():
    city = select_city_dropdown.get()
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.api_key}&units=metric"
    server_data = requests.get(api_url).json()

    # server_data = json.dumps(server_data,indent=2)
    # print(server_data)

    weather = server_data["weather"][0]["main"]
    temp = server_data["main"]["temp"]
    feels = server_data["main"]["feels_like"]
    humidity = server_data["main"]["humidity"]
    today = datetime.date.today()

    output_label.config(
        text=f"City: {city.title()}\n"
        f"Date: {today.day} / {today.month} / {today.year}\n"
        f"Weather: {weather}\n"
        f"Temperature: {temp}°C\n"
        f"Feels Like: {feels}°C\n"
        f"Humidity: {humidity} g.m⁻³"
    )
    output_frame.pack()


# r is to consider string as regular string without any escape character like backslash
image_path = "background.png"
bg_image = PhotoImage(file=image_path)
set_bg_image = tkinter.Label(root, image=bg_image)
set_bg_image.place(relheight=1, relwidth=1)

app_header = tkinter.Label(root,text="Weather Widget",font=("Georgia", 24),bg="white",fg="blue",highlightbackground="pink",highlightthickness=1,)
app_header.pack(pady=20)
select_city_label = tkinter.Label(root, text="Type or Select a City", font=("Georgia", 15))
select_city_label.pack(pady=20)

cities = ["Mumbai", "Pune", "Goa", "Delhi", "Bangalore"]
select_city_dropdown = ttk.Combobox(root, values=cities, font=("Georgia", 10))
select_city_dropdown.pack(pady=20)

get_weather_button = tkinter.Button(root, text="Get Weather", font=("Georgia", 15), command=func_get_weather)
get_weather_button.pack(pady=10)

output_frame = tkinter.Frame(root, highlightbackground="light green", highlightthickness=5)

output_label = tkinter.Label(output_frame, text="", font=("Georgia", 15))
output_label.pack(pady=10)

# keeps the app open until we close it
root.mainloop()
