import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as tkmb
import customtkinter as ctk
import os
from datetime import datetime
import requests
from CTkTable import *
from PIL import Image
import asyncio
import aiohttp
import uri as u
import messageBox
ctk.set_appearance_mode("System")

get_data_url = u.api_uri+"user/"
upd_data_url = u.api_uri+"user/"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #inisiasi 
        self.title("Setting page")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False)
        self.configure(fg_color="#abd1c6")

        self.wm_attributes('-fullscreen','true')

        self.username_admin = tk.StringVar()
        self.name_admin = tk.StringVar()
        self.job_master = tk.StringVar()
        self.idNumber_admin = tk.StringVar()

        self.status = [ "Available","Unavailable"]
        job = ["Instructor", "Staff", "Student", "Other"]
        

         #inisiasi gambar log out
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
       
         #inisiasi gambar add data
        self.logo_image_master = ctk.CTkImage(Image.open(os.path.join(image_path, "master_admin.png")), size=(100, 100))

        self.logo_image_updt_data = ctk.CTkImage(Image.open(os.path.join(image_path, "settings putih.png")), size= (100,100))

        self.logo_image_clear = ctk.CTkImage(Image.open(os.path.join(image_path, "dust_hitam.png")), size= (100,100))

        self.logo_scan_card = ctk.CTkImage(Image.open(os.path.join(image_path, "scan card hitam.png")), size= (100,100))

        
        #background
        self.main_frame = ctk.CTkFrame(master=self,height=600,width=1024,fg_color="#abd1c6")
        self.main_frame.place(relx=0, rely=0)
            
        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Setting data", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)
         #jam   
        self.clock_frame = ctk.CTkFrame(master=self.main_frame, height=65, width=250,fg_color="#abd1c6", border_color="#004643",border_width=3,corner_radius=0)
        self.clock_frame.place(relx=0.8, rely=0.005)
        self.clock_frame.grid_rowconfigure((0, 1), weight=1)

        self.clock_time = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        # self.clock_time.place(relx=0.26, rely=0.12)
        self.clock_time.grid(row=0,column=0,padx=20, pady=(5,0))

        self.clock_date = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#004643",font=ctk.CTkFont(size=12, weight="bold"))
        # self.clock_date.place(relx=0.14, rely=0.5)
        self.clock_date.grid(row=1,column=0,padx=20,pady=(0,5))
        self.display_time()

         #frame kiri
        self.frame_left = ctk.CTkFrame(master=self.main_frame, height=500, width=400,corner_radius=20,fg_color="#004643")
        self.frame_left.place(relx=0.125, rely=0.089)
        self.icon1 = ctk.CTkLabel(self.frame_left,text="Settings",text_color="#abd1c6",font=ctk.CTkFont(size=30, weight="bold"))
        self.icon1.place(relx=0.15,rely=0.03)

        #entry username
        self.entry_username = ctk.CTkEntry(master=self.frame_left, textvariable= self.username_admin,height=35,width=370,fg_color="#004643", border_color="#abd1c6",corner_radius=25, text_color="#abd1c6",font=ctk.CTkFont(size=15),state="disabled")
        self.entry_username.place(relx=0.04, rely= 0.185)
        self.label_username = ctk.CTkLabel(master=self.frame_left, text="Username", font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_username.place(relx=0.06, rely=0.12)
        #entry nama
        self.entry_name = ctk.CTkEntry(master=self.frame_left, textvariable=self.name_admin,height=35,width=370,fg_color="#004643", border_color="#abd1c6", corner_radius=25, text_color="#abd1c6",font=ctk.CTkFont(size=15))
        self.entry_name.place(relx=0.04, rely= 0.32)
        self.label_name = ctk.CTkLabel(master=self.frame_left, text="Name", font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_name.place(relx=0.06, rely=0.255)
        
        ##entry job
        self.combo_job = ctk.CTkComboBox(master=self.frame_left,values=job  ,height=35, width=365, fg_color="#004643", border_color="#abd1c6",text_color="#abd1c6",dropdown_fg_color="#abd1c6",dropdown_text_color="#004643",corner_radius=25,font=ctk.CTkFont(size=17),dropdown_font=ctk.CTkFont(size=17),button_color="#abd1c6")
        self.combo_job.place(relx = 0.04,rely = 0.455)
        self.label_job = ctk.CTkLabel(master=self.frame_left, text="Job", font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_job.place(relx=0.06, rely=0.39)

        #section
        self.entry_id_number = ctk.CTkEntry(master=self.frame_left, textvariable= self.idNumber_admin,height=35,width=370,fg_color="#004643",border_color="#abd1c6", corner_radius=25, text_color="#abd1c6",font=ctk.CTkFont(size=15))
        self.entry_id_number.place(relx=0.04, rely= 0.59)
        self.label_id_number = ctk.CTkLabel(master=self.frame_left, text="ID Number", font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_id_number.place(relx=0.06, rely=0.525)
        self.req_res()



        #tombol add data
        self.btn_update_data = ctk.CTkButton(master=self.main_frame,width=150,height=150,text="Update",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_updt_data,compound="top", command=self.update)
        self.btn_update_data.place(relx=0.7, rely=0.15)
       
        #button back 
        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#abd1c6", fg_color="#004643",corner_radius=10,font=ctk.CTkFont(size=20,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.01, rely=0.9)

        

    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")

        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.clock_date.after(1000, self.display_time)

    def req_res(self):
        response = requests.get(get_data_url,headers={"Authorization":u.Authorization})
        res = response.json()
        print(res)
        self.username_admin.set(res['username'])
        self.name_admin.set(res['name'])
        self.combo_job.set(res['job'])
        self.idNumber_admin.set(res['id_number'])

    def update(self):
        username = self.username_admin.get()
        name = self.name_admin.get()
        job = self.combo_job.get()
        id_num = self.idNumber_admin.get()
        

        body_json ={
            "username": username,
            "name": name,
            "job": job,
            "id_number": id_num

        }
        res = requests.put(upd_data_url,json=body_json,headers={"Authorization":u.Authorization})
        message = res.json()
        if res.status_code == 200:
            messageBox.show("Information",message["message"],"info")
        else:
            messageBox.show("Warning",message["message"],"warn")

        self.req_res()


    def btnback (self):
        self.destroy()
        import dashboard_admin as da
        da.main()    


def main():
    app = App()
    app.mainloop()
