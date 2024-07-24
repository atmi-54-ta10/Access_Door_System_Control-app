import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import requests
from CTkTable import *
from PIL import Image
import uri as u
import messageBox

ctk.set_appearance_mode("System")

get_data_url = u.api_uri + "user/list_user"
del_data_url = u.api_uri + "user/"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #inisiasi 
        self.name_user = []
        self.job_user = []
        self.id_number_user =[]
        self.id_user =[]
        self.jumlah_data = 0      
        self.name_slct= tk.StringVar()
        self.job_slct= tk.StringVar()
        self.id_number_slct= tk.StringVar()
        job = ["Instructor", "Staff", "Student", "Other"]
        self.head = ["Name", "Job", "ID Number"]
        self.rows_per_page = u.row_per_pages
        self.nama_asli =""



        #inisiasi 
        self.title("Delete Data page")
        self.configure(fg_color="#004643")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False)
        self.wm_attributes('-fullscreen','true')


         #inisiasi gambar log out
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
       
         #inisiasi gambar add data
        self.logo_image_delete_data = ctk.CTkImage(Image.open(os.path.join(image_path, "delete-user putih.png")), size=(75, 75))
        self.logo_image_clear = ctk.CTkImage(Image.open(os.path.join(image_path, "dust_putih.png")), size= (75,75))


        #background
        self.main_frame = ctk.CTkFrame(master=self,height=600,width=1024,fg_color="#004643")
        self.main_frame.place(relx=0, rely=0)

        self.clock_frame = ctk.CTkFrame(master=self.main_frame, height=65, width=250,fg_color="#004643", border_color="#ffffff",border_width=3,corner_radius=0)
        self.clock_frame.place(relx=0.8, rely=0.005)
        self.clock_frame.grid_rowconfigure((0, 1), weight=1)
        self.clock_time = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#ffffff",font=ctk.CTkFont(size=25, weight="bold"))
        # self.clock_time.place(relx=0.26, rely=0.12)
        self.clock_time.grid(row=0,column=0,padx=20, pady=(5,0))
        self.clock_date = ctk.CTkLabel(master=self.clock_frame,text="", text_color="#ffffff",font=ctk.CTkFont(size=12, weight="bold"))
        # self.clock_date.place(relx=0.2, rely=0.5)
        self.clock_date.grid(row=1,column=0,padx=20,pady=(0,5))
        self.display_time()

        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Delete data", text_color="#abd1c6",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)

        self.frame_kanan = ctk.CTkFrame(master=self.main_frame, height=467, width=400,fg_color="#abd1c6")
        self.frame_kanan.place(relx=0.535, rely=0.12)

        #tabview kiri
        self.tab_view = ctk.CTkTabview(master=self.main_frame, corner_radius=5, width=460, height=480, fg_color="#abd1c6",
                                       text_color="#000000", segmented_button_fg_color="#abd1c6",
                                       segmented_button_unselected_color="#abd1c6",
                                       segmented_button_selected_color="#00aaa1",
                                       segmented_button_selected_hover_color="#f9bc60",
                                       segmented_button_unselected_hover_color="#f9bc60")
        self.tab_view.place(relx=0.06, rely=0.1)
        
        self.table_user()
        
        self.name = ctk.CTkEntry(master=self.frame_kanan, textvariable=self.name_slct,height=28,width=350,fg_color="#abd1c6", corner_radius=25, text_color="#004643",border_color="#004643",font=ctk.CTkFont(size=15),state="disabled")
        self.name.place(relx=0.04, rely= 0.1)
        self.label_name = ctk.CTkLabel(master=self.frame_kanan, text="Name", font=ctk.CTkFont(size=17, weight="bold"),text_color="#004643")
        self.label_name.place(relx=0.06, rely=0.04)
       
        self.job = ctk.CTkEntry(master=self.frame_kanan, textvariable=self.job_slct,height=30,width=350,fg_color="#abd1c6", corner_radius=25, text_color="#004643",border_color="#004643",font=ctk.CTkFont(size=15),state="disabled")
        self.job.place(relx=0.04,rely=0.24)
        self.label_job = ctk.CTkLabel(master=self.frame_kanan, text="job", font=ctk.CTkFont(size=17, weight="bold"),text_color="#004643")
        self.label_job.place(relx=0.06, rely=0.18)

        self.ni = ctk.CTkEntry(master=self.frame_kanan, textvariable=self.id_number_slct,height=28,width=350,fg_color="#abd1c6", corner_radius=25, text_color="#004643",border_color="#004643",font=ctk.CTkFont(size=15),state="disabled")
        self.ni.place(relx=0.04, rely= 0.38)
        self.label_role = ctk.CTkLabel(master=self.frame_kanan, text="ID Number", font=ctk.CTkFont(size=17, weight="bold"),text_color="#004643")
        self.label_role.place(relx=0.06, rely=0.32)
        #tombol 
        self.btn_delete_data = ctk.CTkButton(master=self.frame_kanan,width=150,height=150,text="Delete",text_color="#ffffff", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_delete_data,compound="top", anchor="c", command= self.del_data)
        self.btn_delete_data.place(relx=0.1, rely=0.65) 

        self.btn_clear_data = ctk.CTkButton(master=self.frame_kanan,width=150,height=150,text="Clear",text_color="#ffffff", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_clear,compound="top",command=self.clear)
        self.btn_clear_data.place(relx=0.5, rely=0.65)

        self.btn_back = ctk.CTkButton(master=self.main_frame,width=70,height=20,text="BACK",text_color="#000000", fg_color="#abd1c6",corner_radius=10,font=ctk.CTkFont(size=20,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.02, rely=0.93)

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
         # Destroy existing tabs
        a = 0 if self.jumlah_data % self.rows_per_page == 0 else 1

        for i in range((self.jumlah_data // self.rows_per_page) + a):
            self.tab_view.delete(f"Page {i+1}")

        self.table_user()

    def table_user(self):
        self.name_user.clear()
        self.job_user.clear()
        self.id_number_user.clear()
        self.id_user.clear()

        response = requests.get(get_data_url,headers={"Authorization":u.Authorization})
        data = response.json()

        self.name_user = [item.get('name', 'Unknown') for item in data]
        self.job_user = [item.get('job', 'Unknown') for item in data]
        self.id_number_user = [item.get('id_number', 'Unknown') for item in data]
        self.id_user = [item.get('_id', 'Unknown') for item in data]
        self.jumlah_data = len(data)

        self.pages = self.create_pages()

        # Update each table with the new data
        for i, page_data in enumerate(self.pages, start=1):
            tab_name = f"Page {i}"
            self.tab_view.add(tab_name)
            tab_frame = self.tab_view.tab(tab_name)
            table = CTkTable(master=tab_frame, row=len(page_data) + 1, column=len(self.head),
                             values=[self.head] + page_data, corner_radius=5, padx=0, pady=0,
                             header_color="#00aaa1", colors=["#ffffff", "#ffffff"], text_color="#000000",
                             justify="center", hover_color="#f9bc60",font=ctk.CTkFont(size=13),command=self.slct)
            table.pack(padx=5, pady=5)

        if self.jumlah_data > 0:
            self.tab_view.set("Page 1")

    def del_data(self):
        nama = self.name_slct.get()
        if nama != "":
            no = self.name_user.index(nama)
            id_USER = self.id_user[no]

            response = requests.delete(del_data_url+id_USER,headers={"Authorization":u.Authorization})
            message = response.json()
            if response.status_code == 200:
                messageBox.show("INFO",message["message"],"info")
            else:
                messageBox.show("WARNING",message["message"],"warn")
        else:
            messageBox.show("WARNING","Please Select the Table","warn")

        self.clear()
        self.refresh_data()
       
    def btnback (self):
        self.destroy()
        import database_master_admin as dma
        dma.main()    

    def clear(self):
        self.name_slct.set("")
        self.job_slct.set("")
        self.id_number_slct.set("")
        self.nama_asli =""

    def slct(self, choice):
        ca = choice["row"]
        current_page = self.tab_view.get().split(" ")
        cp = current_page[1]

        if ca > 0:
            adjusted_index = (int(cp)-1) * self.rows_per_page + ca - 1
            if 0 <= adjusted_index < len(self.name_user):
                self.name_slct.set(self.name_user[adjusted_index])
                self.nama_asli = self.name_slct.get()
                self.job_slct.set(self.job_user[adjusted_index])
                self.id_number_slct.set(self.id_number_user[adjusted_index])
                print(self.name_user[adjusted_index]+self.job_user[adjusted_index]+self.id_number_user[adjusted_index])

    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")
       
        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.clock_date.after(1000, self.display_time)
    

def main():
    app = App()
    app.mainloop()

