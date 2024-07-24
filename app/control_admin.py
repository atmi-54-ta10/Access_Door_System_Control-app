import customtkinter as ctk
import tkinter as tk
import os
from PIL import Image
from datetime import datetime
import requests
import uri as u 
import messageBox
get_data_url = u.api_uri+"door/status"
lock_door_url= u.api_uri+"door/lock"
unlock_door_url = u.api_uri+"door/unlock"
open_door_url = u.api_uri+"door/open"
get_stat_master =u.api_uri+"master/status"


ctk.set_appearance_mode("System")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #inisiasi 
        self.title("Control Page")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False)
        self.wm_attributes('-fullscreen','true')
        self.configure(fg_color="#ABD1C6")


        #inisiasi gambar log out
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
       
         #inisiasi gambar open door
        self.logo_image_open_door = ctk.CTkImage(Image.open(os.path.join(image_path, "open_door putih.png")), size=(125, 125))
        self.logo_image_lock = ctk.CTkImage(Image.open(os.path.join(image_path, "lock_door putih.png")), size=(125, 125))
        self.logo_image_unlock = ctk.CTkImage(Image.open(os.path.join(image_path, "unlock_door putih.png")), size=(125, 125))

        

        #background
        self.main_frame = ctk.CTkFrame(master=self,height=600,width=1024,fg_color="#abd1c6")
        self.main_frame.place(relx=0, rely=0)


        self.status_frame_door =ctk.CTkFrame(self.main_frame,corner_radius=20,height=100, width=250,fg_color="#004643")
        self.status_frame_door.place(relx=0.17,rely=0.2)
        self.label_door = ctk.CTkLabel(master=self.status_frame_door,text="Door :", text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"))
        self.label_door.place(relx=0.1,rely=0.1)

        self.stat_door_label = ctk.CTkLabel(master=self.status_frame_door,text='', text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"))
        self.stat_door_label.place(relx=0.1,rely=0.55)



        self.status_frame_master =ctk.CTkFrame(self.main_frame,corner_radius=20,height=100, width=290,fg_color="#004643")
        self.status_frame_master.place(relx=0.55,rely=0.2)
        self.label_master = ctk.CTkLabel(master=self.status_frame_master,text="Master Availability:", text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"), justify="left")
        self.label_master.place(relx=0.1,rely=0.1)

        self.stat_master_label = ctk.CTkLabel(master=self.status_frame_master,text='', text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"))
        self.stat_master_label.place(relx=0.1,rely=0.55)

        self.clock_frame = ctk.CTkFrame(master=self.main_frame, height=65, width=250,fg_color="#abd1c6", border_color="#004643",border_width=3,corner_radius=20)
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
        self.button_open = ctk.CTkButton(master=self.main_frame,width=200,height=200,text="OPEN",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_open_door,compound="top", command=self.btn_open)
        self.button_open.place(relx=0.17, rely=0.57)

        #button Control
        self.button_lock = ctk.CTkButton(master=self.main_frame,width=200,height=200,text="LOCK",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_lock,compound="top", command=self.btn_lock)
        self.button_lock.place(relx=0.4, rely=0.57)
        #button unlock
        self.button_unlock = ctk.CTkButton(master=self.main_frame,width=200,height=200,text="UNLOCK",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_unlock,compound="top", command=self.btn_unlock)
        self.button_unlock.place(relx=0.63, rely=0.57)

        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#abd1c6", fg_color="#004643",corner_radius=10,font=ctk.CTkFont(size=20,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.02, rely=0.91)
        self.display_time()
    


    def btn_open(self):
        req_body ={
            "platform": "Dekstop"
        }
        res3 = requests.put(open_door_url,json=req_body,headers={"Authorization":u.Authorization})
        message = res3.json()
        response = message['message']
        if res3.status_code == 200:
            messageBox.show("Info",response, "info")
        elif res3.status_code == 409:
            messageBox.show("Warning",response,"warn")

    def btn_lock(self):
        req_body ={
            "platform": "Dekstop"
        }
        res_lock = requests.put(lock_door_url, json=req_body,headers={"Authorization":u.Authorization})
        if res_lock.status_code== 200:
            messageBox.show("Information",res_lock.json()['message'],"info")

        else:
            messageBox.show("Warning",res_lock.json()['message'],"warn")

        
    
    def btn_unlock(self):
        req_body ={
            "platform": "Dekstop"
        }
        res_unlock = requests.put(unlock_door_url, json=req_body,headers={"Authorization":u.Authorization})
        if res_unlock.status_code ==200:
            messageBox.show("Information",res_unlock.json()['message'],"info")
         
        else:
            messageBox.show("Warning",res_unlock.json()['message'],"warn")

    def update_data(self):
        res_door = requests.get(get_data_url)
        res_master = requests.get(get_stat_master)
        status = res_door.json()
        self.stat_master_label.configure(text=res_master.json()["status"]) 
        if status['lock'] == 1:
            self.stat_door_label.configure(text="Locked")
        else:
            self.stat_door_label.configure(text="Unlocked")
        

    
    def btnback (self):
        self.destroy()
        import dashboard_admin as da
        da.main()    



    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")

        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.update_data()
        self.clock_date.after(500, self.display_time)



def main():
    app = App()
    app.mainloop()
