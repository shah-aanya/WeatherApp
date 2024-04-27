import requests
import tkinter as tk
import math

bgcolor= 'white'
fgcolor = '#558da6'
clicked = False

def GetWeatherData(c = None):
    if c == None:
        city_name = entry.get()
    else: 
        city_name = c
    url = 'https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=5eff8794b918351c605e5cb12b6f59cf'
    data = requests.get(url)
    data = data.json()
    description = data["weather"][0]["description"]
    temp_in_kelvin = data["main"]["temp"]
    temp_in_farenheit = round(temp_in_kelvin - 273.15,2)
    city = data["name"]
    country = data["sys"]["country"]
    humidity = data["main"]["humidity"]

    info = '''%s %s
Description: %s
Temp: %s°C
Humidity: %s'''%(city, country, description, temp_in_farenheit, humidity)
    
    if clicked == True:
        return [city, country, description, temp_in_farenheit, humidity]
    else:
        ShowData(info)
  
def ShowData(info):
    show_data_tp = tk.Toplevel(root, height= 400, width = 600, bg = bgcolor)

    frame = tk.LabelFrame(show_data_tp, bg = bgcolor, fg = fgcolor, text = 'Weather Data', font = ( 'comic', 30), labelanchor= 'n' )
    frame.place(relwidth= 0.8, relheight= 0.8, rely = 0.1, relx = 0.1)

    label =  tk.Label(frame, bg = bgcolor, fg = 'black', text = info , font = ( 'comic', 30), justify = 'left')
    label.place(relwidth= 0.8, relheight= 0.8, rely = 0.1, relx = 0.1)

def ShowCompareData():
    label_list = ['City:', 'Country:', 'Description:','Temp:', 'Humidity:']
    big_list = [label_list, city1data, city2data]

    toplevel_scw = tk.Toplevel(root, height = 500, width = 800, bg = bgcolor)
    frame = tk.LabelFrame(toplevel_scw, bg = bgcolor, fg = fgcolor, text = 'Compare Weather Data', font = ( 'comic', 40), labelanchor= 'n' )
    frame.place(relwidth= 0.8, relheight= 0.8, rely = 0.1, relx = 0.1)

    for r in range(5):
        for c in range(3):
            button = tk.Button(frame, bg = bgcolor, fg = fgcolor, text = big_list[c][r], font= ( 'comic', 25) )
            button.place(relwidth = 1/3, relheight= 1/5, relx = c/3, rely = r/5)

def CompareWeather():
    global clicked, city1data, city2data
    city1 = entry1.get()
    city1data = GetWeatherData(city1)
    city2 = entry2.get()
    city2data = GetWeatherData(city2)
    clicked = False
    ShowCompareData()


def ComparePageUI():
    global entry1, entry2, clicked

    clicked = True
    toplevel_cw = tk.Toplevel(root, height = 500, width = 800, bg = bgcolor)

    label =  tk.Label(toplevel_cw, bg = bgcolor, fg = 'black', text = 'Compare 2 Cities' , font = ( 'comic', 30), justify = 'center')
    label.place(relwidth= 0.8, relheight= 0.1, rely = 0.1, relx = 0.1)
    
    label1 =  tk.Label(toplevel_cw, bg = bgcolor, fg = 'black', text = 'City 1:' , font = ( 'comic', 30))
    label1.place(relwidth= 0.4, relheight= 0.1, rely = 0.3, relx = 0.1)

    label2 =  tk.Label(toplevel_cw, bg = bgcolor, fg = 'black', text = 'City 2:' , font = ( 'comic', 30))
    label2.place(relwidth= 0.4, relheight= 0.1, rely = 0.5, relx = 0.1)

    entry1 = tk.Entry(toplevel_cw, bg = bgcolor, fg = fgcolor, font = ('comic',30 ))
    entry1.place(relwidth= 0.4, relheight = 0.1, rely= 0.3, relx= 0.5)

    entry2 = tk.Entry(toplevel_cw, bg = bgcolor, fg = fgcolor, font = ('comic',30 ))
    entry2.place(relwidth= 0.4, relheight = 0.1, rely= 0.5, relx= 0.5)

    comp_button = tk.Button(toplevel_cw, bg = '#c1c7b5', fg = fgcolor, text = 'Submit', font = ( 'comic', 30), command= CompareWeather)
    comp_button.place(relwidth= 0.4, relheight = 0.1, rely= 0.7, relx= 0.3)

def HomePageUI():
    global root, entry
    root = tk.Tk()
    canvas = tk.Canvas(root, bg = 'white', height= 800, width= 1000)
    canvas.pack()

    label =  tk.Label(canvas, bg = bgcolor, fg = fgcolor, text = '''Weather app!''', font = ( 'Nevolide', 70))
    label.place(relwidth= 0.7, relheight= 0.2, rely = 0, relx = 0.15)

    frame = tk.Frame(canvas, bg = bgcolor)
    frame.place(relwidth= 0.8, relheight= 0.3, rely = 0.2, relx = 0.1)

    entry = tk.Entry(frame, bg = bgcolor, fg = fgcolor, font = ('comic',30 ))
    entry.place(relwidth= 0.7, relheight = 0.3, rely= 0, relx= 0)

    button = tk.Button(frame, bg = '#c1c7b5', fg = fgcolor, text = 'Submit', font = ( 'comic', 30), command= GetWeatherData)
    button.place(relwidth= 0.3, relheight = 0.3, rely= 0, relx= 0.7)

    bookmark_frame = tk.Frame(canvas, bg= bgcolor)
    bookmark_frame. place(relwidth= 0.8, relheight= 0.5, rely = 0.4, relx= 0.1)

    compare_button= tk.Button(bookmark_frame, bg = bgcolor, fg = fgcolor, text = 'Compare', font = ( 'comic', 30), command = ComparePageUI)
    compare_button.place(relwidth= 0.3, relheight= 0.92, relx= 0.35, rely= 0.04)

    city_list = [{'Paris': 'Paris', 'New York': 'New York', 'Mumbai': 'Mumbai', 'Cape Town': 'Cape Town'}, 
    {'Driest' : 'Arica', 'Rainiest': 'Mawsynram', 'Hottest': 'Dallol', 'Coldest': 'Yakutsk' }]

    relX = 0
    for r in range(2):
        relY = 0.04
        dict = city_list[r]
        for k,v in dict.items():
            button = tk.Button(bookmark_frame, bg = '#c1c7b5', fg = fgcolor, text = k, font = ( 'comic', 30), command= lambda c = v: GetWeatherData(c))
            button.place(relwidth= 0.3, relheight = 0.2, rely= relY, relx= relX)
            relY += 0.24
        relX += 0.7

HomePageUI()
root.mainloop()