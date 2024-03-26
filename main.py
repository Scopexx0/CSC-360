import tkinter
import customtkinter
# import PySimpleGUI as psg


# app settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Tkinter init
app = tkinter.Tk()

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Hawks meal")

title = customtkinter.CTkLabel(app, text="check")
title.pack(padx=10, pady=10)

# button
download = customtkinter.CTkButton(app, text="Button")
download.pack(padx=10, pady=10)  

# input
usr = customtkinter.CTkEntry(app, width=350, height=40)
usr.pack()

# running app
app.mainloop()
