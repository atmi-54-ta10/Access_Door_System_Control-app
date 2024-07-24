import tkinter as tk
import tkinter.messagebox as tkmb
from typing import Optional, Tuple, Union
import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime


ctk.set_appearance_mode("System")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #inisiasi 
        self.title("Monitoring page")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False)
        self.configure(fg_color="#abd1c6")

        self.wm_attributes('-fullscreen','true')

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
        
        self.logo_image_data_log = ctk.CTkImage(Image.open(os.path.join(image_path, "Data_logging putih.png")), size=(75, 75))
        self.logo_image_temperature = ctk.CTkImage(Image.open(os.path.join(image_path, "thermometer putih.png")), size=(75, 75))

        #background
        self.main_frame = ctk.CTkFrame(master=self,height=600,width=1024,fg_color="#abd1c6")
        self.main_frame.place(relx=0, rely=0)

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

        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="History", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)

         #button log data
        self.btn_data_log = ctk.CTkButton(master=self.main_frame,width=200,height=200,text="Report",text_color="#abd1c6", fg_color="#004643",corner_radius=30,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_data_log,compound="top",command=self.log)
        self.btn_data_log.place(relx=0.22, rely=0.38)

        #button temp
        self.btn_temp_log = ctk.CTkButton(master=self.main_frame,width=200,height=200,text="Temperature",text_color="#abd1c6", fg_color="#004643",corner_radius=30,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_temperature,compound="top",command=self.temp_)
        self.btn_temp_log.place(relx=0.62, rely=0.38)


        #btn back
        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#abd1c6", fg_color="#004643",corner_radius=10,font=ctk.CTkFont(size=15,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.01, rely=0.9)

    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")

        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.clock_date.after(1000, self.display_time)


    def btnback (self):
        self.destroy()
        import dashboard_admin as da
        da.main()    


    def log(self):
        self.destroy()
        import datalog_admin as da 
        da.main()

    def temp_ (self):
        self.destroy()
        import temperature_admin as ta
        ta.main()
    
   

def main():
    app = App()
    app.mainloop()
