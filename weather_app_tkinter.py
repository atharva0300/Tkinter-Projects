from tkinter import *
import requests
from PIL import ImageTk, Image
import json

root = Tk() 
root.title("Weather app Tkinter")
root.geometry("400x100")


# Crret ziplookup function 
def ziplookup()  :
    zip.get()
    """
    zipLabel = Label(root, text=zip.get())
    zipLabel.grid(row =0 ,column=2 , padx=20)
    """

    try : 
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=1C83CC00-F63A-416F-BED0-D3F81B5CCE06")
        api = json.loads(api_request.content)
        city =api[0]['ReportingArea']
        quality =api[0]['AQI']
        category =api[0]['Category']['Name']

        if category == "Good" : 
            weather_color ="#0C0"
        elif category == "Moderate": 
            weather_color ="#FFFF00"
        elif category == "Unhealthy for Sensitive Groups" : 
            weather_color ="#aff9900"
        elif category == "Unhealthy": 
            weather_color ="#FF0000"
        elif category == "Very Unhealthy" : 
            weather_color ="#990066"
        elif category == "Hazardous": 
            weather_color ="#660000"

    except Exception as e:  
        api = "Error..."
    
    root.configure(background =weather_color)
    myLabel = Label(root , text="City : " +city + "\nAir Quality : " + str(quality) + "\nCategory : " + str(category) , font = ("Helvetica" , 10),background=weather_color)
    myLabel.grid(row  =3 , column = 0 , columnspan= 3)


""" Washington DC 
https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=1C83CC00-F63A-416F-BED0-D3F81B5CCE06
"""

zip = Entry(root)
zip.grid(stick= W+E+N+S  )

zipbutton = Button(root, text="Lookup zipcode" , command = ziplookup)
zipbutton.grid(row =0, column=1,padx=25)

root.mainloop()