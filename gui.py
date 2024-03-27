import customtkinter

# app settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# tkinter window
# app = tkinter.Tk()

# window sets
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Hawk's meals")
app.configure(fg_color="yellow")

# title frame
ttl_frame = customtkinter.CTkFrame(app)

# # adding UI elements
title = customtkinter.CTkLabel(app, text="Hawk's Meals", font=("Arial", 35), text_color="black", bg_color="grey")
title.pack(padx=10, pady=50)

# Day entry
day = customtkinter.CTkEntry(app, corner_radius=10, placeholder_text="Enter day", placeholder_text_color="white")
day.pack(pady=10)

# black frame
blck_frame = customtkinter.CTkFrame(app, width=600, height=400)
blck_frame.pack()
blck_frame.pack_propagate(False)

# Entry Calories (Example)
entry_calories = customtkinter.CTkEntry(blck_frame, corner_radius=10, placeholder_text="Enter meal", placeholder_text_color='white')
entry_calories.pack(pady=10)

# # Button results
but = customtkinter.CTkButton(blck_frame, text="Results")
but.pack(padx=10, pady=10, side='bottom')

# def checkbox_event():
#     print("checkbox toggled, current value:", check_var.get())

# check_var = customtkinter.StringVar(value="on")
# checkbox = customtkinter.CTkCheckBox(app, text="CTkCheckBox", command=checkbox_event,
#                                      variable=check_var, onvalue="on", offvalue="off")
# checkbox.pack()


# # running app
app.mainloop()