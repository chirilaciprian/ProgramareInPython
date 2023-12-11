import tkinter as tk
from tkinter import ttk

class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Movies Rating App")
        
        # Define a custom color scheme
        bg_color = "#2E2E2E"  # Dark gray background
        fg_color = "white"   # White text
        button_color = "#3E3E3E"  # Slightly lighter gray for buttons
        font_style = ("Arial", 12)

        # Set the overall background color
        self.root.config(bg=bg_color)

        # Label
        self.mylabel = tk.Label(self.root, text="Enter movie title:", font=font_style, bg=bg_color, fg=fg_color)
        self.mylabel.pack(pady=10)

        # OptionMenu
        self.menu_var = tk.StringVar(self.root)
        self.menu_var.set("Movies")  # Default option
        self.menu = ttk.Combobox(self.root, textvariable=self.menu_var, values=["Movies", "Actors"])
        self.menu.config(font=font_style, background=button_color, foreground=fg_color, width=15)
        self.menu.pack(pady=10)

        # Entry
        self.myentry = tk.Entry(self.root, font=font_style, bg=button_color, fg=fg_color)
        self.myentry.pack(pady=10)

        # Button
        self.submit = tk.Button(self.root, text="Search", font=font_style, command=self.get_entry_text, bg=button_color, fg=fg_color)
        self.submit.pack(pady=10)

        self.root.mainloop()

    def get_entry_text(self):
        entry_text = self.myentry.get()
        selected_option = self.menu_var.get()
        print(entry_text)  # Replace with your desired logic
        print(selected_option)  # Print the selected option
        self.myentry.delete(0, tk.END)  # Clear the entry field

MyGui()