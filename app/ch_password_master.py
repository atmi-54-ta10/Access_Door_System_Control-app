import customtkinter as ctk
import os
from PIL import Image
from datetime import datetime
import requests
import uri as u 
import messageBox

cp_url = u.api_uri+"master/pw"

def show():
    chpw = ctk.CTkToplevel(fg_color="#66A5AD")
    chpw.geometry("450x300+240+150")
    chpw.title("Change Password")
    chpw.resizable(False,False)
    chpw.overrideredirect(True)
    chpw.tkraise()

    # Label dan entry untuk password
    label_pass = ctk.CTkLabel(master=chpw, text="Password", font=ctk.CTkFont(size=15, weight="bold"), text_color="#004643", anchor="center")
    label_pass.place(relx=0.2, rely=0.1)
    entry_pass = ctk.CTkEntry(chpw, placeholder_text="", width=275, height=40, fg_color="#ffffff", corner_radius=25, text_color="#000000", font=ctk.CTkFont(size=15), show="*")
    entry_pass.place(relx=0.2, rely=0.25)
    # Label dan entry untuk new password
    label_new_pass = ctk.CTkLabel(chpw, text="New Password", font=ctk.CTkFont(size=15, weight="bold"), text_color="#004643", anchor="center")
    label_new_pass.place(relx=0.2, rely=0.4)
    entry_new_pass = ctk.CTkEntry(chpw, placeholder_text="", width=275, height=40, fg_color="#ffffff", corner_radius=25, text_color="#000000", font=ctk.CTkFont(size=15), show="*")
    entry_new_pass.place(relx=0.2, rely=0.55)
    # Tombol untuk cancel dan ok
    def cancel():
        entry_new_pass.delete(0, "end")
        entry_pass.delete(0, "end")
        chpw.destroy()
    def ok():
        password = entry_pass.get()
        new_password = entry_new_pass.get()
        if password == new_password:
            messageBox.show("Information", "The New Password and Password same", 'info')
        else:
            body_json={
                "password": password,
                "new_password":new_password
            }
            res = requests.put(cp_url,json=body_json,headers={"Authorization":u.Authorization})
            message = res.json()
            if res.status_code == 200:
                messageBox.show("Information", message['message'],'info')
            else:
                messageBox.show("Information", message['message'],'warn')
            chpw.destroy()
            
        print(password + new_password)

        chpw.destroy()
    btn_cancel = ctk.CTkButton(chpw, text="Cancel", height=40, width=130, corner_radius=7, font=ctk.CTkFont(size=15, weight="bold"), text_color="#abd1c6", fg_color="#004643", command=cancel)
    btn_cancel.place(relx=0.5, rely=0.75)
    btn_ok = ctk.CTkButton(chpw, text="OK", height=40, width=130, corner_radius=7, font=ctk.CTkFont(size=15, weight="bold"), text_color="#abd1c6", fg_color="#004643", command=ok)
    btn_ok.place(relx=0.2, rely=0.75)

    # chpw.place_slaves()

    # chpw.focus_force()
    chpw.wait_window()