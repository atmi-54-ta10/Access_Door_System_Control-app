import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
from PIL import Image
import requests

ctk.set_appearance_mode("System")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        
        self.a = """The Access Door System developed in this Final Project is based on Raspberry Pi, which serves as the main server to manage door access, monitor temperature, and perform various other functions. This system is designed to provide full control and ease of use for its users. Raspberry Pi was chosen for its reliable capabilities as a central controller, capable of processing and executing various complex functions efficiently. In this system, the Raspberry Pi not only acts as the main server but also as a device that displays information and operational status through a Waveshare screen and a monitor located at the lab door. This screen facilitates direct on-site monitoring, providing real-time information about lab conditions, the presence of the lab master, and the current lab practice session. This integration makes the system more user-friendly and informative for users on site.

In addition to the monitor located at the door, the system can be accessed via a website and an Android application. Users can open the door, monitor the temperature, and perform other functions from anywhere using their devices. The website and Android application are developed to provide an intuitive and responsive interface, ensuring a smooth and efficient user experience. This project uses an API for communication between the client and the database."""
        self.text_raka="""Name: Agustinus Raka\nNIM: 20212003\nJobdesk: The Key"""
        self.text_farhan="""Name: Farhan Satria Ardhi\nNIM: 20212022\nJobdesk: Desktop app, API,\n\tand python program"""
        self.text_mario="""Name: Mario Putra Wibawa\nNIM: 20212030\nJobdesk: Website (Frontend)"""
        self.text_pipin="""Name: Pipin Wanodia\nNIM: 20212038\nJobdesk: Mobile APP (Android)"""
        
        #inisiasi 

        self.title("About Us page")
        self.configure(fg_color="#004643")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False).
        self.wm_attributes('-fullscreen','true')

        

         #inisiasi gambar log out
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../assets")
       
         #inisiasi gambar add data
        self.raka_image = ctk.CTkImage(Image.open(os.path.join(image_path, "raka.png")), size=(350, 350))
        self.farhan_image = ctk.CTkImage(Image.open(os.path.join(image_path, "farhan.png")), size=(350, 350))
        self.mario_image = ctk.CTkImage(Image.open(os.path.join(image_path, "mario.png")), size=(350, 350))
        self.pipin_image = ctk.CTkImage(Image.open(os.path.join(image_path, "pipin.png")), size=(350, 350))


        #background
        self.main_frame = ctk.CTkFrame(master=self,height=600,width=1024,fg_color="#004643")
        self.main_frame.place(relx=0, rely=0)

        self.clock_frame = ctk.CTkFrame(master=self.main_frame, height=65, width=250,fg_color="#004643", border_color="#abd1c6",border_width=3,corner_radius=0)
        self.clock_frame.place(relx=0.8, rely=0.005)
        self.clock_frame.grid_rowconfigure((0, 1), weight=1)
        self.clock_time = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"))
        # self.clock_time.place(relx=0.26, rely=0.12)
        self.clock_time.grid(row=0,column=0,padx=20, pady=(5,0))
        self.clock_date = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#abd1c6",font=ctk.CTkFont(size=12, weight="bold"))
        # self.clock_date.place(relx=0.2, rely=0.5)
        self.clock_date.grid(row=1,column=0,padx=20,pady=(0,5))

        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="About Us", text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)
       
        self.tab_view = ctk.CTkTabview(master=self.main_frame, corner_radius=5, width=825, height=440, fg_color="#abd1c6",
                                       text_color="#000000", segmented_button_fg_color="#abd1c6",
                                       segmented_button_unselected_color="#abd1c6",
                                       segmented_button_selected_color="#00aaa1",
                                       segmented_button_selected_hover_color="#f9bc60",
                                       segmented_button_unselected_hover_color="#f9bc60")
        self.tab_view.place(relx=0.04, rely=0.12)
        self.tab_view.add("Project")
        self.tab_view.add("Raka")
        self.tab_view.add("Farhan")
        self.tab_view.add("Mario")
        self.tab_view.add("Pipin")


        self.header_label= ctk.CTkLabel(master = self.tab_view.tab("Project"), text_color= "#004643", text="About Us")
        self.header_label.place(relx=0.02,rely=0.001)

        self.about_text = ctk.CTkLabel(master=self.tab_view.tab("Project"),text=self.a, text_color="#004643",font=ctk.CTkFont(size=17),wraplength=800, justify="center")
        self.about_text.place(relx=0.01,rely=0.1)

        #Raka
        self.tab_view.tab("Raka").grid_columnconfigure((0,1), weight=1)
        self.tab_view.tab("Raka").grid_rowconfigure(0, weight=1)

        self.about_raka_label = ctk.CTkLabel(master=self.tab_view.tab("Raka"),text=self.text_raka, text_color="#004643",font=ctk.CTkFont(size=30),wraplength=800, justify="left")
        self.about_raka_label.grid(row=0,column=1)
        self.about_raka_image= ctk.CTkLabel(master = self.tab_view.tab("Raka"),  text="", image=self.raka_image)
        self.about_raka_image.grid(row=0,column=0)

        #Farhan
        self.tab_view.tab("Farhan").grid_columnconfigure((0,1), weight=1)
        self.tab_view.tab("Farhan").grid_rowconfigure(0, weight=1)

        self.about_Farhan_label = ctk.CTkLabel(master=self.tab_view.tab("Farhan"),text=self.text_farhan, text_color="#004643",font=ctk.CTkFont(size=30),wraplength=800, justify="left")
        self.about_Farhan_label.grid(row=0,column=1)
        self.about_Farhan_image= ctk.CTkLabel(master = self.tab_view.tab("Farhan"),  text="", image=self.farhan_image)
        self.about_Farhan_image.grid(row=0,column=0)

        #Mario
        self.tab_view.tab("Mario").grid_columnconfigure((0,1), weight=1)
        self.tab_view.tab("Mario").grid_rowconfigure(0, weight=1)

        self.about_Mario_label = ctk.CTkLabel(master=self.tab_view.tab("Mario"),text=self.text_mario, text_color="#004643",font=ctk.CTkFont(size=30),wraplength=800, justify="left")
        self.about_Mario_label.grid(row=0,column=1)
        self.about_Mario_image= ctk.CTkLabel(master = self.tab_view.tab("Mario"),  text="", image=self.mario_image)
        self.about_Mario_image.grid(row=0,column=0)

        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#004643", fg_color="#abd1c6",corner_radius=10,font=ctk.CTkFont(size=20,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.02, rely=0.91)
        self.display_time()

        #pipin
        self.tab_view.tab("Pipin").grid_columnconfigure((0,1), weight=1)
        self.tab_view.tab("Pipin").grid_rowconfigure(0, weight=1)

        self.about_Pipin_label = ctk.CTkLabel(master=self.tab_view.tab("Pipin"),text=self.text_pipin, text_color="#004643",font=ctk.CTkFont(size=30),wraplength=800, justify="left")
        self.about_Pipin_label.grid(row=0,column=1)
        self.about_Pipin_image= ctk.CTkLabel(master = self.tab_view.tab("Pipin"),  text="", image=self.pipin_image)
        self.about_Pipin_image.grid(row=0,column=0)

        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#004643", fg_color="#abd1c6",corner_radius=10,font=ctk.CTkFont(size=20,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.02, rely=0.91)
        self.display_time()

    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")
       
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        self.clock_date.after(1000, self.display_time)


    def btnback (self):
        self.destroy()
        import login_page as lg
        lg.main() 

  



def main():
    app = App()
    app.mainloop()
