import tkinter as tk
from tkinter import ttk
from backend import sign_up , login, getUsername, searchMedicine, debug_view_medicines, manual_test_search, deleteMedicine, updateMedicine, viewAllMedicines, getReminder
from tkinter import messagebox
import subprocess
import os

window = tk.Tk()
window.geometry("600x500") 
window.title("Medication Tracker - SignUp/Login")

label = tk.Label(window, text="Medication Tracker App", font=('Arial', 20))
label.pack(padx=30, pady=30)

label1 = tk.Label(window, text="~~HIEEE~~", font=('Arial', 15))
label1.pack()

button_frame = tk.Frame(window)
button_frame.pack(padx=30)

def signup_form():
    for widget in window.winfo_children():
        widget.destroy()
        
    tk.Label(window, text="Sign Up", font=('Arial', 20)).pack(padx=30, pady=30)
    
    tk.Label(window, text="Username").pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    tk.Label(window, text="Email").pack()
    email_entry=tk.Entry(window)
    email_entry.pack()

    tk.Label(window, text="Password").pack()
    password_entry=tk.Entry(window, show="*")
    password_entry.pack()

    tk.Label(window, text="Age").pack()
    age_entry=tk.Entry(window)
    age_entry.pack()

    tk.Label(window, text="Gender").pack()
    gender_entry=tk.Entry(window)
    gender_entry.pack()

    tk.Label(window, text="Weight").pack()
    weight_entry=tk.Entry(window)
    weight_entry.pack()

    def submit_signup():
        username = username_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        age = age_entry.get()
        gender = gender_entry.get()
        weight = weight_entry.get()

        try: 
            age = int(age)
            weight = float(weight)
        except ValueError:
            messagebox.showerror("Invalid input, Please enter valid info")
            return
        
        user = sign_up(username, email, password, age, weight, gender)

        if user: 
            messagebox.showinfo("Account successfully created") 
            dashboard(user["userID"], user["username"])
        else:
            messagebox.showerror("Error :: Invalid info or email already exists")

    tk.Button(window, text = "Submit", command = submit_signup).pack(pady=20)

def login_form():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text = "Login", font=('Arial', 20)).pack(padx = 30, pady = 10)

    tk.Label(window, text = "Email").pack()
    email_entry = tk.Entry(window)
    email_entry.pack()

    tk.Label(window, text = "Password").pack()
    password_entry = tk.Entry(window)
    password_entry.pack()

    def submit_login():
        email = email_entry.get()
        password = password_entry.get()

        user = login(email, password)

        if user:
            messagebox.showinfo(f"Logged in as {user['username']}")
            dashboard(user["userID"], user["username"])
        else:
            messagebox.showerror("Invalid credentials")

    tk.Button(window, text="Submit", command = submit_login).pack(pady=20)

sign_up_button = tk.Button(button_frame, padx=15, text="Sign Up", width=8, height=1, command = signup_form)
sign_up_button.pack(pady=(20, 10))
login_button = tk.Button(button_frame, text="Login", padx=15, width=8, height=1, command = login_form)
login_button.pack(pady=(30, 15))

def main_screen():
    for widget in window.winfo_children():
        widget.destroy()

    label = tk.Label(window, text="Medication Tracker App", font=('Arial', 20))
    label.pack(padx=30, pady=30)

    label1 = tk.Label(window, text="~~HIEEE~~", font=('Arial', 15))
    label1.pack()

    button_frame = tk.Frame(window)
    button_frame.pack(padx=30)

    tk.Button(button_frame, padx=15, text="Sign Up", width=8, height=1, command=signup_form).pack(pady=(20, 10))
    tk.Button(button_frame, text="Login", padx=15, width=8, height=1, command=login_form).pack(pady=(30, 15))

def dashboard(userID, username):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text=f"Welcome, {username} *_*", font=('Arial, 18')).pack(pady=20)

    tk.Button(window, text = "Add Medicine", width = 20, height = 2, command = lambda: addMeds_Form(userID)).pack(pady=10)
    tk.Button(window, text = "Search Medicine", width = 20, height = 2, command=lambda: searchMeds_Form(userID)).pack(pady=10)
    tk.Button(window, text = "Update Medicine", width = 20, height = 2, command=lambda: updateMeds_Form(userID)).pack(pady=10)
    tk.Button(window, text = "Delete Medicine", width = 20, height = 2, command=lambda: deleteMeds_Form(userID)).pack(pady=10)
    tk.Button(window, text = "View all Medicines", width = 20, height = 2, command=lambda: viewAll_Form(userID)).pack(pady=10)

    tk.Button(window, text = "Logout", command=logout, width = 20, height = 2).pack(pady=30)

