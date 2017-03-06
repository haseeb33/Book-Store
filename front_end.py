"""
A program that store this book information:
Title, Author
Price, Quantity
Shelf Number, Section Number

User can:
View all the entries
Search an entry
Insert new entry
Update an entry
Delete an entry
Close the program
"""
from tkinter import *
import intermediate as itmd

def view_command():
    itmd.view_command()

def search_command():
    itmd.search_command(title_txt.get(), author_txt.get(), shelf_txt.get(), price_txt.get(), quantity_txt.get(), section_txt.get())
    
def insert_command():
    itmd.insert_command(title_txt.get(), author_txt.get(), shelf_txt.get(), price_txt.get(), quantity_txt.get(), section_txt.get())
    
def update_command():
    itmd.update_command(title_txt.get(), author_txt.get(), shelf_txt.get(), price_txt.get(), quantity_txt.get(), section_txt.get())
    
def delete_command():
    itmd.delete_command()

    
window = Tk(baseName = "Book Store")

button_width = 15

title_l = Label(window, text = "Title")
title_l.grid(row = 0, column = 0, padx = (10, 10), pady=(5,5))

title_txt = StringVar()
title_e = Entry(window, textvariable = title_txt)
title_e.grid(row = 0, column = 1)

author_l = Label(window, text = "Author")
author_l.grid(row = 0, column = 2, padx = (10, 10))

author_txt = StringVar()
author_e = Entry(window,textvariable = author_txt)
author_e.grid(row = 0, column = 3)

shelf_l = Label(window, text = "Shelf No")
shelf_l.grid(row = 0, column = 4, padx = (10, 10))

shelf_txt = StringVar()
shelf_e = Entry(window, textvariable = shelf_txt)
shelf_e.grid(row = 0, column = 5, padx = (0, 10))

price_l = Label(window, text = "Price")
price_l.grid(row = 1, column = 0, pady = (5,5))

price_txt = StringVar()
price_e = Entry(window, textvariable = price_txt)
price_e.grid(row = 1, column = 1)

quantity_l = Label(window, text = "Quantity")
quantity_l.grid(row = 1, column = 2)

quantity_txt = StringVar()
quantity_e =Entry(window, textvariable = quantity_txt)
quantity_e.grid(row = 1, column = 3)

section_l = Label(window, text = "Section No")
section_l.grid(row = 1, column = 4)

section_txt = StringVar()
section_e = Entry(window, textvariable = section_txt)
section_e.grid(row = 1, column = 5, padx = (0, 10))

book_list = Listbox(window, height = 12, width = 55)
book_list.grid(row = 2, column = 1, columnspan = 3, rowspan = 6, pady = (0, 10))

scroll = Scrollbar(window)
scroll.grid(row = 2, column = 4, rowspan = 6, sticky = W+N+S, pady = (5, 10))

book_list.configure(yscrollcommand = scroll.set)
scroll.configure(command = book_list.yview)

book_list.bind("<<ListboxSelect>>", itmd.get_selected_row)

view_b = Button(window, text = "View All", width = button_width, command = view_command)
view_b.grid(row = 2, column = 5, pady = (2, 2))

search_b = Button(window, text = "Search", width = button_width, command = search_command)
search_b.grid(row = 3, column = 5, pady = (2, 2))

insert_b = Button(window, text = "Insert New Entry", width = button_width, command = insert_command)
insert_b.grid(row = 4, column = 5, pady = (2, 2))

update_b = Button(window, text = "Update", width = button_width, command = update_command)
update_b.grid(row = 5, column = 5, pady = (2, 2))

delete_b = Button(window, text = "Delete an Entry", width = button_width, command = delete_command)
delete_b.grid(row = 6, column = 5, pady = (2, 2))

close_b  = Button(window, text = "Close Program", width = button_width)
close_b.grid(row = 7, column = 5, pady = (2, 5))

window.mainloop()
