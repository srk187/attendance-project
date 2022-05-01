from optparse import Values
from tkinter import *
import tkinter as tk
from unicodedata import name
import mysql.connector
from tkinter import messagebox

root = tk.Tk()
root.title("Attandance System")
root.geometry("400x400")

name_var = tk.StringVar()
enrollment_var = tk.StringVar()
attand_var = tk.StringVar()
show_var = tk.StringVar()
option=['--select--']
show_var.set(option[0])

db = mysql.connector.connect(host="localhost",user="root",password ="",database="student_data")
cursor = db.cursor()
query1 = "SELECT name FROM attendance_data"
cursor.execute(query1)
fetch = cursor.fetchall()
for i in fetch:
    option.append(i)
print(option)
def database():
    try:
        name = name_var.get()
        enrollment = enrollment_var.get()
        attandence = attand_var.get() 
        query = "INSERT INTO attendance_data (name,enrollment_no,attandence) VALUES(%s,%s,%s)"
        b1=(name,enrollment,attandence)
        cursor.execute(query,b1)
        db.commit()
        messagebox.showinfo("info",)
    except:
        print("note done")
def add():
    name_label = tk.Label(root, text="Enter Name").grid(row=0,column=0)
    enroll_label = tk.Label(root, text="Enter Enrollment No:").grid(row=2,column=0)
    attandence_label = tk.Label(root,text="Enter Absent or Present").grid(row=4,column=0)
    
    name_entry = tk.Entry(root,textvariable=name_var).grid(row=0,column=2)
    enroll_entry = tk.Entry(root,textvariable=enrollment_var).grid(row=2,column=2)
    attandance_entry = tk.Entry(root,textvariable=attand_var).grid(row=4,column=2)
    
    
    btn=tk.Button(root,text="add",command = database).grid(row=8,column=2)
def fetch():
    query2 = "SELECT * FROM attendance_data"
    cursor.execute(query2)
    get = cursor.fetchall()
    for k in get:
        messagebox.showinfo("records",k)
    
def show():
    
    w= OptionMenu(root,show_var,*option).grid(row=12,column=2)
    fetch_records = tk.Button(root,text="Get Records",command=fetch).grid(row=13,column=2)

addRecord = tk.Button(root,text="Add Record",command=add).grid(row=6,column=2)
showrecord =tk.Button(root,text="Show Records",command=show).grid(row=10,column=2)

root.mainloop()