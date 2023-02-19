import tkinter as tk
from tkinter import ttk
import converter.converter as conv
import sqlite3 as sql

def getConnection():
    conn = sql.connect("../sql/db.sql")
    return conn, conn.cursor()

def saveData():
    conn, cur = getConnection()
    
    
def loadData():
    conn, cur = getConnection()

def do_conversion(link, path, format):
    conv.converter(link, path, format)

def start_app():
    root = tk.Tk()
    root.title("youtube converter")

    root.geometry('250x300')

    canvas = tk.Canvas(root, highlightthickness=0)
    canvas.pack(side = tk.TOP, fill='both')

    # input for link

    link_lable = tk.Label(canvas, text="Insert Link here")
    link_lable.pack(side = tk.TOP, pady = [50, 3])

    link_input = ttk.Entry(canvas)
    link_input.pack(side = tk.TOP ,ipadx = 30, ipady = 6)

    # input for the output folder 
    # will be saved for the next time

    folderpath_lable = tk.Label(canvas, text="insert path here")
    folderpath_lable.pack(side = tk.TOP)

    folder_input = ttk.Entry(canvas)
    folder_input.pack(side = tk.TOP, ipadx = 30, ipady = 6)

    # format choosing drop down

    dropdown_menu_options = [
        None,
        ".mp3",
        ".wav",
        # add more endings
    ]

    variable = tk.StringVar(root)
    variable.set(dropdown_menu_options[1]) # default value

    file_ending_dropdown = ttk.OptionMenu(canvas, variable, *dropdown_menu_options)
    file_ending_dropdown.pack(side = tk.TOP, ipadx = 30, ipady = 6)

    # convert button 
    
    convert_button = ttk.Button(canvas, text="convert", command=lambda: do_conversion(link_input.get(), folder_input.get(), variable.get()))
    convert_button.pack(side = tk.TOP, ipadx = 30, ipady = 6)

    # progress bar / no idea how this is gonna work but thats why we are here

    # footer with social links or something legal 

    root.mainloop()