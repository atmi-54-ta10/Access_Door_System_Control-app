import tkinter as tk
import tkinter.messagebox as tkmb
import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import requests
from CTkTable import *
from PIL import Image
import pytz
import uri as u
import messageBox

ctk.set_appearance_mode("System")

# get_data_url = u.api_uri+"user/all_user"
del_data_url = u.api_uri+"user/"
get_log_url = u.api_uri+"action/list"
get_csv = u.api_uri+"action/csv"
get_pdf = u.api_uri+"action/pdf"
get_excel = u.api_uri+"action/excel"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.id_log =[]
        self.name_user = []
        self.job_user = []
        self.platform_user = []
        self.action_user =[]
        self.time_log =[]
        self.date_log =[]
        self.name_slct= tk.StringVar()
        self.job_slct= tk.StringVar()
        self.id_number_slct= tk.StringVar()
        #inisiasi database
        job = ["Karyawan","TMI","TMK","PM","RTM","TPM","TRMK"]
        self.rows_per_page = u.row_per_pages
        self.jumlah_data = 0
        self.format_export = ['CSV','PDF','EXCEL']





        #inisiasi 
        self.title("Data LOG page")
        self.configure(fg_color="#abd1c6")
        self.geometry("1024x600+0+0")
        # self.resizable(False, False).
        self.wm_attributes('-fullscreen','true')

        

         #inisiasi gambar log out
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../icon")
       
         #inisiasi gambar add data
        self.logo_image_export_data = ctk.CTkImage(Image.open(os.path.join(image_path, "export_putih.png")), size=(40, 40))
        self.logo_image_clear = ctk.CTkImage(Image.open(os.path.join(image_path, "dust_putih.png")), size= (40,40))


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

        self.name_of_page = ctk.CTkLabel(master=self.main_frame,text="Datalogging", text_color="#004643",font=ctk.CTkFont(size=25, weight="bold"))
        self.name_of_page.place(relx=0.01, rely=0.01)

       
        self.tab_view = ctk.CTkTabview(master=self.main_frame, corner_radius=5, width=825, height=440, fg_color="#004643",
                                       text_color="#000000", segmented_button_fg_color="#abd1c6",
                                       segmented_button_unselected_color="#abd1c6",
                                       segmented_button_selected_color="#00aaa1",
                                       segmented_button_selected_hover_color="#f9bc60",
                                       segmented_button_unselected_hover_color="#f9bc60")
        self.tab_view.place(relx=0.03, rely=0.12)
        
        self.update_table()
      
        
        #tombol 

        self.combobox_form_export = ctk.CTkComboBox(master=self.main_frame,values=self.format_export, width=100,height=35, fg_color="#abd1c6",text_color="#000000",dropdown_fg_color="#ffffff",dropdown_text_color="#000000",corner_radius=25,font=ctk.CTkFont(size=15))
        self.combobox_form_export.set(value= self.format_export[0])
        self.combobox_form_export.place(relx=0.88,rely=0.5)


        self.btn_export_data = ctk.CTkButton(master=self.main_frame,width=100,height=70,text="Export",text_color="#ffffff", fg_color="#004643",corner_radius=20,font=ctk.CTkFont(size=12,weight="bold"), image=self.logo_image_export_data,compound="top", anchor="c", command= self.download_file)
        self.btn_export_data.place(relx=0.88, rely=0.57) 

        # self.btn_clear_data = ctk.CTkButton(master=self.main_frame,width=100,height=70,text="Clear",text_color="#000000", fg_color="#abd1c6",corner_radius=20,font=ctk.CTkFont(size=15,weight="bold"), image=self.logo_image_clear,compound="left")
        # self.btn_clear_data.place(relx=0.8, rely=0.87)


        self.btn_back = ctk.CTkButton(master=self.main_frame,width=80,height=50,text="BACK",text_color="#ffffff", fg_color="#004643",corner_radius=10,font=ctk.CTkFont(size=20,weight="bold"), command=self.btnback)
        self.btn_back.place(relx=0.02, rely=0.91)

    


    def create_pages(self):
        pages = []
        for i in range(0, self.jumlah_data, self.rows_per_page):
            page_data = []
            for j in range(self.rows_per_page):
                if i + j < self.jumlah_data:
                    page_data.append([self.date_log[i + j],self.time_log[i + j],self.name_user[i + j], self.job_user[i + j], self.platform_user[i + j],self.action_user[i + j]])
            pages.append(page_data)
        return pages

    def refresh_data(self):
         # Destroy existing tabs
        a = 0 if self.jumlah_data % self.rows_per_page == 0 else 1

        for i in range((self.jumlah_data // self.rows_per_page) + a):
            self.tab_view.delete(f"Page {i+1}")
        
        self.update_table()
        
    def update_table(self):
        self.name_user.clear()
        self.job_user.clear()
        self.platform_user.clear()
        self.action_user.clear()
        self.id_log.clear()
        del self.time_log
        del self.date_log
        self.jumlah_data = 0
        
        response = requests.get(get_log_url,headers={"Authorization":u.Authorization})
        data = response.json() 
        data = data[:10]
        
        self.jumlah_data= len(data)
        self.head = ["Date", "Time", "Name", "Job", "Platform", "Action"]
        self.rows_per_page = u.row_per_pages
        self.name_user = [item.get('name', 'Unknown') for item in data]
        self.job_user = [item.get('job', 'Unknown') for item in data]
        self.platform_user = [item.get('platform', 'Unknown') for item in data]
        self.action_user = [item.get('action', 'Unknown') for item in data]
        self.id_log = [item.get('_id', 'Unknown') for item in data]
        data_log = [(
            datetime.strptime(item['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
            .replace(tzinfo=pytz.utc)
            .astimezone(pytz.timezone('Asia/Jakarta'))
            .strftime("%Y-%m-%d"),
            
            datetime.strptime(item['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
            .replace(tzinfo=pytz.utc)
            .astimezone(pytz.timezone('Asia/Jakarta'))
            .strftime("%H:%M:%S")
        ) for item in data]
        if self.jumlah_data >0:
            self.date_log, self.time_log = zip(*data_log)
        
        
        self.head = ["Date", "Time", "Name", "job", "Platform", "Action"]

        self.pages = self.create_pages()

        # Update each table with the new data
        for i, page_data in enumerate(self.pages, start=1):
            tab_name = f"Page {i}"
            self.tab_view.add(tab_name)
            tab_frame = self.tab_view.tab(tab_name)
            table = CTkTable(master=tab_frame, row=len(page_data) + 1, column=len(self.head),
                             values=[self.head] + page_data, corner_radius=5, padx=0, pady=0,
                             header_color="#00aaa1", colors=["#ffffff", "#ffffff"], text_color="#000000",
                             justify="center", hover_color="#f9bc60",font=ctk.CTkFont(size=13))
            table.pack(padx=0, pady=0)
        if self.jumlah_data > 0:
            self.tab_view.set("Page 1")

    def btnback (self):
        self.destroy()
        import History_page_admin as da
        da.main() 


    def display_time(self):
        current_time = datetime.now().strftime("%H : %M :%S")
        current_date = datetime.now().strftime("%A, %d %B %Y")
       
        self.clock_time.configure(text=current_time)
        self.clock_date.configure(text=current_date)

        self.clock_date.after(1000, self.display_time)


    def download_file(self):
        form = self.combobox_form_export.get()
        filepath= '../../History/Data_Log/'
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        uri = ''
        print(form)
        if form !="":
            if form == self.format_export[0]:
                 uri =get_csv
            elif form == self.format_export[1]:
                uri = get_pdf
            elif form == self.format_export[2]:
                uri = get_excel
            else:
                messageBox.show("Information","Please select the format","warn")
            response = requests.get(uri)
            if "content-disposition" in response.headers:
                content_disposition = response.headers["content-disposition"]
                filename = content_disposition.split('"')[1]
                print(content_disposition.split('"')[1])
                print(type(filename))
               #  print(" ".join(filename))
            else:
                filename = get_pdf.split("/")[-1]
                print(filename)
            with open(filepath+filename, mode="wb") as file:
                file.write(response.content)
            print(f"Downloaded file {filename}")
            messageBox.show("Information","Success","info")
        else:
            messageBox.show("Information","Please select the format","warn")



def main():
    app = App()
    app.mainloop()