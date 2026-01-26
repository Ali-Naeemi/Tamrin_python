import tkinter as tk
from tkinter import messagebox
import Tamrin_09_Backend

book = Tamrin_09_Backend.PhoneBook()

def refresh_list():
    
    lst_contacts.delete(0, tk.END)
    
    for contact in book.contacts:
        display_text = f"{contact.name} - {contact.phone}"
        lst_contacts.insert(tk.END, display_text)
        
def refresh_list(data_list = None):
    lst_contacts.delete(0, tk.END)

    source = data_list if data_list is not None else book.contacts
    
    for contact in source:
        lst_contacts.insert(tk.END, f"{contact.name} - {contact.phone}")
        
def btn_add_click():
    
    name = ent_name.get()
    phone = ent_phone.get()

    if not name or not phone:
        messagebox.showwarning("warning", "please enter name and phone")
        return

    try:
        
        book.add_contact(name, phone)

        refresh_list()

        ent_name.delete(0, tk.END)
        ent_phone.delete(0, tk.END)
        messagebox.showinfo("sucsesful", "contact added")
        
    except ValueError as e:
        messagebox.showerror("error 444", str(e))

def btn_save_click():
    book.save_to_csv()
    messagebox.showinfo("save", "saving to file")

def btn_load_click():
    book.load_from_csv()
    refresh_list()
    messagebox.showinfo("loaded", "loaded from file")

def btn_delete_click():
    selection = lst_contacts.curselection()

    if not selection:
        messagebox.showwarning("warning!!!", "please select one contact for delete")
        return
    
    index = selection[0]

    confirm = messagebox.askyesno("are you serious?", "yes, delete")

    if confirm:
        book.remove_contact(index)

        refresh_list()
        messagebox.showinfo("sucsesfull", "contact is delete")

def btn_search_click():
    query = ent_search.get()
    
    if query:
        
        found_list = book.search_contacts(query)
        refresh_list(found_list)
    else:
        refresh_list()

root = tk.Tk()
root.title("smart phone book ")
root.geometry("800x600")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk_lbl = tk.Label(frame_top, text="name :")
tk_lbl.grid(row=0, column=0)

ent_name = tk.Entry(frame_top)
ent_name.grid(row=0, column=1, padx=5)

tk_lbl = tk.Label(frame_top, text="phone :")
tk_lbl.grid(row=0, column=2)

ent_phone = tk.Entry(frame_top)
ent_phone.grid(row=0, column=3, padx=5)

tk_lbl = tk.Label(frame_top, text="search")
tk_lbl.grid(row=0, column=4)

ent_search = tk.Entry(frame_top)
ent_search.grid(row=0, column=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk_btn = tk.Button(frame_buttons, text="add contact", command=btn_add_click, bg="#5900FF", fg="#FFFFFF")
tk_btn.pack(side=tk.LEFT, padx=5)

tk_btn = tk.Button(frame_buttons, text="save to file", command=btn_save_click, bg="#5900FF", fg="#FFFFFF")
tk_btn.pack(side=tk.LEFT, padx=5)

tk_btn = tk.Button(frame_buttons, text="load from file", command=btn_load_click, bg="#5900FF", fg="#FFFFFF")
tk_btn.pack(side=tk.LEFT, padx=5)

tk_btn = tk.Button(frame_buttons, text="delete", command=btn_delete_click, bg="#5900FF", fg="#FFFFFF")
tk_btn.pack(side=tk.LEFT, padx=5)

btn_search = tk.Button(frame_top, text="search", command=btn_search_click, bg="#5900FF", fg="#FFFFFF")
btn_search.grid(row=1, column=5, pady=5, sticky='w')

tk_btn = tk.Label(root, text="contact list :")
tk_btn.pack(pady=(30, 0))

lst_contacts = tk.Listbox(root, width=50, height=15)
lst_contacts.pack(pady=5)

root.mainloop()