import mysql.connector
from tkinter import *
from tkinter import messagebox

db = mysql.connector.connect(
    host="localhost",
    user="root",         
    password="Kumari@123", 
    database="hospital"
)
cursor = db.cursor()

# Patient Functions
def add_patient():
    name = entry_name.get()
    age = entry_age.get()
    gender = entry_gender.get()
    contact = entry_contact.get()
    address = entry_address.get()

    if name and age and gender and contact and address:
        query = "INSERT INTO Patients (Name, Age, Gender, Contact, Address) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (name, age, gender, contact, address))
        db.commit()
        messagebox.showinfo("Success", "Patient added successfully!")
        clear_patient_fields()
    else:
        messagebox.showwarning("Warning", "All fields are required.")

def view_patients():
    query = "SELECT * FROM Patients"
    cursor.execute(query)
    rows = cursor.fetchall()
    display_text = "\n".join([f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Gender: {row[3]}, Contact: {row[4]}, Address: {row[5]}" for row in rows])
    messagebox.showinfo("Patient Records", display_text or "No records found.")

def clear_patient_fields():
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_gender.delete(0, END)
    entry_contact.delete(0, END)
    entry_address.delete(0, END)

# Medicine Functions
def add_medicine():
    name = entry_medicine_name.get()
    manufacturer = entry_manufacturer.get()
    price = entry_price.get()
    stock = entry_stock.get()

    if name and manufacturer and price and stock:
        query = "INSERT INTO Medicines (Name, Manufacturer, Price, Stock) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, manufacturer, float(price), int(stock)))
        db.commit()
        messagebox.showinfo("Success", "Medicine added successfully!")
        clear_medicine_fields()
    else:
        messagebox.showwarning("Warning", "All fields are required.")

def view_medicines():
    query = "SELECT * FROM Medicines"
    cursor.execute(query)
    rows = cursor.fetchall()
    display_text = "\n".join([f"ID: {row[0]}, Name: {row[1]}, Manufacturer: {row[2]}, Price: {row[3]}, Stock: {row[4]}" for row in rows])
    messagebox.showinfo("Medicine Records", display_text or "No records found.")

def clear_medicine_fields():
    entry_medicine_name.delete(0, END)
    entry_manufacturer.delete(0, END)
    entry_price.delete(0, END)
    entry_stock.delete(0, END)

# Doctor Functions
def add_doctor():
    name = entry_doctor_name.get()
    specialization = entry_specialization.get()
    contact = entry_doctor_contact.get()

    if name and specialization and contact:
        query = "INSERT INTO Doctors (Name, Specialization, Contact) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, specialization, contact))
        db.commit()
        messagebox.showinfo("Success", "Doctor added successfully!")
        clear_doctor_fields()
    else:
        messagebox.showwarning("Warning", "All fields are required.")

def view_doctors():
    cursor.execute("SELECT * FROM Doctors")
    rows = cursor.fetchall()
    display_text = "\n".join([f"ID: {row[0]}, Name: {row[1]}, Specialization: {row[2]}, Contact: {row[3]}" for row in rows])
    messagebox.showinfo("Doctor Records", display_text or "No records found.")

def clear_doctor_fields():
    entry_doctor_name.delete(0, END)
    entry_specialization.delete(0, END)
    entry_doctor_contact.delete(0, END)

# GUI Setup
root = Tk()
root.title("Hospital Management System")

# Patient Registration
Label(root, text="Patient Registration", font=("Helvetica", 16)).grid(row=0, column=1, pady=10)
Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5)
entry_name = Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)
Label(root, text="Age:").grid(row=2, column=0, padx=10, pady=5)
entry_age = Entry(root)
entry_age.grid(row=2, column=1, padx=10, pady=5)
Label(root, text="Gender:").grid(row=3, column=0, padx=10, pady=5)
entry_gender = Entry(root)
entry_gender.grid(row=3, column=1, padx=10, pady=5)
Label(root, text="Contact:").grid(row=4, column=0, padx=10, pady=5)
entry_contact = Entry(root)
entry_contact.grid(row=4, column=1, padx=10, pady=5)
Label(root, text="Address:").grid(row=5, column=0, padx=10, pady=5)
entry_address = Entry(root)
entry_address.grid(row=5, column=1, padx=10, pady=5)
Button(root, text="Add Patient", command=add_patient).grid(row=6, column=1, pady=10)
Button(root, text="View Patients", command=view_patients).grid(row=6, column=2, pady=10)
Button(root, text="Clear Fields", command=clear_patient_fields).grid(row=6, column=0, pady=10)

# Medicine Management Section
Label(root, text="Medicine Management", font=("Helvetica", 16)).grid(row=7, column=1, pady=20)
Label(root, text="Medicine Name:").grid(row=8, column=0, padx=10, pady=5)
entry_medicine_name = Entry(root)
entry_medicine_name.grid(row=8, column=1, padx=10, pady=5)
Label(root, text="Manufacturer:").grid(row=9, column=0, padx=10, pady=5)
entry_manufacturer = Entry(root)
entry_manufacturer.grid(row=9, column=1, padx=10, pady=5)
Label(root, text="Price:").grid(row=10, column=0, padx=10, pady=5)
entry_price = Entry(root)
entry_price.grid(row=10, column=1, padx=10, pady=5)
Label(root, text="Stock:").grid(row=11, column=0, padx=10, pady=5)
entry_stock = Entry(root)
entry_stock.grid(row=11, column=1, padx=10, pady=5)
Button(root, text="Add Medicine", command=add_medicine).grid(row=12, column=1, pady=10)
Button(root, text="View Medicines", command=view_medicines).grid(row=12, column=2, pady=10)
Button(root, text="Clear Fields", command=clear_medicine_fields).grid(row=12, column=0, pady=10)

# Doctor Management Section
Label(root, text="Doctor Management", font=("Helvetica", 16)).grid(row=13, column=1, pady=20)
Label(root, text="Doctor Name:").grid(row=14, column=0, padx=10, pady=5)
entry_doctor_name = Entry(root)
entry_doctor_name.grid(row=14, column=1, padx=10, pady=5)
Label(root, text="Specialization:").grid(row=15, column=0, padx=10, pady=5)
entry_specialization = Entry(root)
entry_specialization.grid(row=15, column=1, padx=10, pady=5)
Label(root, text="Contact:").grid(row=16, column=0, padx=10, pady=5)
entry_doctor_contact = Entry(root)
entry_doctor_contact.grid(row=16, column=1, padx=10, pady=5)
Button(root, text="Add Doctor", command=add_doctor).grid(row=17, column=1, pady=10)
Button(root, text="View Doctors", command=view_doctors).grid(row=17, column=2, pady=10)
Button(root, text="Clear Fields", command=clear_doctor_fields).grid(row=17, column=0, pady=10)

root.mainloop()



