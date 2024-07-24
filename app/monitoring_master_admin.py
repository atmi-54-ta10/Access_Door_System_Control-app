import tkinter as tk
import tkinter.messagebox as tkmb
from typing import Optional, Tuple, Union
import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import uri as u
import requests
import pytz

get_data_master = u.api_uri + "master/status"
get_data_pintu = u.api_uri + "door/status"
get_data_temp = u.api_uri + "temp/"

ctk.set_appearance_mode("System")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #inisiasi 
        self.title("Monitoring page")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False)
        self.configure(fg_color="#004643")

        self.wm_attributes('-fullscreen','true')


        #background
        self.main_frame = ctk.CTkFrame(master=self,height=600,width=1024,fg_color="#004643")
        self.main_frame.place(relx=0, rely=0)

        #jam
        self.clock_frame = ctk.CTkFrame(master=self.main_frame, height=65, width=250,fg_color="#004643", border_color="#abd1c6",border_width=3,corner_radius=0)
        self.clock_frame.place(relx=0.8, rely=0.005)
        self.clock_frame.grid_rowconfigure((0, 1), weight=1)
        self.clock_time = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"))
        # self.clock_time.place(relx=0.26, rely=0.12)
        self.clock_time.grid(row=0,column=0,padx=20, pady=(5,0))
        self.clock_date = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#abd1c6",font=ctk.CTkFont(size=12, weight="bold"))
        # self.clock_date.place(relx=0.2, rely=0.5)
        self.clock_date.grid(row=1,column=0,padx=20,pady=(0,5))
        self.display_time()

        
        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Monitoring", text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)
        #stat door
        self.status_frame_door =ctk.CTkFrame(self.main_frame,corner_radius=20,height=150, width=200,fg_color="#abd1c6")
        self.status_frame_door.place(relx=0.1,rely=0.2)
        self.status_frame_door.grid_columnconfigure(0,weight=1)
        self.status_frame_door.grid_rowconfigure((0,1),weight=1)

        self.label_door = ctk.CTkLabel(master=self.status_frame_door,text="Door :", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        # self.label_door.place(relx=0.1,rely=0.1)
        self.label_door.grid(row=0,column=0,pady=(15,20),padx=(40))

        self.stat_door_label = ctk.CTkLabel(master=self.status_frame_door,text='', text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        # self.stat_door_label.place(relx=0.1,rely=0.5)
        self.stat_door_label.grid(row=1,column=0,pady=(0,20))

        #stat master
        self.status_frame_master =ctk.CTkFrame(self.main_frame,corner_radius=20,height=150, width=250,fg_color="#abd1c6")
        self.status_frame_master.place(relx=0.29,rely=0.2)
        self.status_frame_master.grid_columnconfigure(0,weight=1)
        self.status_frame_master.grid_rowconfigure((0,1),weight=1)

        self.label_master = ctk.CTkLabel(master=self.status_frame_master,text="Master Availability:", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"), justify="left",wraplength=300)
        # self.label_master.place(relx=0.1,rely=0.1)
        self.label_master.grid(row=0,column=0,pady=(15,20),padx=(50))

        self.stat_master_label = ctk.CTkLabel(master=self.status_frame_master,text='', text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        # self.stat_master_label.place(relx=0.1,rely=0.5)
        self.stat_master_label.grid(row=1,column=0,pady=(0,20))
        
        #stat tap card 
        self.frame_num_of_tap_card =ctk.CTkFrame(self.main_frame,corner_radius=20,height=150, width=175,fg_color="#abd1c6")
        self.frame_num_of_tap_card.place(relx=0.65,rely=0.2)        
        self.frame_num_of_tap_card.grid_columnconfigure(0,weight=1)
        self.frame_num_of_tap_card.grid_rowconfigure((0,1),weight=1)

        self.label_notc = ctk.CTkLabel(master=self.frame_num_of_tap_card,text="Tap Card:", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"), justify="left")
        # self.label_notc.place(relx=0.1,rely=0.1)
        self.label_notc.grid(row=0,column=0,pady=(15,20),padx=(40))

        self.num_of_tap_card = ctk.CTkLabel(master=self.frame_num_of_tap_card,text='', text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        # self.num_of_tap_card.place(relx=0.1,rely=0.5)
        self.num_of_tap_card.grid(row=1,column=0,pady=(0,20))

        #stat tap card 
        self.frame_panel =ctk.CTkFrame(self.main_frame,corner_radius=20,height=150, width=175,fg_color="#abd1c6")
        self.frame_panel.place(relx=0.14,rely=0.45)
        self.frame_panel.grid_columnconfigure(0,weight=1)
        self.frame_panel.grid_rowconfigure((0,1,2),weight=1)

        self.label_tempPanel = ctk.CTkLabel(master=self.frame_panel,text="Panel:", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"), justify="left")
        # self.label_tempPanel.place(relx=0.1,rely=0.1)
        self.label_tempPanel.grid(row=0,column=0,pady=(15,10),padx=(40))

        self.temp_panel = ctk.CTkLabel(master=self.frame_panel,text='', text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        # self.temp_panel.place(relx=0.1,rely=0.5)
        self.temp_panel.grid(row=1,column=0,pady=(0,10))

        self.temp_panel_date = ctk.CTkLabel(master=self.frame_panel,text='', text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        # self.temp_panel.place(relx=0.1,rely=0.5)
        self.temp_panel_date.grid(row=2,column=0,pady=(0,20), padx=20)


        #stat tap card 
        self.frame_Emlock =ctk.CTkFrame(self.main_frame,corner_radius=20,height=150, width=175,fg_color="#abd1c6")
        self.frame_Emlock.place(relx=0.50,rely=0.45)
        self.frame_Emlock.grid_columnconfigure(0,weight=1)
        self.frame_Emlock.grid_rowconfigure((0,1),weight=1)

        self.label_emlock = ctk.CTkLabel(master=self.frame_Emlock,text="EmLock:", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"), justify="left")
        # self.label_emlock.place(relx=0.1,rely=0.1)
        self.label_emlock.grid(row=0,column=0,pady=(15,10),padx=(40))
        self.temp_emlock = ctk.CTkLabel(master=self.frame_Emlock,text='', text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        # self.temp_emlock.place(relx=0.1,rely=0.5)
        self.temp_emlock.grid(row=1,column=0,pady=(0,10))
        self.temp_emlock_date = ctk.CTkLabel(master=self.frame_Emlock,text='', text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        # self.temp_panel.place(relx=0.1,rely=0.5)
        self.temp_emlock_date.grid(row=2,column=0,pady=(0,20), padx=20)


        #btn back
        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#004643", fg_color="#abd1c6",corner_radius=10,font=ctk.CTkFont(size=15,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.01, rely=0.9)
        self.req()

    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")

        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.clock_date.after(1000, self.display_time)

    def req(self):
        res_master = requests.get(get_data_master)
        res_pintu = requests.get(get_data_pintu)
        res_temp = requests.get(get_data_temp)
        self.stat_master_label.configure(text=(res_master.json()["status"]).capitalize())
        self.num_of_tap_card.configure(text=(res_pintu.json()["tap_card"]))
        if res_pintu.json()['lock']==0:
            self.stat_door_label.configure(text="Unlock")
        if res_pintu.json()['lock']==1:
            self.stat_door_label.configure(text="Lock")
        if res_temp.status_code == 200:
            date_time= datetime.strptime(res_temp.json()['time'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Jakarta')).strftime("%a %b %d %Y %H:%M")
            # print(date_time)
            self.temp_panel.configure(text=res_temp.json()["panel_temp"])
            self.temp_emlock.configure(text=res_temp.json()["emlock_temp"])
            self.temp_panel_date.configure(text=date_time)
            self.temp_emlock_date.configure(text=date_time)
        if res_temp.status_code != 200:
            self.temp_panel.configure(text="0°C")
            self.temp_emlock.configure(text="0°C")


    def btnback (self):
        self.destroy()
        import dashboard_master_admin as dma
        dma.main()    


    
   

def main():
    app = App()
    app.mainloop()

