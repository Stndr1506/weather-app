import tkinter as tk
import requests
from PIL import Image,ImageTk

root=tk.Tk()
root.title("Weather App")
root.geometry("600x500")

def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City:%s\nCondition:%s\nTemperature:%s'%(city,condition,temp)
    except:
        final_str='There is a problem in retrieving this information'
    return final_str


def get_weather(city):
    weather_key='d2069b1580a5d86ac1e4716ef70f62be'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    weather=response.json()
    result['text']=format_response(weather)

img = Image.open('./whether.jpg')
img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_lbl,text='Earth including over 200,000 cities!',fg='red',bg='sky blue',font=("times new roman",25))
heading_title.place(x=80,y=18)

frame_one=tk.Frame(bg_lbl, bg="#42c2f4",bd=5)
frame_one.place(x=80,y=60,width=475,height=50)

txt_box=tk.Entry(frame_one,font=("times new roman",25),width=17)
txt_box.grid(row=0,column=0,sticky='W')

btn=tk.Button(frame_one,text="whether status",fg="green",font=('times new roman',16,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

frame_two=tk.Frame(bg_lbl, bg="#42c2f4",bd=5)
frame_two.place(x=80,y=130,width=475,height=300)

result=tk.Label(frame_two,font=40,bg='white')
result.place(relwidth=1,relheight=1)



root.mainloop()