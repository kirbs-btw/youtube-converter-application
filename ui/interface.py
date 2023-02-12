import tkinter as tk
from tkinter import ttk
# import converte / trying to find the syntax to import prev folder

def do_conversion(link, path):
    # converter(link ,path)
    pass

def start_app():
    root = tk.Tk()

    root.geometry('500x500')

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    # title

    # input for link

    link_input = ttk.Entry(canvas)
    link_input.pack(side = tk.TOP ,ipadx = 30, ipady = 6)

    # input for the output folder 
    # will be saved for the next time

    folder_input = ttk.Entry(canvas)
    folder_input.pack(side = tk.TOP, ipadx = 30, ipady = 6)

    # format choosing drop down

    # convert button 
    
    convert_button = ttk.Button(canvas, text="convert", command=lambda: do_conversion(link_input.get(), folder_input.get()))
    convert_button.pack(side = tk.TOP, ipadx = 30, ipady = 6)

    # progress bar / no idea how this is gonna work but thats why we are here

    # footer with social links or something legal 

    root.mainloop()