"""
A program that store this book information:
Backend functionaltiy 
Creating the db file
attaching the functions with buttons

"""

import back_end as be
import front_end as fe
from tkinter import *

be.create_table()
#When the app starts creating the book table in books.db


def view_command():
    fe.book_list.delete(0, END)
    for row in be.view():
        fe.book_list.insert(END, row)
        
def search_command(title, author, shelf, price, quantity, section):
    fe.book_list.delete(0, END)
    for row in be.search(title, author, shelf, price, quantity, section):
        fe.book_list.insert(END, row)

def insert_command(title, author, shelf, price, quantity, section):
    fe.book_list.delete(0, END)
    row = (title, author, shelf, price, quantity, section)
    be.insert(title, author, shelf, price, quantity, section)
    fe.book_list.insert(END, row)

def update_command():
    fe.book_list.delete(0, END)

def delete_command():
    fe.book_list.delete(0, END)
    be.delete(selected_tuple[0])
    for row in be.view():
        fe.book_list.insert(END, row)

def get_selected_row(event):
    global selected_tuple
    index = fe.book_list.curselection()[0]
    selected_tuple = fe.book_list.get(index)