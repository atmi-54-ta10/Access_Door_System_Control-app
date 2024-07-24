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
# from ...uri import config
import messageBox
import ch_password_master  as cp
ctk.set_appearance_mode("System")

get_data_url = u.api_uri+"master/"
upd_data_url = u.api_uri+"master/edit"
scan_in_url = u.api_uri+"master/card_in"
scan_out_url = u.api_uri+"master/card_out"
cw_url = u.api_uri+"master/pw"


        

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #inisiasi 
        self.title("Setting page")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False)
        self.configure(fg_color="#004643")

        self.wm_attributes('-fullscreen','true')

        self.username_master = tk.StringVar()
        self.name_master = tk.StringVar()
        self.Lab_master = tk.StringVar()
        self.job_master = tk.StringVar()
        self.section_master = tk.StringVar()
        self.status_master = tk.StringVar()

        self.status = [ "Available","Unavailable"]
        job = ["Instructor", "Staff", "Student", "Other"]
        

         #inisiasi gambar log out
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
       
         #inisiasi gambar add data
        self.logo_image_master = ctk.CTkImage(Image.open(os.path.join(image_path, "master_admin.png")), size=(100, 100))

        self.logo_image_updt_data = ctk.CTkImage(Image.open(os.path.join(image_path, "settings hitam.png")), size= (100,100))

        self.logo_image_clear = ctk.CTkImage(Image.open(os.path.join(image_path, "dust_hitam.png")), size= (100,100))

        self.logo_scan_card = ctk.CTkImage(Image.open(os.path.join(image_path, "scan card hitam.png")), size= (100,100))
        
        self.logo_image_chpw = ctk.CTkImage(Image.open(os.path.join(image_path, "reset-password_hitam.png")), size= (100,100))
        
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

        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Setting data", text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)
         #frame kiri
        self.frame_left = ctk.CTkFrame(master=self.main_frame, height=500, width=400,corner_radius=20,fg_color="#abd1c6")
        self.frame_left.place(relx=0.125, rely=0.089)
        self.icon1 = ctk.CTkLabel(self.frame_left,text="Settings",text_color="#004643",font=ctk.CTkFont(size=30, weight="bold"))
        self.icon1.place(relx=0.15,rely=0.03)

        #entry username
        self.entry_username = ctk.CTkEntry(master=self.frame_left, textvariable= self.username_master,height=35,width=370,fg_color="#abd1c6",border_color="#004643", corner_radius=25, text_color="#004643",font=ctk.CTkFont(size=15))
        self.entry_username.place(relx=0.04, rely= 0.185)
        self.label_username = ctk.CTkLabel(master=self.frame_left, text="Username", font=ctk.CTkFont(size=17, weight="bold"),text_color="#004643")
        self.label_username.place(relx=0.06, rely=0.12)
        #entry nama
        self.entry_name = ctk.CTkEntry(master=self.frame_left, textvariable=self.name_master,height=35,width=370,fg_color="#abd1c6",border_color="#004643", corner_radius=25, text_color="#004643",font=ctk.CTkFont(size=15))
        self.entry_name.place(relx=0.04, rely= 0.32)
        self.label_name = ctk.CTkLabel(master=self.frame_left, text="Name", font=ctk.CTkFont(size=17, weight="bold"),text_color="#004643")
        self.label_name.place(relx=0.06, rely=0.255)
        #nama lab
        self.entry_Lab = ctk.CTkEntry(master=self.frame_left, textvariable=self.Lab_master,height=35,width=370,fg_color="#abd1c6",border_color="#004643", corner_radius=25, text_color="#004643",font=ctk.CTkFont(size=15))
        self.entry_Lab.place(relx=0.04, rely= 0.455)
        self.label_Lab = ctk.CTkLabel(master=self.frame_left, text="Lab", font=ctk.CTkFont(size=17, weight="bold"),text_color="#004643")
        self.label_Lab.place(relx=0.06, rely=0.39)

        ##entry job
        self.combo_job = ctk.CTkComboBox(master=self.frame_left,values=job  ,height=35, width=365, fg_color="#abd1c6",text_color="#004643",dropdown_fg_color="#abd1c6",dropdown_text_color="#004643",border_color="#004643",corner_radius=25,font=ctk.CTkFont(size=17),dropdown_font=ctk.CTkFont(size=20))
        self.combo_job.place(relx = 0.04,rely = 0.59)
        self.label_job = ctk.CTkLabel(master=self.frame_left, text="job", font=ctk.CTkFont(size=17, weight="bold"),text_color="#004643")
        self.label_job.place(relx=0.06, rely=0.525)


        

        #section
        self.entry_section = ctk.CTkEntry(master=self.frame_left, textvariable= self.section_master,height=35,width=370,fg_color="#abd1c6", corner_radius=25, text_color="#004643",font=ctk.CTkFont(size=15))
        self.entry_section.place(relx=0.04, rely= 0.72)
        self.label_section = ctk.CTkLabel(master=self.frame_left, text="Section", font=ctk.CTkFont(size=17, weight="bold"),text_color="#004643")
        self.label_section.place(relx=0.06, rely=0.66)
        
        #status 
        self.combobox_status = ctk.CTkComboBox(master=self.frame_left,values=self.status,height=35, width=365, fg_color="#abd1c6",text_color="#004643",dropdown_fg_color="#abd1c6",dropdown_text_color="#004643",corner_radius=25,font=ctk.CTkFont(size=17),dropdown_font=ctk.CTkFont(size=20))
        self.combobox_status.place(relx=0.04,rely=0.85)

        self.label_status = ctk.CTkLabel(master=self.frame_left, text="Status",font=ctk.CTkFont(size=17, weight="bold"),text_color="#004643")
        self.label_status.place(relx=0.06, rely=0.79 )
        #tombol add data
        self.btn_update_data = ctk.CTkButton(master=self.main_frame,width=100,height=100,text="Update\n  ",text_color="#004643", fg_color="#abd1c6",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_updt_data,compound="top", command=self.update)
        self.btn_update_data.place(relx=0.6, rely=0.15)

        # change password 
        self.btn_chpw = ctk.CTkButton(master=self.main_frame,width=100,height=100,text="Change\nPassword",text_color="#004643", fg_color="#abd1c6",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_chpw,compound="top", command=self.open_toplevel)
        self.btn_chpw.place(relx=0.795, rely=0.15)

        #frame scan card
        self.frame_card =ctk.CTkFrame(master=self.main_frame, height=265, width=350,corner_radius=10,fg_color="#abd1c6")
        self.frame_card.place(relx=0.6, rely=0.45)

        self.label_scan= ctk.CTkLabel(master=self.frame_card,text="Scan Card",text_color="#004643", image=self.logo_scan_card,font=ctk.CTkFont(size=40, weight="bold"),compound="top")
        self.label_scan.place(relx=0.22,rely=0.125)
        #tombol scan dard in
        self.btn_scan_card_in = ctk.CTkButton(master=self.frame_card,width=90,height=50,text="Card IN",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"),command=self.card_in)
        self.btn_scan_card_in.place(relx=0.11, rely=0.7)
        #tombol add data
        self.btn_scan_card_out = ctk.CTkButton(master=self.frame_card,width=75,height=50,text="Card OUT",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"),command=self.card_out)
        self.btn_scan_card_out.place(relx=0.55, rely=0.7)
        #button back 
        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#004643", fg_color="#abd1c6",corner_radius=10,font=ctk.CTkFont(size=20,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.01, rely=0.9)
        self.req_res()


        

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
        a = res["status"].capitalize()
        print(a)
        self.username_master.set(res['username'])
        self.name_master.set(res['name'])
        self.combobox_status.set(res["status"])
        print(res["status"])
        self.Lab_master.set(res['lab'])
        # self.job_master.set(res['job'])
        self.combo_job.set(res['job'])
        self.section_master.set(res['section'])

    def update(self):
        username = self.username_master.get()
        name = self.name_master.get()
        lab = self.Lab_master.get()
        job = self.combo_job.get()
        section = self.section_master.get()
        status = self.combobox_status.get()
        self.status_master.set(status)  

        body_json ={
            "username": username,
            "name": name,
            "lab": lab,
            "job": job,
            "section": section,
            "status": status

        }
        res = requests.put(upd_data_url,json=body_json,headers={"Authorization":u.Authorization})
        message = res.json()
        if res.status_code == 200:
            messageBox.show("Information",message["message"],"info")
        else:
            messageBox.show("Warning",message["message"],"warn")

        self.req_res()

    async def scan_rfid_async(self, url):
        self.display_time()
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url,headers={"Authorization":u.Authorization}) as response:
                # ,headers={"Authorization":u.Authorization}) as response:
                    return await response.json()
        except Exception as e:
            return {"message": str(e)}

        
    async def on_scan_rfid(self,url_card):
        data = await self.scan_rfid_async(url_card) 
        messageBox.show("Infomartion", data['message'], "info")



    def scan_rfid(self,url):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.on_scan_rfid(url))
        loop.close()

    def card_in(self):
        self.scan_rfid(scan_in_url)
        self.req_res()
    def card_out(self):
        self.scan_rfid(scan_out_url)
        self.req_res()


    def btnback (self):
        self.destroy()
        import dashboard_master_admin as dma
        dma.main()    

    def open_toplevel(self):
        cp.show()


def main():
    app = App()
    app.mainloop()