def addMeds_Form(userID):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Add Medicine", font=('Arial, 18')).pack(pady=20)

    tk.Label(window, text = "Medicine name").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    tk.Label(window, text = "Dosage (mg)").pack()
    dosage_entry = tk.Entry(window)
    dosage_entry.pack()

    tk.Label(window, text = "Quantity (e.g, 2 times a day)").pack()
    quantity_entry = tk.Entry(window)
    quantity_entry.pack()

    tk.Label(window, text = "Start Date (YYYY-MM-DD)").pack()
    startDate_entry = tk.Entry(window)
    startDate_entry.pack()

    tk.Label(window, text = "End Date (YYYY-MM-DD)").pack()
    endDate_entry = tk.Entry(window)
    endDate_entry.pack()

    tk.Label(window, text="Reminders (e.g, 8:00AM or 9:00PM)").pack()
    time_entry = tk.Entry(window)
    time_entry.pack()

    reminder_var = tk.IntVar()
    tk.Checkbutton(window, text = "Enable Reminder", variable = reminder_var).pack(pady=10)

    def submitForm():
        name = name_entry.get()
        dosage = dosage_entry.get()
        quantity = quantity_entry.get()
        startDate = startDate_entry.get()
        endDate = endDate_entry.get()
        times_raw = time_entry.get()
        reminderEnabled = reminder_var.get()

        if not all ([name, dosage, quantity, startDate, endDate]):
            messagebox.showerror("ERROR :: Please fill all fields")
            return
        
        times = [t.strip() for t in times_raw.split(",")] if reminderEnabled else []
        
        from backend import addMedicine
        success = addMedicine(name, dosage, quantity, startDate, endDate, reminderEnabled, userID)

        if success and reminderEnabled:
            from backend import addReminderTimes, getMedicineID
            from backend import viewAllMedicines
            all_meds = viewAllMedicines(userID)
            medID = all_meds[-1][0]  

            addReminderTimes(medID, times)
            messagebox.showinfo("Medicine successfully added")
            dashboard(userID, getUsername(userID))

        else:
            messagebox.showerror("Invalid info, Medicine couldn't be added")

    tk.Button(window, text = "Submit", command = submitForm).pack(pady = 20)
    tk.Button(window, text = "Back", command = lambda: dashboard(userID, getUsername(userID)))
        

def searchMeds_Form(userID):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text = "Search Medicine", font=('Arial, 18')).pack(pady=20)

    tk.Label(window, text="Enter name: ").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    result_box = tk.Text(window, height = 10, width = 60)
    result_box.pack(pady=10)

    def submit_form():
        medName = name_entry.get().strip()
        print(f"Searching for: {medName}, for userID: {userID}")
        debug_view_medicines()
        manual_test_search()
        results = searchMedicine(userID, medName)

        result_box.delete("1.0", tk.END)

        if results:
            for med in results:
                result_box.insert(tk.END, f"Name: {med[1]}, Dosage: {med[2]} mg, Quantity: {med[3]} \n")
                result_box.insert(tk.END, f"Start Date: {med[4]}, End Date: {med[5]}\n")
                result_box.insert(tk.END, f"Reminder Enabled: {'Yes' if med[7] else 'No'}\n")
                
                reminder_times = getReminder(med[0])
                if reminder_times:
                   result_box.insert(tk.END, f"Times: {', '.join(reminder_times)}\n")
                else:
                   result_box.insert(tk.END, "No reminder times set\n")


        else:
            result_box.insert(tk.END, "No medicine found")  

    tk.Button(window, text="Search", command=submit_form).pack(pady=10) 
    tk.Button(window, text="Back", command=lambda:dashboard(userID, getUsername(userID))).pack(pady=10)

