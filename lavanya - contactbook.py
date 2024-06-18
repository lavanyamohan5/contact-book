import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("CONTACT BOOK")

contacts = {}

def add_contact():
    name = entry_Name.get()
    phone = entry_Phone.get()
    email = entry_Email.get()
    address = entry_Address.get()
    if name and phone and email and address:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo("Success", "Contact {name} added")
        entry_Name.delete(0, tk.END)
        entry_Phone.delete(0, tk.END)
        entry_Email.delete(0, tk.END)
        entry_Address.delete(0, tk.END)
        update_list()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields")

def list_contacts():
    if not contacts:
        print("No contacts are here")
    else:
        for name, info in contacts.items():
            print("Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")

def find_contact():
    name = entry_search.get()
    if name in contacts:
        info = contacts[name]
        messagebox.showinfo("Contact Found", "Name: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}")
    else:
        messagebox.showwarning("Error", "Contact not found")

def delete_contact():
    name = entry_search.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact {name} removed")
        update_list()
    else:
        messagebox.showwarning("Error", "Contact not found")

def update_list():
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        contact_listbox.insert(tk.END, "Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")

tk.Label(window, text='Name').grid(row=0, column=0)
tk.Label(window, text='Phone').grid(row=1, column=0)
tk.Label(window, text='Email').grid(row=2, column=0)
tk.Label(window, text='Address').grid(row=3, column=0)

entry_Name = tk.Entry(window)
entry_Name.grid(row=0, column=1, pady=5)
entry_Phone = tk.Entry(window)
entry_Phone.grid(row=1, column=1, pady=5)
entry_Email = tk.Entry(window)
entry_Email.grid(row=2, column=1, pady=5)
entry_Address = tk.Entry(window)
entry_Address.grid(row=3, column=1, pady=5)

tk.Label(window, text='Search').grid(row=4, column=0)
entry_search = tk.Entry(window)
entry_search.grid(row=4, column=1, pady=5)

tk.Button(window, text='Add Contact', command=add_contact).grid(row=5, column=0, pady=5)
tk.Button(window, text='Delete Contact', command=delete_contact).grid(row=5, column=1, pady=5)
tk.Button(window, text='Find Contact', command=find_contact).grid(row=5, column=2, pady=5)

contact_listbox = tk.Listbox(window, width=50)
contact_listbox.grid(row=6, column=0, columnspan=3, pady=5)
update_list()

window.mainloop()
