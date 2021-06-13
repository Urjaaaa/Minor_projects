import tkinter as tk
import urllib.request
import json
import serial as sr
bkey = "4VQtsdmF8ZtwbsD4fJSy~VbZ2Lwq-JyEH-uyUKfyp7A~AtYhfGK58KhnSByHW22N2ZmlEkvn6Wsg7pxm8KSFoKR0y2G_F8sKMbKeclrGglhJ"
print("Taking your current location as starting point")
gps=sr.Serial("COM5",9600)
ln=gps.readline()

lat=ln[0:10]
rlat=float(lat)
i=int(rlat/100)
lat=round(i+(rlat-i*100)/60,6)

lng=ln[11:21]
rlng=float(lng)
i=int(rlng/100)
lng=round(i+(rlng-i*100)/60,6)

dest =input("Enter latitude and longitude of destination : ")#" 23.136358,72.542181"###d block#"c block 23.127249, 72.542494
t = urllib.parse.quote(dest, safe='')
Url = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + str(lat) + "," + str(lng) + "&wp.1=" + t + "&key=" + bkey
req = urllib.request.Request(Url)
res = urllib.request.urlopen(req)

r = res.read().decode(encoding="utf-8")
final = json.loads(r)
#print(final)
itineraryItems = final["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]

T = tk.Text(tk.Tk(), height=30, width=50)
T.pack()
for item in itineraryItems:
    T.insert(tk.END,str(item["instruction"]["text"])+"\n"+str(item["maneuverPoint"]["coordinates"])+"\n")
tk.mainloop()

