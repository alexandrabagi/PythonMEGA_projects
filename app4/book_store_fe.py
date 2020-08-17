"""
A program that stores book information (title, author, year, isbn). 
The user can: 
view all records
search entry
add entry
update entry
delete entry
and close the program.
"""

from tkinter import *
import book_store_be

def view_command():
    lb.delete(0, END)
    for row in book_store_be.view():
        lb.insert(END, row)

def search_command():
    lb.delete(0, END)
    for row in book_store_be.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        lb.insert(END, row)

def add_command():
    book_store_be.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    lb.delete(0, END)
    lb.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

def get_selected_row(event): # this function is executed by the bind method, so event argument can't be removed
    global selected_tuple
    # if lb.size() != 0:
    #     index = lb.curselection()[0] # returns the index of the row
    #     selected_tuple = lb.get(index)
    #     e1.delete(0, END)
    #     e1.insert(END, selected_tuple[1])
    #     e2.delete(0, END)
    #     e2.insert(END, selected_tuple[2])
    #     e3.delete(0, END)
    #     e3.insert(END, selected_tuple[3])
    #     e4.delete(0, END)
    #     e4.insert(END, selected_tuple[4])
    try:
        index = lb.curselection()[0] # returns the index of the row
        print(lb.curselection())
        selected_tuple = lb.get(index)
        print(selected_tuple)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def delete_command():
    id = selected_tuple[0]
    book_store_be.delete(id)

def update_command():
    book_store_be.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())    

window = Tk()

window.wm_title("BookStore")

# labels
l1 = Label(window, text="Title")
l1.grid(row = 0, column = 0)
l2 = Label(window, text="Author")
l2.grid(row = 0, column = 2)
l3 = Label(window, text="Year")
l3.grid(row = 1, column = 0)
l4 = Label(window, text="ISBN")
l4.grid(row = 1, column = 2)

# entries
title_text = StringVar() # spatial object
e1 = Entry(window, text=title_text)
e1.grid(row = 0, column = 1)
author_text = StringVar()
e2 = Entry(window, text=author_text)
e2.grid(row = 0, column = 3)
year_text = StringVar()
e3 = Entry(window, text=year_text)
e3.grid(row = 1, column = 1)
isbn_text = StringVar()
e4 = Entry(window, text=isbn_text)
e4.grid(row = 1, column = 3)

# listbox
lb = Listbox(window, height = 6, width = 35)
lb.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
lb.bind('<<ListboxSelect>>', get_selected_row)

# scrollbar
sb = Scrollbar(window)
sb.grid(row = 2, column = 2, rowspan = 6)

# configuring scrollbar
lb.configure(yscrollcommand = sb.set)
sb.configure(command = lb.yview)

# buttons
b1 = Button(window, text="View All", width = 12, command = view_command)
b1.grid(row = 2, column = 3)
b2 = Button(window, text="Search Entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)
b3 = Button(window, text="Add Entry", width = 12, command = add_command)
b3.grid(row = 4, column = 3)
b4 = Button(window, text="Update Selected", width = 12, command = update_command)
b4.grid(row = 5, column = 3)
b5 = Button(window, text="Delete Selected", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)
b6 = Button(window, text="Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

# a way to wrap up all the widgets that enter the space above
window.mainloop()