def deleteMeds_Form(userID):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Delete Medicine", font=('Arial', 18)).pack()

    tk.Label(window, text="Enter Medicine").pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    result_label = tk.Label(window, text="", fg="red")
    result_label.pack(pady=10)
    
    def submit_delete():
        medName = name_entry.get().strip()

        if not medName:
            result_label.config(text="Please enter a medicine name")
            return
        
        success = deleteMedicine(userID, medName)

        if success:
            result_label.config(text=f"{medName} deleted successfully", fg="green")

        else:
            result_label.config(text=f"{medName} could not be found", fg="red")

    tk.Button(window, text="Delete", command=submit_delete).pack(pady=10)
    tk.Button(window, text="Back", command=lambda: dashboard(userID, getUsername(userID))).pack(pady=10)
  
def updateMeds_Form(userID):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text = "Update Medicine", font=('Arial', 18)).pack()

    fields = [
        ("Medicine name: ", "name_entry"),
        ("Dosage (mg): ", "dosage_entry"),
        ("Quantity: ", "quantity_entry"),
        ("Start Date: ", "startDate_entry"),
        ("End Date: ", "endDate_entry")
    ]

    entries = {}

    for label_text, var_name in fields:
        tk.Label(window, text=label_text ).pack()
        entry = tk.Entry(window)
        entry.pack()
        entries[var_name] = entry

    reminder_var = tk.IntVar()
    tk.Checkbutton(window, text="Enable Reminder", variable=reminder_var).pack()


    result_label = tk.Label(window, text="", fg="red")
    result_label.pack()

    def submit_update():
        try:
            medName = entries["name_entry"].get().strip()
            dosage = int(entries["dosage_entry"].get())
            quantity = entries["quantity_entry"].get().strip()
            startDate = entries["startDate_entry"].get().strip()
            endDate = entries["endDate_entry"].get().strip()
            reminder = reminder_var.get()


            if not medName:
              result_label.config(text="Please enter valid info")
              return

            success = updateMedicine(userID, medName, dosage, quantity, startDate, endDate, reminder)

            if success:
               result_label.config(text="Medicine updated", fg="green")

            else:
               result_label.config(text="Medicine couldnt be updated", fg="red")

        except Exception as e:
            result_label.config(text=f"Error: {e}", fg="red")

    tk.Button(window, text="Update", command = submit_update).pack(pady=10)
    tk.Button(window, text= "Back", command=lambda: dashboard(userID, getUsername(userID))).pack(pady=10)

def showDetails(medis):
    show = tk.Toplevel(window)
    show.title("Medicine Details")

    from backend import getReminder
    times = getReminder(medis[0])
    times_str = f"Reminder Times: {', '.join(times)}" if times else "No specific times"

    details = (
        f"Name: {medis[1]}\n"
        f"Dosage: {medis[2]} mg\n"
        f"Quantity: {medis[3]} per day\n"
        f"Start Date: {medis[4]}\n"
        f"End Date: {medis[5]}\n"
        f"Reminder: {'Yes' if medis[6] else 'No'}\n"
        f"{times_str}"
    )

    tk.Label(show, text=details, justify="left", padx=10, pady=10).pack()
    tk.Button(show, text="Close", command=show.destroy).pack(pady=5)


def viewAll_Form(userID):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text = "All Medicines", font=('Arial', 18)).pack(pady=20)

    columns = ("Name", "Dosage", "Time")
    tree = ttk.Treeview(window, columns = columns, show = "headings")
    tree.heading("Name", text="Name")
    tree.heading("Dosage", text = "Dosage (mg)")
    tree.heading("Time", text = "Time to Take")
    tree.pack(pady=10)

    view = viewAllMedicines(userID)

    for med in view:
        times = getReminder(med[0])
        tree.insert("", tk.END, values=(med[1], med[2], ', '.join(times) if times else '-'), tags=(med[0], ))


    def itemClick(click):
        selectedItem = tree.selection()
        if selectedItem:
            itemValue = tree.item(selectedItem[0])['values']
            medName = itemValue[0]

            for med in view:
                if med[1] == medName:
                    showDetails(med)
                    break

    tree.bind("<Double-1>", itemClick)

    tk.Button(window, text = "Back", command = lambda: dashboard(userID, getUsername(userID))).pack(pady=10)

def logout():
    for widget in window.winfo_children(): 
        widget.destroy()
    login_form()

reminder_process = subprocess.Popen(["python", "reminders.py"], creationflags=subprocess.CREATE_NO_WINDOW)

window.mainloop() #creates a new window
