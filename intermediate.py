"""
A program that store this book information:
Backend functionaltiy 
Creating the db file
attaching the functions with buttons

"""

from back_end import Database
import front_end as fe
from tkinter import *

db = Database("books.db")
#When the app starts creating the book table in books.db

def view_command():
    fe.book_list.delete(0, END)
    hide_entries()
    for row in db.view():
        fe.book_list.insert(END, row)
        
def search_command(title, author, shelf, price, quantity, section):
    fe.book_list.delete(0, END)
    for row in db.search(title, author, shelf, price, quantity, section):
        fe.book_list.insert(END, row)

def insert_command(title, author, shelf, price, quantity, section):
    fe.book_list.delete(0, END)
    row = (title, author, shelf, price, quantity, section)
    db.insert(title, author, shelf, price, quantity, section)
    fe.book_list.insert(END, row)
    
def update_command(title, author, shelf, price, quantity, section):
    fe.book_list.delete(0, END)
    row = (title, author, shelf, price, quantity, section)
    db.update(selected_tuple[0],title, author, shelf, price, quantity, section)
    fe.book_list.insert(END, row)

def delete_command():
    fe.book_list.delete(0, END)
    hide_entries()
    db.delete(selected_tuple[0])
    for row in db.view():
        fe.book_list.insert(END, row)
    
def get_selected_row(event):
    global selected_tuple
    index = fe.book_list.curselection()[0]
    selected_tuple = fe.book_list.get(index)
    update_entries()
    
def hide_entries():
    fe.title_e.delete(0, END)
    fe.author_e.delete(0, END)
    fe.shelf_e.delete(0, END)
    fe.quantity_e.delete(0, END)
    fe.price_e.delete(0, END)
    fe.section_e.delete(0, END)
    
    
def update_entries():
    hide_entries()
    try:
        fe.title_e.insert(END, selected_tuple[1])
        fe.author_e.insert(END, selected_tuple[2])
        fe.shelf_e.insert(END, selected_tuple[3])
        fe.quantity_e.insert(END, selected_tuple[4])
        fe.price_e.insert(END, selected_tuple[5])
        fe.section_e.insert(END, selected_tuple[6])
    