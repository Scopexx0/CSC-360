import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hawk's Test App")
        self.minsize(720, 480)

        # create 2x2 grid system
        self.grid_rowconfigure(0)
        self.grid_columnconfigure(0)

        self.button = customtkinter.CTkButton(master=self, text=1, command=self.button_callback)
        self.button.grid(row=1, column=5, padx=1, pady=1)

        self.button = customtkinter.CTkButton(master=self, text=2, command=self.button_callback)
        self.button.grid(row=2, column=1, padx=1, pady=1)


    def button_callback(self):
        print("button pressed")


if __name__ == "__main__":
    app = App()
    app.mainloop()