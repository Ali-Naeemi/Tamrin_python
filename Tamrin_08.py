# import tkinter as tk
# from tkinter import messagebox

# def submit_form():
#     fullname = ent_name.get()
    
#     if fullname == "":
#         messagebox.showwarning("Warning!", "Enter your name: ")
#     else:
#         messagebox.showinfo("Welcome", f"Hello {fullname}, welcome to the program.")
#         ent_name.delete(0, tk.END)

# root = tk.Tk()
# root.title("Register")
# root.geometry("360x480")

# tk.Label(root, text="Fullname: ").grid(row=0, column=0, padx=10, pady=20)

# ent_name = tk.Entry(root, width=25)
# ent_name.grid(row=0, column=1)

# btn_submit = tk.Button(root, text="Register", command=submit_form, bg="#FF0000", fg="#000000")
# btn_submit.grid(row=1, column=0, columnspan=2, pady=10)

# root.mainloop()

##################################################

import tkinter as tk
from tkinter import messagebox

def dong_calculate():
    try:
        total_bill = float(ent_bill.get())
        num_people = int(ent_people.get())
        
        if total_bill <= 0 or num_people <= 0:
            messagebox.showwarning("Warning", "Numbers must be greater than 0.")
            return
            
        dong_person = total_bill / num_people
        
        messagebox.showinfo("Dong", f"Each Persons Dong: {dong_person:,.2f}")
        
    except ValueError:
        messagebox.showwarning("Warning", "Please enter integer numbers.")
        
    except ZeroDivisionError:
        messagebox.showwarning("Warning", "Number of people cannot be zero.")

root = tk.Tk()
root.title("Dong Calculator")
root.geometry("300x320")

label_bill = tk.Label(root, text="Total Bill: ")
label_bill.grid(row=0, column=0, padx=10, pady=10)

ent_bill = tk.Entry(root)
ent_bill.grid(row=0, column=1, padx=10, pady=10)

label_people = tk.Label(root, text="People Number: ")
label_people.grid(row=1, column=0, padx=10, pady=10)

ent_people = tk.Entry(root)
ent_people.grid(row=1, column=1, padx=10, pady=10)

btn_calculate = tk.Button(root, text="Dong Person", command=dong_calculate, bg="#FF0000", fg="#000000")
btn_calculate.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()