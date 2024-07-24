import asyncio
import tkinter as tk
import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import requests
import aiohttp
from CTkTable import *
from PIL import Image
import uri as u
import messageBox


ctk.set_appearance_mode("Dark")

get_data_url = u.api_uri +"user/list_user"
edit_data_url = u.api_uri +"user/"
scan_card_url = u.api_uri +"user/add_card/"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #inisiasi 
        self.name_user = []
        self.job_user = []
        self.nomor_induk_user =[]
        self.id_user =[]
        self.jumlah_data = 0
      
        
        
        self.name_slct= tk.StringVar()
        self.job_slct= tk.StringVar()
        self.nomor_induk_slct= tk.StringVar()

        job = ["Instructor", "Staff", "Student", "Other"]
        # job = ["Karyawan","TMI","TMK","PM","RTM","TPM","TRMK"]
        self.head = ["Name", "Job", "Nomor Induk"]
        self.rows_per_page = u.row_per_pages

       

        self.nama_asli =""
        #inisiasi 
        self.title("Edit Page Master Admin")
        self.configure(fg_color="#abd1c6")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False)
        self.wm_attributes('-fullscreen','true')
        


         #inisiasi gambar log out
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
       
         #inisiasi gambar add data
        self.logo_image_delete_data = ctk.CTkImage(Image.open(os.path.join(image_path, "edit_hitam.png")), size=(75, 75))
        self.logo_image_clear = ctk.CTkImage(Image.open(os.path.join(image_path, "dust_hitam.png")), size= (75,75))


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
        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Edit data", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)

        self.frame_kanan = ctk.CTkFrame(master=self.main_frame, height=465, width=400,fg_color="#004643")
        self.frame_kanan.place(relx=0.535, rely=0.12)

        #frame kiri
        self.tab_view = ctk.CTkTabview(master=self.main_frame, corner_radius=5, width=460, height=480, fg_color="#004643",
                                       text_color="#004643", segmented_button_fg_color="#004643",
                                       segmented_button_unselected_color="#004643",
                                       segmented_button_selected_color="#00aaa1",
                                       segmented_button_selected_hover_color="#f9bc60",
                                       segmented_button_unselected_hover_color="#f9bc60")
        self.tab_view.place(relx=0.06, rely=0.1)
        
        self.table_user()
 


        self.name = ctk.CTkEntry(master=self.frame_kanan, textvariable=self.name_slct,height=30,width=350,fg_color="#004643", corner_radius=25, text_color="#abd1c6",border_color="#abd1c6",font=ctk.CTkFont(size=15),state="normal")
        self.name.place(relx=0.04, rely= 0.1)
        self.label_name = ctk.CTkLabel(master=self.frame_kanan, text="Name", font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_name.place(relx=0.06, rely=0.04)
       
        self.label_job = ctk.CTkLabel(master=self.frame_kanan, text="job", font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_job.place(relx=0.06, rely=0.18)

        self.combobox_job = ctk.CTkComboBox(master=self.frame_kanan,values=job,height=30, width=350, fg_color="#004643",text_color="#abd1c6",dropdown_fg_color="#abd1c6",dropdown_text_color="#004643",border_color="#abd1c6",corner_radius=25,font=ctk.CTkFont(size=15),dropdown_font=ctk.CTkFont(size=15))
        self.combobox_job.set(value="")  
        self.combobox_job.place(relx= 0.04, rely= 0.24)
       
        self.ni = ctk.CTkEntry(master=self.frame_kanan, textvariable=self.nomor_induk_slct,height=30,width=350,fg_color="#004643", corner_radius=25, text_color="#abd1c6",font=ctk.CTkFont(size=15),state="normal",border_color="#abd1c6")
        self.ni.place(relx=0.04, rely= 0.38)
        self.label_ni = ctk.CTkLabel(master=self.frame_kanan, text="Nomor Induk", font=ctk.CTkFont(size=17, weight="bold"),text_color="#abd1c6")
        self.label_ni.place(relx=0.06, rely=0.32)
        #tombol 
        self.btn_edit_data = ctk.CTkButton(master=self.frame_kanan,width=150,height=150,text="Edit",text_color="#004643", fg_color="#abd1c6",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_delete_data,compound="top", anchor="c", command= self.edit_data)
        self.btn_edit_data.place(relx=0.1, rely=0.5) 

        self.btn_clear_data = ctk.CTkButton(master=self.frame_kanan,width=150,height=150,text="Clear",text_color="#004643", fg_color="#abd1c6",corner_radius=20,font=ctk.CTkFont(size=20,weight="bold"), image=self.logo_image_clear,compound="top",command=self.clear)
        self.btn_clear_data.place(relx=0.5, rely=0.5)

        self.btn_scan_card = ctk.CTkButton(master=self.frame_kanan,width=100,height=50,text="Scan Card",text_color="#004643", fg_color="#abd1c6",corner_radius=20,font=ctk.CTkFont(size=15,weight="bold"), command= self.scan_rfid)
        self.btn_scan_card.place(relx=0.35, rely=0.85)


        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#abd1c6", fg_color="#004643",corner_radius=10,font=ctk.CTkFont(size=20,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.02, rely=0.91)

    

    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")
       
        # Pembaruan tampilan dengan variabel Tkinter
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        # Setel pembaruan berikutnya
        self.clock_date.after(1000, self.display_time)

    def create_pages(self):
        pages = []
        for i in range(0, self.jumlah_data, self.rows_per_page):
            page_data = []
            for j in range(self.rows_per_page):
                if i + j < self.jumlah_data:
                    page_data.append([self.name_user[i + j], self.job_user[i + j], self.nomor_induk_user[i + j]])
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
        self.nomor_induk_user.clear()
        self.id_user.clear()

        response = requests.get(get_data_url,headers={"Authorization":u.Authorization})
        data = response.json()

        self.name_user = [item.get('name', 'Unknown') for item in data]
        self.job_user = [item.get('job', 'Unknown') for item in data]
        self.nomor_induk_user = [item.get('nomor_induk', 'Unknown') for item in data]
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
        

    def edit_data(self):
        nama = self.name_slct.get()
        
        if nama != "":
            if self.nama_asli in self.name_user:
                no_id = self.name_user.index(self.nama_asli)
                job = self.combobox_job.get()
                ni = self.nomor_induk_slct.get()
                id_USER = self.id_user[no_id]
                edit_json = {
                    'name':nama,
                    'job':job,
                    'nomor_induk':ni
                }

                response = requests.put(edit_data_url+id_USER,edit_json,headers={"Authorization":u.Authorization})
                message = response.json()
                if response.status_code == 200:
                    messageBox.show("INFO",message["message"],"info")
                    self.clear()
                else:
                    messageBox.show("WARNING",message["message"],"warn")
                    self.clear()
            elif self.nama_asli == "":
                messageBox.show("WARNING","Please select the table","warn")

            else:
                messageBox.show("WARNING","Name not in data","warn")

        else:
            messageBox.show("WARNING","Please Select the Table","warn")
        self.refresh_data()

    def slct(self, choice):
        ca = choice["row"]
        current_page = self.tab_view.get().split(" ")
        cp = current_page[1]

        
        if ca > 0:
            adjusted_index = (int(cp)-1) * self.rows_per_page + ca - 1
            if 0 <= adjusted_index < len(self.name_user):
                self.name_slct.set(self.name_user[adjusted_index])
                self.nama_asli = self.name_slct.get()
                self.nomor_induk_slct.set(self.nomor_induk_user[adjusted_index])
                self.combobox_job.set(self.job_user[adjusted_index])
                print(self.name_user[adjusted_index]+self.job_user[adjusted_index]+self.nomor_induk_user[adjusted_index])

    def btnback (self):
        self.destroy()
        import database_admin as da
        da.main()    

    def clear(self):
        self.name_slct.set("")
        self.job_slct.set("")
        self.nomor_induk_slct.set("")
        self.nama_asli =""
        self.combobox_job.set("")

    async def scan_rfid_async(self, url):
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url,headers={"Authorization":u.Authorization}) as response:
                    self.display_time()
                    return await response.json()
        except Exception as e:
            return {"message": str(e)}

        
    async def on_scan_rfid(self):
        nama = self.name_slct.get()
        if nama != "":
            if self.nama_asli in self.name_user:
                no_id = self.name_user.index(self.nama_asli)
                id_USER = self.id_user[no_id]
                data = await self.scan_rfid_async(scan_card_url+id_USER,headers={"Authorization":u.Authorization}) 
                # self.loading_top.destroy()

                messageBox.show("INFO", data['message'], "info")
                self.clear()    

        else:
            messageBox.show("WARNING", "Please Select the Table", "warn")
            self.clear()


    def coba (self):
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
        self.logomsb = ctk.CTkImage(Image.open(os.path.join(image_path, "info.png")), size=(50, 50))

        self.loading_top = ctk.CTkToplevel(fg_color= "#66A5AD")
        self.loading_top.title("Information")
        self.loading_top.geometry("400x180+1000+500")
        self.loading_top.resizable(False,False)
        self.loading_top.place_slaves()
        self.loading_top.grab_set()
        self.loading_frame = ctk.CTkFrame(master=self.loading_top,fg_color= "#004643",height=100, width=350,corner_radius=20)
        self.loading_frame.place(relx=0.065,rely=0.1)
        self.message = ctk.CTkLabel(master=self.loading_frame,text="Wait for tap..",text_color="#ffffff",image=self.logomsb, compound="left", font = ctk.CTkFont(size=15, weight="bold"))
        self.message.place(relx=0.1,rely=0.2)

    def scan_rfid(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.on_scan_rfid())
        loop.close()
        self.refresh_data()
        self.clear()


def main():
    app = App()
    app.mainloop()
