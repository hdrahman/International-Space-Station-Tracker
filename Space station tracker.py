#backend
import requests
import geopy.distance
import geocoder


#returns the longitude and latitude of the ISS in that order
def iss_coords(number_only = False):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    latitude = data.get("iss_position").get("latitude")
    longitude = data.get("iss_position").get("longitude")
    if not number_only:
        if latitude[0] == "-":
            latitude = f"{latitude[1:]}º South"
        else:
            latitude = f"{latitude}º North"

        if longitude[0] == "-":
            longitude = f"{longitude[1:]}º West"
        else:
            longitude = f"{longitude}º East"
        return latitude, longitude
    return float(latitude), float(longitude)

#returns ground distance from current location to ISS in kilometers
def dist_to_iss():
    user_loc = geocoder.ip("me").latlng
    user_loc = (float(user_loc[0]), float(user_loc[1]))
    iss_loc = iss_coords(number_only = True)

    dist_to_iss = geopy.distance.distance(user_loc, iss_loc).km

    return round(dist_to_iss, 3)



#front end
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root = tk.Tk()
canvas = tk.Canvas(root, width=750,height = 650)
canvas.configure(bg='grey19')
canvas.pack()

label1 = tk.Label(root, bg="black", fg="grey81", text=' Space Station Tracker ', font=("Trajan Pro", 25), borderwidth=3, relief="solid")
canvas.create_window(375, 75, window=label1)

frame = Frame(canvas, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img= (Image.open("C:\\Users\\Haame\\Desktop\\iss.jpg"))

#Resize the Image using resize method
resized_image= img.resize((750,650), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

label = Label(frame, image = new_image).pack()

button1 = tk.Button (root, text='Calculate Information', font=("ROG FONTS", 10), bg='white', command = lambda:open())
canvas.create_window(375, 450, window=button1)

def open():
    Distance = tk.Label(root, bg="black", fg="grey81", text="Distance from position: " + str(dist_to_iss()), font=("Trajan Pro", 15), borderwidth=3, relief="solid")
    canvas.create_window(375, 485, window=Distance)

    coords = tk.Label(root, bg="black", fg="grey81", text="ISS coordinates: " + str(iss_coords()), font=("Trajan Pro", 15), borderwidth=3, relief="solid")
    canvas.create_window(375, 525, window=coords)


root.mainloop()
