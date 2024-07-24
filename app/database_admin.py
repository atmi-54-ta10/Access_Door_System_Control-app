from tkinter import ttk
import tkinter.messagebox as tkmb
import customtkinter as ctk
import os
from datetime import datetime
import requests
from CTkTable import *
from PIL import Image
import uri as u
import messageBox
ctk.set_appearance_mode("System")

get_data_url = u.api_uri+"user/all_guest"



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #inisiasi 
        self.name_user = []
        self.job_user = []
        self.id_number_user =[]
        self.id_user =[]
        self.jumlah_data = 0
        self.rows_per_page = u.row_per_pages


        job = ["Karyawan","TMI","TMK","PM","RTM","TPM","TRMK"]
        
        

        self.title("Database page")
        self.configure(fg_color="#abd1c6")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False)
        self.wm_attributes('-fullscreen','true')


         #inisiasi gambar log out
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
       
         #inisiasi gambar add data
        self.logo_image_adddata = ctk.CTkImage(Image.open(os.path.join(image_path, "add-user putih.png")), size=(100, 100))

         #inisiasi gambar remove data
        self.logo_image_delete = ctk.CTkImage(Image.open(os.path.join(image_path, "delete-user putih.png")), size=(100, 100))

        #inisiasi gambar edit data
        self.logo_image_edit = ctk.CTkImage(Image.open(os.path.join(image_path, "database putih.png")), size=(100, 100))

        #inisiasi gambar Data logging
        self.logo_image_datalogging = ctk.CTkImage(Image.open(os.path.join(image_path, "Data_logging putih.png")), size=(100, 100))

        #background
        self.main_frame = ctk.CTkFrame(master=self,height=600,width=1024,fg_color="#abd1c6")
        self.main_frame.place(relx=0, rely=0)

        self.tab_view = ctk.CTkTabview(master=self.main_frame, corner_radius=5, width=460, height=480, fg_color="#004643",
                                       text_color="#ffffff", segmented_button_fg_color="#004643",
                                       segmented_button_unselected_color="#004643",
                                       segmented_button_selected_color="#00aaa1",
                                       segmented_button_selected_hover_color="#f9bc60",
                                       segmented_button_unselected_hover_color="#f9bc60")
        self.tab_view.place(relx=0.06, rely=0.1)
        
        self.table_user()
            
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
        
        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Database", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)

        #button add data
        self.btn_add_data = ctk.CTkButton(master=self.main_frame,width=200,height=200,text="ADD",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_adddata,compound="top", command=self.add_data)
        self.btn_add_data.place(relx=0.75, rely=0.16)

        #button delete data
        self.btn_delete_data = ctk.CTkButton(master=self.main_frame,width=200,height=200,text="DELETE",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_delete,compound="top", command=self.del_data)
        self.btn_delete_data.place(relx=0.64, rely=0.55)

        #  #button data logging
        # self.btn_datalogging = ctk.CTkButton(master=self.main_frame,width=200,height=200,text="DATA LOG",text_color="#ffffff", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_datalogging,compound="top", command=self.data_log)
        # self.btn_datalogging.place(relx=0.75, rely=0.55)

        #button edit data
        self.btn_edit_data = ctk.CTkButton(master=self.main_frame,width=200,height=200,text="EDIT DATA",text_color="#abd1c6", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_edit,compound="top", command= self.edit_data)
        self.btn_edit_data.place(relx=0.53, rely=0.16)

        #button back 
        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#abd1c6", fg_color="#004643",corner_radius=10,font=ctk.CTkFont(size=20,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.02, rely=0.91)


    def create_pages(self):
        pages = []
        for i in range(0, self.jumlah_data, self.rows_per_page):
            page_data = []
            for j in range(self.rows_per_page):
                if i + j < self.jumlah_data:
                    page_data.append([self.name_user[i + j], self.job_user[i + j], self.id_number_user[i + j]])
            pages.append(page_data)
        return pages

    def refresh_data(self):
        response = requests.get(get_data_url,headers={"Authorization":u.Authorization})
        data = response.json()

         # Destroy existing tabs
        a = 0 if self.jumlah_data % self.rows_per_page == 0 else 1

        for i in range((self.jumlah_data // self.rows_per_page) + a):
            self.tab_view.delete(f"Page {i+1}")

    def table_user(self):
        self.name_user.clear()
        self.job_user.clear()
        self.id_number_user.clear()
        self.id_user.clear()

        self.head = ["Name", "Job", "ID Number"]


        response = requests.get(get_data_url,headers={"Authorization":u.Authorization})
        data = response.json()

        self.name_user = [item.get('name', 'Unknown') for item in data]
        self.job_user = [item.get('job', 'Unknown') for item in data]
        self.id_number_user = [item.get('id_number', 'Unknown') for item in data]
        self.id_user = [item.get('_id', 'Unknown') for item in data]
        self.jumlah_data = len(data)

        self.pages = self.create_pages()

        for i, page_data in enumerate(self.pages, start=1):
            tab_name = f"Page {i}"
            self.tab_view.add(tab_name)
            tab_frame = self.tab_view.tab(tab_name)
            table = CTkTable(master=tab_frame, row=len(page_data) + 1, column=len(self.head),
                             values=[self.head] + page_data, corner_radius=5, padx=0, pady=0,
                             header_color="#00aaa1", colors=["#ffffff", "#ffffff"], text_color="#000000",
                             justify="center", hover_color="#f9bc60",font=ctk.CTkFont(size=13))
            table.pack(padx=5, pady=5)
  

    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")

        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.clock_date.after(1000, self.display_time)

    def add_data(self):
        self.destroy()
        import dt_add_admin as ada
        ada.main()

    def del_data(self):
        self.destroy()
        import dt_del_admin as da
        da.main()

    def edit_data(self):
        self.destroy()
        import dt_edit_admin as ea
        ea.main()

    def data_log(self):
        self.destroy()
        import datalog_admin as dla
        dla.main()

    def btnback (self):
        self.destroy()
        import dashboard_admin as dsa
        dsa.main()    


def main():
    app = App()
    app.mainloop()
