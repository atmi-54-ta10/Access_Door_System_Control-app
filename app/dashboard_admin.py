import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import uri as u 
import requests
ctk.set_appearance_mode("System")
lab_name = u.api_uri +"master/status"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #deklarasi
        self.title("Dashboard page")
        self.configure(fg_color="#ABD1C6")

        self.geometry("1024x600+0+0")
        # self.resizable(False,False)
        self.wm_attributes('-fullscreen','true')
        res = requests.get(lab_name)


        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
        self.logo_image_logout = ctk.CTkImage(Image.open(os.path.join(image_path, "logout putih.png")), size=(25, 25))

         #inisiasi gambar edit data
        self.logo_image_editdata = ctk.CTkImage(Image.open(os.path.join(image_path, "database putih.png")), size=(100, 100))

         #inisiasi gambar Control
        self.logo_image_control = ctk.CTkImage(Image.open(os.path.join(image_path, "control putih.png")), size=(100, 100))

        #inisiasi gambar monitoring
        self.logo_image_monitoring = ctk.CTkImage(Image.open(os.path.join(image_path, "monitor putih.png")), size=(100, 100))

         #inisiasi gambar settings
        self.logo_image_report = ctk.CTkImage(Image.open(os.path.join(image_path, "Data_logging putih.png")), size=(100, 100))

                 #inisiasi gambar settings
        self.logo_image_settings = ctk.CTkImage(Image.open(os.path.join(image_path, "settings putih.png")), size=(100, 100))



        #background
        self.main_frame = ctk.CTkFrame(master=self,height=600,width=1024,fg_color="#ABD1C6")
        self.main_frame.place(relx=0, rely=0)

         #button log out
        self.logout = ctk.CTkButton(master= self.main_frame,fg_color="#004643",text="Logout",text_color="#ABD1C6",font=ctk.CTkFont(size=20,weight="bold"),image=self.logo_image_logout,corner_radius=20,width=50,command=self.logout)
        self.logout.place(relx=0.85, rely=0.02)

        #jam 
        self.clock_frame = ctk.CTkFrame(master=self.main_frame, height=100, width=275,fg_color="#ABD1C6", border_color="#004643",border_width=3,corner_radius=0)
        self.clock_frame.place(relx=0.7, rely=0.16)
        self.clock_frame.grid_rowconfigure((0,1),weight=1)

        self.clock_time = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        # self.clock_time.place(relx=0.26, rely=0.15)
        self.clock_time.grid(row=0,column=0,padx=25,pady=(20,0))

        self.clock_date = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#004643",font=ctk.CTkFont(size=18, weight="bold"))
        self.clock_date.place(relx=0.1, rely=0.55)
        self.clock_date.grid(row=1,column=0,padx=25,pady=(0,20))

        self.display_time()

        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Dashboard", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)

        #label WElcome
        self.label_welcome = ctk.CTkLabel(master=self.main_frame, text="Welcome to, " + res.json()['lab']+ "\nLaboratory", text_color="#004643", font=ctk.CTkFont(size=30, weight="bold"),justify="left",wraplength=750)
        self.label_welcome.place(relx=0.07,rely=0.155)

        #button edit data
        self.btn_edit_data = ctk.CTkButton(master=self.main_frame,width=150,height=150,text="User Data",text_color="#ABD1C6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_editdata,compound="top", command= self.edit_data)
        self.btn_edit_data.place(relx=0.22, rely=0.68)

        #button Control
        self.btn_control = ctk.CTkButton(master=self.main_frame,width=150,height=150,text="Controlling",text_color="#ABD1C6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_control,compound="top", command= self.control)
        self.btn_control.place(relx=0.32, rely=0.38)

         #button Monitoring
        self.btn_monitoring = ctk.CTkButton(master=self.main_frame,width=150,height=150,text="Monitoring",text_color="#ABD1C6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_monitoring,compound="top", command=self.monitoring)
        self.btn_monitoring.place(relx=0.52, rely=0.38)

        #button setting
        self.btn_setting = ctk.CTkButton(master=self.main_frame,width=150,height=150,text="Setting",text_color="#ABD1C6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_settings,compound="top", command=self.setting)
        self.btn_setting.place(relx=0.42, rely=0.68)


        #button report
        self.btn_report = ctk.CTkButton(master=self.main_frame,width=150,height=150,text="History",text_color="#ABD1C6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_report,compound="top", command=self.report)
        self.btn_report.place(relx=0.62, rely=0.68)


    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")

        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.clock_date.after(1000, self.display_time)


    def logout(self):
        self.destroy()
        import login_page as lg
        lg.main()

    def edit_data(self):
        self.destroy()
        import database_admin as da
        da.main()

    def control(self):
        self.destroy()
        import control_admin as ca
        ca.main()

    def monitoring(self):
        self.destroy()
        import monitoring_admin as ma
        ma.main()
    
    def report(self):
        self.destroy()
        import History_page_admin as hpa
        hpa.main()

    def setting(self):
        self.destroy()
        import setting_admin as sa 
        sa.main()
   



def main():
    app =App()
    app.mainloop()

