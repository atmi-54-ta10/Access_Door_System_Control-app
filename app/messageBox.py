import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import requests
import uri as u 




def show(judul,pesan,icon):
    
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
    if icon == "warn":
        logomsb = ctk.CTkImage(Image.open(os.path.join(image_path, "warning.png")), size=(50, 50))
    elif icon == "info":
        logomsb = ctk.CTkImage(Image.open(os.path.join(image_path, "info.png")), size=(50, 50))
    mb = ctk.CTkToplevel(fg_color= "#66A5AD")
    mb.title(judul)
    mb.geometry("400x180+312+120")
    mb.resizable(False,False)
    mb.place_slaves()
    mb.overrideredirect(True)
    # mb.attributes
    # mb.grab_set()
    mb.tkraise()
    def exit_m():
        # mb.grab_release()
        mb.destroy()
    mbframe = ctk.CTkFrame(master=mb,fg_color= "#004643",height=100, width=350,corner_radius=20)
    mbframe.place(relx=0.065,rely=0.1)
    message = ctk.CTkLabel(master=mbframe,text=pesan,text_color="#ffffff",image=logomsb, compound="left", font = ctk.CTkFont(size=15, weight="bold"),wraplength=300)
    message.place(relx=0.1,rely=0.2)
    mbtn = ctk.CTkButton(master=mb,width=50,height=40,text="OK",text_color="#ffffff", fg_color="#66A5AD",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), command=exit_m)
    mbtn.place(relx=0.4, rely=0.7)
    mb.wait_window()