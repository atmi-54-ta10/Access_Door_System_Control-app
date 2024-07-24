import tkinter as tk
import tkinter.messagebox as tkmb
from typing import Optional, Tuple, Union
import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import requests
import uri as u 
import messageBox


get_data_master = u.api_uri +"master/status"
get_data_door = u.api_uri +"door/status"
open_uri = u.api_uri + "door/opens"

ctk.set_appearance_mode("System")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #inisiasi 
        self.title("Dashboard page")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False)
        self.wm_attributes('-fullscreen','true')


         #inisiasi gambar log out
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
        
        self.logo_image_logout = ctk.CTkImage(Image.open(os.path.join(image_path, "logout putih.png")), size=(25, 25))

        font_nama = ctk.CTkFont('Segoe UI Black',30)
         #inisiasi gambar open door
        self.logo_image_open_door = ctk.CTkImage(Image.open(os.path.join(image_path, "open_door putih.png")), size=(150, 150))

         #inisiasi gambar lock door
        self.logo_image_master = ctk.CTkImage(Image.open(os.path.join(image_path, "master_admin.png")), size=(230, 230))

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
        

        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Control", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)

        #button edit data
        self.left_frame = ctk.CTkFrame(master=self.main_frame,width=450,height=450, fg_color="#abd1c6",corner_radius=20,border_width=5,border_color="#004643")
        self.left_frame.grid_columnconfigure((0,1),weight=1)
        self.left_frame.grid_rowconfigure((0),weight=1)
        self.left_frame.place(relx=0.17,rely=0.2)
        
        self.btn_open = ctk.CTkButton(master=self.left_frame,width=250,height=250,text="OPEN",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=30,weight="bold"), image=self.logo_image_open_door,compound="top",command=self.openn)
        # self.btn_open.place(relx=0.17, rely=0.4)
        self.btn_open.grid(row=1,column=0,pady=20,padx=50)

        self.frm_pd = ctk.CTkFrame(master=self.left_frame, height=40, width=300, fg_color="#abd1c6", border_width=5,border_color="#004643",corner_radius=20)
        # self.frm_pd.place(relx=0.2,rely=0.2)
        self.frm_pd.grid(row=0,column=0,pady=20,padx =50)
        self.frm_pd.grid_columnconfigure(0,weight=1)
        self.frm_pd.grid_rowconfigure(0,weight=1)

        self.stat_pd = ctk.CTkLabel(master=self.frm_pd,text_color="#004643",fg_color="#abd1c6", font=font_nama, wraplength=200, justify="center")
        self.stat_pd.grid(row=0,column=0,pady=5,padx=15)

        #frame status master admin
        self.right_frame = ctk.CTkFrame(master=self.main_frame,height=300, width=250, corner_radius=20, fg_color="#abd1c6",border_width=5,border_color="#004643")
        self.right_frame.place(relx=0.55, rely=0.2)
        self.right_frame.grid_columnconfigure(0,weight=1)
        self.right_frame.grid_rowconfigure((0,1),weight=1)


        #button Control
        self.icon_master = ctk.CTkLabel(master=self.right_frame,text="", corner_radius=20, image=self.logo_image_master)
        # self.icon_master.place(relx=0.05, rely=0.1)
        self.icon_master.grid(row=0,column=0,pady=20,padx=50)

        #status 
        self.frm_st = ctk.CTkFrame(master=self.right_frame, height=40, width=200, fg_color="#abd1c6", border_width=5,border_color="#004643",corner_radius=30)
        # self.frm_st.place(relx=0.3,rely=0.85)
        self.frm_st.grid(row=1,column=0, pady=30,padx=50)
        self.frm_st.grid_columnconfigure(0,weight=1)
        self.frm_st.grid_rowconfigure(0,weight=1)

        self.status_master = ctk.CTkLabel(master=self.frm_st, text="", font=ctk.CTkFont(size=20, weight="bold"),text_color="#004643",corner_radius=20,fg_color="#abd1c6")
        # self.status_master.place(relx=0.1, rely=0.18)
        self.status_master.grid(row=0,column=0,pady=10,padx=10)

         
        self.display_time()

         #button log out
        self.logout = ctk.CTkButton(master= self.main_frame,fg_color="#004643",text="Logout",text_color="#abd1c6",font=ctk.CTkFont(size=20,weight="bold"),image=self.logo_image_logout,corner_radius=20,width=50, height=50, command=self.btnlogout)
        self.logout.place(relx=0.85, rely=0.9)


    def btnlogout (self):
        self.destroy()
        import login_page as l
        l.main()    


    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")

        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.update_data()
        self.clock_date.after(500, self.display_time)
    

    def openn(self):
        req_body = {
            "name": "Guest",
            "job": "Other",
            "platform":"Aplikasi Desktop"
        }
        res = requests.put(open_uri,req_body)
        response = res.json()['message']
        if res.status_code == 200:
            messageBox.show("Information",response, "info")
        elif res.status_code == 409:
            messageBox.show("Warning",response,"warn")

    def update_data(self):
        res = requests.get(get_data_door)
        status = res.json()
        if status['lock'] == 1:
            self.stat_pd.configure(text="Locked")
        else:
            self.stat_pd.configure(text="Unlocked")
        res_master = requests.get(get_data_master)
        self.status_master.configure(text=res_master.json()["status"])


def main():
    app = App()
    app.mainloop()
