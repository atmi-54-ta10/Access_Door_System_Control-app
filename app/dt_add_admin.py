import tkinter.messagebox as tkmb
import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import requests
import uri as u
import messageBox 


ctk.set_appearance_mode("System")
job = ["Instructor", "Staff", "Student", "Other"]

add_URL = u.api_uri+"user/add_data"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #inisiasi 
        self.title("Add Data page")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False)
        self.configure(fg_color="#abd1c6")
        self.wm_attributes('-fullscreen','true')


         #inisiasi gambar log out
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
       
         #inisiasi gambar add data
        self.logo_image_adddata = ctk.CTkImage(Image.open(os.path.join(image_path, "add-user putih.png")), size=(100, 100))
        self.logo_image_clear = ctk.CTkImage(Image.open(os.path.join(image_path, "dust_putih.png")), size= (100,100))


        #background
        self.main_frame = ctk.CTkFrame(master=self,height=600,width=1024,fg_color="#abd1c6")
        self.main_frame.place(relx=0, rely=0)

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
        
        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Add data", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)

        #frame kiri
        self.frame_1 = ctk.CTkFrame(master=self.main_frame, height=500, width=400,corner_radius=20,fg_color="#004643")
        self.frame_1.place(relx=0.125, rely=0.1)
        #self.frame_1.place(relx=0.07, rely=0.115)
        self.icon1 = ctk.CTkLabel(self.frame_1,text="Create your Account",text_color="#abd1c6",font=ctk.CTkFont(size=30, weight="bold"))
        self.icon1.place(relx=0.15,rely=0.03)

                #entry name
        self.entry_name = ctk.CTkEntry(master=self.frame_1, placeholder_text="Name",height=35,width=370,fg_color="#004643", corner_radius=25, text_color="#abd1c6",font=ctk.CTkFont(size=15),border_color="#abd1c6")
        self.entry_name.place(relx=0.04, rely= 0.32)
        self.label_name = ctk.CTkLabel(master=self.frame_1, text="Name", font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_name.place(relx=0.06, rely=0.255)
        #ID Number
        self.entry_id_num = ctk.CTkEntry(master=self.frame_1, placeholder_text="ID Number",height=35,width=370,fg_color="#004643", corner_radius=25, text_color="#abd1c6",font=ctk.CTkFont(size=15),border_color="#abd1c6")
        self.entry_id_num.place(relx=0.04, rely= 0.455)
        self.label_id_num = ctk.CTkLabel(master=self.frame_1, text="ID Number", font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_id_num.place(relx=0.06, rely=0.39)

        #
        #
        #
       
        self.combobox_role = ctk.CTkComboBox(master=self.frame_1,values="guest",height=35, width=175, fg_color="#004643",text_color="#abd1c6",dropdown_fg_color="#004643",dropdown_text_color="#abd1c6", corner_radius=25,font=ctk.CTkFont(size=17),dropdown_font=ctk.CTkFont(size=17),border_color="#abd1c6")
        self.combobox_role.set(value="guest")
        self.combobox_role.place(relx=0.04,rely=0.59)
        self.label_role = ctk.CTkLabel(master=self.frame_1, text="Role",font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_role.place(relx=0.06, rely=0.525)

        #entry job
        self.combobox_job = ctk.CTkComboBox(master=self.frame_1,values=job,height=35, width=175, fg_color="#004643",text_color="#abd1c6",dropdown_fg_color="#004643",dropdown_text_color="#abd1c6",corner_radius=25,font=ctk.CTkFont(size=17),dropdown_font=ctk.CTkFont(size=17),border_color="#abd1c6")
        self.combobox_job.set(value="")    
        self.combobox_job.place(relx=0.52,rely=0.59)
        self.label_job = ctk.CTkLabel(master=self.frame_1, text="Job",font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_job.place(relx=0.52, rely=0.525  )

        self.begin()


        #entry role


        #tombol add data
        self.btn_add_data = ctk.CTkButton(master=self.main_frame,width=150,height=150,text="ADD",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_adddata,compound="top",command=self.req)
        self.btn_add_data.place(relx=0.7, rely=0.25)

        self.btn_clear_data = ctk.CTkButton(master=self.main_frame,width=150,height=150,text="Clear",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_clear,compound="top",command=self.clear)
        self.btn_clear_data.place(relx=0.7, rely=0.55)

        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#abd1c6", fg_color="#004643",corner_radius=10,font=ctk.CTkFont(size=20,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.02, rely=0.91)

    

    
    def btnback (self):
        self.destroy()
        import database_admin as da
        da.main()    

    

    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")

        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.clock_date.after(1000, self.display_time)


    def req(self):
        name = self.entry_name.get()
        job = self.combobox_job.get()
        roles = self.combobox_role.get()
        ni = self.entry_id_num.get()
        #print(ni)
        
        if name =="" or job =="" or ni == "":
            messageBox.show("Warning", "You must fill all the data","warn")
        else:
            add_data={
                "name":name,
                "id_number": ni,
                "job":job,
                "role":roles,
                "card":"0"
            }
            response = requests.post(add_URL,json=add_data,headers={"Authorization":u.Authorization})
            message = response.json()
            if response.status_code == 200:
                messageBox.show("Info", message["message"],"info")
            else:
                messageBox.show("Warning", message["message"],"warn")
           
        self.clear()
        self.begin()


    def clear(self):
        self.combobox_job.set(value="")    
        self.combobox_role.set(value="")
        self.entry_name.delete(0,"end")    
        self.entry_id_num.delete(0,"end")    
        self.begin()

    def begin(self):
        self.combobox_role.configure(state="disabled")
        self.combobox_role.set(value="guest")

            

def main():
    app = App()
    app.mainloop()

