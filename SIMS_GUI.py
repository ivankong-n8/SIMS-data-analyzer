import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from file_reader import *

win = tk.Tk()
win.title("SIMS data analyzer")

data = None

def select_file(folder_name_tk):
    '''
    folder_name_tk: tk.StringVar()
    function: set folder_name to fname
    '''
    file_adr = filedialog.askopenfilename()
    # data = fr.data_SIMS(file_adr)
    print(file_adr)
    data_no_label.config(text=file_adr)
    folder_name_tk.set(file_adr)
    
folder_name_tk = tk.StringVar()
select_button = tk.Button(win, text= 'Select file', command = 
               lambda:select_file(folder_name_tk))
select_button.grid(column=0, row=0)

data_no_label = ttk.Label(win, text="Data Unloaded")
data_no_label.grid(column=0, row=1)

ylist_label = ttk.Label(win, text="Select Plot Data")
ylist_label.grid(column=1, row=0)

ylist_listbox = tk.Listbox(win, selectmode='MULTIPLE')
ylist_listbox.grid(column=1, row=1)

plot_button = tk.Button(win, text= 'Plot', command = 
               lambda:plot())
plot_button.grid(column=2, row=1)


win.mainloop()
