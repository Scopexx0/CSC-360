import pandas as pd
import sqlite3
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# day_variable = ''

class TitleFrame(customtkinter.CTkFrame):
    def __init__(self, master, app_instance, **kwargs):
        self.app_instance = app_instance
        super().__init__(master, **kwargs, fg_color='yellow')

        # Title Label
        self.title = customtkinter.CTkLabel(self, text="Hawk's Meals", font=("Arial", 35), text_color="black", bg_color="grey")
        self.title.pack(padx=10, pady=50)

        # Days Button
        self.day_button = customtkinter.CTkSegmentedButton(self, values=['Mon', 'Tue',
                                                                        'Wed', 'Thu',
                                                                        'Fri', 'Sat', 'Sun'],
                                                           command=self.day_entry)
        self.day_button.pack()

    # Day entry
    def day_entry(self, value):
        self.app_instance.pass_day(value)


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, width=600, height=400)
        
        # Frame config
        self.grid_propagate(False)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Meals buttons
        self.breakfast = customtkinter.CTkButton(self, text='BreakFast', command=lambda: self.show_options('Breakfast'))
        self.lunch = customtkinter.CTkButton(self, text='Lunch', command=lambda: self.show_options('Lunch'))
        self.dinner = customtkinter.CTkButton(self, text='Dinner', command=lambda: self.show_options('Dinner'))
        self.breakfast.grid(row=0, column=0, ipadx=20)
        self.lunch.grid(row=0, column=1, ipadx=20)
        self.dinner.grid(row=0, column=2, ipadx=20)

        # Meal type for calories_button()
        self.mt = ''

        # Day variable from TitleFrame
        self.day_variable = ''

        # Create boxes_frame attribute
        self.boxes_frame = customtkinter.CTkScrollableFrame(self, width=400, height=200)
        self.boxes_frame.grid(row=1, column=1)

        # Results button.
        self.res_button = customtkinter.CTkButton(self, text='Results', command=lambda: self.calories_button())
        self.res_button.grid(row=2, column=1)

        # Lists to store the indexes
        self.checkbox_vars = {}
        self.checked_rows = []
        self.checked_oids = {}
        # print('xxx', day_variable)

    def show_options(self, meal_type):
        # Dont print results if day not choosen
        if(self.day_variable == ''):
            return
        # Pass the meal type to mt for later use in calories_button()
        self.mt = meal_type
        # Reset dicts/lists whenever meal button is pressed.
        self.reset()
        # Clear previous options if any
        for widget in self.boxes_frame.winfo_children():
            widget.destroy()

        # Connect to the database
        conn = sqlite3.connect('hawks.db')
        c = conn.cursor()
        # print('day var = ', self.day_variable)
        # Execute query to retrieve options based on meal type
        c.execute(f"SELECT oid, * FROM meals_data WHERE Day LIKE ? AND meal = ?", ('%'+self.day_variable+'%', meal_type,))
        options = c.fetchall()

        if ((self.day_variable == 'Sat' or self.day_variable == 'Sun') and (meal_type == 'Lunch')):
            e_label = customtkinter.CTkLabel(self.boxes_frame, text='There is no lunch, plase select Breakfast instead')
            e_label.pack(expand=True, fill='both')
        else:
            # Display options in the options frame [3 -> 'Name']
            for i, option in enumerate(options):
                box_var = customtkinter.IntVar()
                label = customtkinter.CTkCheckBox(self.boxes_frame, text=option[3], variable=box_var,
                                                command=lambda opt=option[0], index=i: self.checkbox_changed(index, opt),)
                label.pack(expand=True, fill='both')
                self.checkbox_vars[i] = box_var

        # print(self.checkbox_vars)
        # Close the database connection
        conn.close()

    # Save the row checked into the list.
    def checkbox_changed(self, row, oid):
        if self.checkbox_vars[row].get() == 1:
            self.checked_rows.append(row)
            self.checked_oids[row] = oid
        else:
            self.checked_rows.remove(row)
            del self.checked_oids[row]
            
    # Reset the checked items.
    def reset(self):
        self.checkbox_vars.clear()
        self.checked_oids.clear()
        self.checked_rows.clear()

    # Receive day variable from the TitleFrame class through App class
    def receive_day(self, day):
        print("Selected day:", day)
        self.day_variable = day
        for widget in self.boxes_frame.winfo_children():
            widget.destroy()
        self.reset()

    # Results button that will show all the nutritional values.
    def calories_button(self):
        # Delete the boxes
        for widget in self.boxes_frame.winfo_children():
            widget.destroy()
        # Connect to the database
        conn = sqlite3.connect('hawks.db')
        c = conn.cursor()
        # Execute query to retrieve options based on meal type
        c.execute(f"SELECT oid, * FROM meals_data WHERE meal = ?", (self.mt,))
        options = c.fetchall()
        cals = 0 
        prot = 0
        carb = 0
        sug = 0 
        fat= 0
        for option in options:
            if(option[0] in self.checked_oids.values()):
                print('Checked = ', option[3])
                res_label = customtkinter.CTkLabel(self.boxes_frame, text=option[3])
                res_label.pack(expand=True, fill='both')
                cals += option[4]
                prot += option[5]
                carb += option[6]
                sug += option[7]
                fat += option[8]
        cal_values = customtkinter.CTkLabel(self.boxes_frame, text=(f"Total Calories: {cals}"))
        cal_values.pack(expand=True, fill='both')
        prot_values = customtkinter.CTkLabel(self.boxes_frame, text=(f"Total Protein: {prot}"))
        prot_values.pack(expand=True, fill='both')
        carb_values = customtkinter.CTkLabel(self.boxes_frame, text=(f"Total Carbs: {carb}"))
        carb_values.pack(expand=True, fill='both')
        sug_values = customtkinter.CTkLabel(self.boxes_frame, text=(f"Total Sugar: {sug}"))
        sug_values.pack(expand=True, fill='both')
        fat_values = customtkinter.CTkLabel(self.boxes_frame, text=(f"Total Fat: {fat}"))
        fat_values.pack(expand=True, fill='both')


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # window settings
        # height= self.winfo_screenheight() // 1.3
        # width= self.winfo_screenwidth() // 2
        # self.geometry("%dx%d" % (width,height))
        self.title("Hawk's meals")
        self.configure(fg_color="yellow")
        
        # Title Frame with title widgets.
        self.title_frame = TitleFrame(master=self, app_instance=self)
        self.title_frame.pack(padx=10, pady=50)

        # Main Frame with the meal information.
        self.main_frame = MainFrame(master=self)
        self.main_frame.pack()

    # Function to pass day to main frame
    def pass_day(self, day):
        self.main_frame.receive_day(day)


if __name__ == "__main__":
    app = App()
    app.mainloop()
# app = App()
# app.mainloop()