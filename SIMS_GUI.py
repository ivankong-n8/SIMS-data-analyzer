import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import file_reader as fr

win = tk.Tk()
win.title("SIMS data analyzer")

def select_file(folder_name_tk):
    '''
    folder_name_tk: tk.StringVar()
    function: set folder_name to fname
    '''
    file_adr = filedialog.askopenfilename()
    global data
    data = fr.data_SIMS(file_adr)
    print(file_adr)
    data_no_label.config(text=data.no)
    
    list_num = ylist_listbox.size()
    ylist_listbox.delete(0,list_num-1)      # clear former list

    for i in list(data.data.columns[1:]):
        ylist_listbox.insert('end',i)

    
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

def plot(data):
    select_list = ylist_listbox.curselection()
    print(data)
    y=ylist_listbox.get(select_list)
    data.plot(y)

plot_button = tk.Button(win, text= 'Plot', command = lambda:plot(data))
plot_button.grid(column=2, row=1)

win.mainloop()
