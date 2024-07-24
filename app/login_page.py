import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import requests
import uri as u 
import messageBox


ctk.set_appearance_mode("System")
login_URL = u.api_uri +"user/log_in"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #deklarasi
        self.title("Login page")
        self.configure(fg_color="#66A5AD")
        self.geometry("1024x600+0+0")
        # self.overrideredirect(True)
        self.wm_attributes('-fullscreen','true')
        # self.resizable(False,False)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "smart-door.png")), size=(280,330))

        self.main_frame = ctk.CTkFrame(master=self,height=600,width=1024,fg_color="#66A5AD")
        self.main_frame.place(relx=0, rely=0)

        self.clock_frame = ctk.CTkFrame(master=self.main_frame, height=65, width=250,fg_color="#66A5AD", border_color="#000000",border_width=3,corner_radius=0)
        self.clock_frame.place(relx=0.8, rely=0.005)
        self.clock_frame.grid_rowconfigure((0, 1), weight=1)
        self.clock_time = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#000000",font=ctk.CTkFont(size=25, weight="bold"))
        # self.clock_time.place(relx=0.26, rely=0.12)
        self.clock_time.grid(row=0,column=0,padx=20, pady=(5,0))
        self.clock_date = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#000000",font=ctk.CTkFont(size=12, weight="bold"))
        # self.clock_date.place(relx=0.2, rely=0.5)
        self.clock_date.grid(row=1,column=0,padx=20,pady=(0,5))
        self.display_time()
        
        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Login", text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)


        #frame kiri
        self.left_frame = ctk.CTkFrame(master=self.main_frame, height=450, width=400,border_color="#004643",border_width=10,fg_color="#abd1c6")
        self.left_frame.place(relx=0.07, rely=0.15)
        self.icon1 = ctk.CTkLabel(self.left_frame,text="SMART DOOR SYSTEM",text_color="#004643", image=self.logo_image,font=ctk.CTkFont(size=35, weight="bold"),compound="top", wraplength=300)
        self.icon1.place(relx=0.17,rely=0.05)
        


        #frame login (kanan)
        self.right_frame = ctk.CTkFrame(master=self.main_frame, height=450, width=400,fg_color="#abd1c6",border_color="#004643",border_width=10)
        self.right_frame.place(relx=0.535, rely=0.15)
        self.judul_log = ctk.CTkLabel(master=self.right_frame, text="LOGIN", font=ctk.CTkFont(size=55, weight="bold"),text_color="#004643")
        self.judul_log.place(relx=0.3, rely=0.05)
        self.text_log = ctk.CTkLabel(master=self.right_frame, text="Sign in to continue", font=ctk.CTkFont(size=15),text_color="#004643")
        self.text_log.place(relx=0.34, rely=0.175)
        
        self.entry_user = ctk.CTkEntry(master=self.right_frame, placeholder_text="",height=50,width=250,fg_color="#abd1c6", corner_radius=25, text_color="#004643",font=ctk.CTkFont(size=20),border_width=5,border_color="#004643")
        self.entry_user.place(relx=0.2, rely= 0.35)
        self.label_user = ctk.CTkLabel(master=self.right_frame, text="Username", font=ctk.CTkFont(size=20, weight="bold"),text_color="#004643")
        self.label_user.place(relx=0.2, rely=0.28)

        self.entry_pass = ctk.CTkEntry(master=self.right_frame, placeholder_text="",height=50,width=250,fg_color="#abd1c6", corner_radius=25, text_color="#004643",font=ctk.CTkFont(size=20),show="*",border_width=5,border_color="#004643")
        self.entry_pass.place(relx=0.2, rely= 0.55)
        self.label_pass = ctk.CTkLabel(master=self.right_frame, text="Password", font=ctk.CTkFont(size=20, weight="bold"),text_color="#004643")
        self.label_pass.place(relx=0.2, rely=0.48)


        #button login
        self.btn_log = ctk.CTkButton(master=self.right_frame,width=50,height=40,text="LOG IN",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"),command=self.login)
        self.btn_log.place(relx=0.2, rely=0.7)

        self.btn_guest = ctk.CTkButton(master=self.right_frame,width=50,height=40,text="GUEST",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), command=self.guest)
        self.btn_guest.place(relx=0.55, rely=0.7)

        self.btn_about_us = ctk.CTkButton(master=self.right_frame,width=50,height=40,text="ABOUT US",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), command=self.about_us)
        self.btn_about_us.place(relx=0.335, rely=0.85)

        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=40,text="EXIT",text_color="#abd1c6", fg_color="#004643",corner_radius=10,font=ctk.CTkFont(size=15,weight="bold"), command=self.btn_exit)
        self.btn_back.place(relx=0.01, rely=0.91)


    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")

        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.clock_date.after(1000, self.display_time)


    def clear(self):
        self.entry_pass.delete(0,"end") 
        self.entry_user.delete(0,"end") 

    def login(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()
        logindata = {
            'username': username,
            'password': password
        }
        if username == "" or  password == "":
            messageBox.show("Warning","Username or password is empty","warn")
        else:
            try:
                response = requests.post(login_URL,json=logindata)
                if response.status_code == 200:
                    token = response.json()
                    a = u.Authorization.split(' ')
                    a[1] = token['token']
                    a = " ".join(a)
                    u.Authorization = a
                    print(u.Authorization) 
                    print(token)    
                    if "admin" in token["role"]:
                        messageBox.show("Information","Welcome "+token['name'],"info")
                        self.destroy()
                        import dashboard_admin as da
                        da.main()
                    elif "master" in token["role"]:
                        messageBox.show("Warning","Welcome "+ token['name'],"info")
                        self.destroy()
                        import dashboard_master_admin as dma
                        dma.main()
                else:
                    messageBox.show("Warning","Username or password wrong","warn")
            except:
                messageBox.show("Warning","Server Error","warn")
            self.clear()
    def guest(self):
        messageBox.show("Information","Wellcome, Guest","info")
        self.destroy()
        import control_guest as g
        g.main()

    def about_us(self):
        self.destroy()
        import about as a
        a.main()

    def btn_exit(self):
        self.destroy()
        u.Loop = 0
def main():
    app =App()
    app.mainloop()

