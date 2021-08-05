from tkinter import messagebox
import tkinter as tk
import mysql.connector

# function to configure database connection and add employee to hospital database
def employee_insert():

    # entered employee data
    emp_last = empInfo1.get()
    emp_first = empInfo2.get()
    emp_position = empInfo3.get()
    emp_department = empInfo4.get()

    # connect to SQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="hospitalDBMS"
    )
    cursor = connection.cursor()


    emp_data = (emp_last, emp_first, emp_position, emp_department)

    # SQL insert statement for employees
    emp_insert = ("INSERT INTO employees"
                  "(last_name, first_name, position, department) "
                  "VALUES (%s, %s, %s, %s)")

    # insert employee data
    try:
        cursor.execute(emp_insert, emp_data)
        connection.commit()
        tk.messagebox.showinfo(title="Employee Added", message="Employee has been added successfully.")
    except mysql.connector.Error as err:
        tk.messagebox.showerror(title="Error", message=f"An error occurred. {err}")

    root.destroy()

# function to configure tkinter window & canvas, prompt user input for employee information
def add_employee():

    global empInfo1, empInfo2, empInfo3, empInfo4, root

    # configure tkinter window
    root = tk.Tk()
    root.title("Add Employee")
    root.minsize = (400, 400)
    root.geometry("600x500")

    # configure canvas
    canvas = tk.Canvas(root)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    # heading frame
    headingFrame = tk.Frame(root, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text="Add Employee", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # label frame for entries
    labelFrame = tk.Frame(root, bg="#cccaca")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # employee last name entry
    label1 = tk.Label(labelFrame, text="Last Name : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label1.place(relx=0.0, rely=0.20, relwidth=0.30, relheight=0.05)
    empInfo1 = tk.Entry(labelFrame)
    empInfo1.place(relx=0.27, rely=0.20, relwidth=0.6, relheight=0.05)

    # employee first name entry
    label2 = tk.Label(labelFrame, text="First Name : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label2.place(relx=0.0, rely=0.45, relwidth=0.30, relheight=0.05)
    empInfo2 = tk.Entry(labelFrame)
    empInfo2.place(relx=0.27, rely=0.45, relwidth=0.6, relheight=0.05)

    # employee position entry
    label3 = tk.Label(labelFrame, text="Position : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label3.place(relx=0.0, rely=0.70, relwidth=0.25, relheight=0.05)
    options_pos = ["Doctor", "Nurse", "Pharmacist", "Surgeon", "IT", "Custodial"]
    empInfo3 = tk.StringVar(root)
    empInfo3.set("Select")
    menu = tk.OptionMenu(labelFrame, empInfo3, *options_pos)
    menu.place(relx=0.20, rely=0.70, relwidth=0.25, relheight=0.08)

    # employee department entry
    label4 = tk.Label(labelFrame, text="Department : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label4.place(relx=.45, rely=0.70, relwidth=0.25, relheight=0.05)
    options_depart = ["ER", "ICU", "Neurology", "Oncology", "Cardiology", "N/A"]
    empInfo4 = tk.StringVar(root)
    empInfo4.set("Select")
    menu2 = tk.OptionMenu(labelFrame, empInfo4, *options_depart)
    menu2.place(relx=0.70, rely=0.69, relwidth=0.25, relheight=0.08)

    checkin_button = tk.Button(root, text=" Add Employee ", font=("Arial Black", 10), command=employee_insert)
    checkin_button.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)

    cancel_button = tk.Button(root, text=" Cancel ", font=("Arial Black", 10), command=root.destroy)
    cancel_button.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)

