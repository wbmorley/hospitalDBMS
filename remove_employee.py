from tkinter import messagebox
import tkinter as tk
import mysql.connector

# connect to SQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="hospitalDBMS"
    )
cursor = connection.cursor()

def employee_remove():

    employee_ID = employeeInfo.get()

    employee_removeSQL = ("DELETE FROM employees WHERE employeeid = " + employee_ID)

    try:
        cursor.execute(employee_removeSQL)
        connection.commit()
        tk.messagebox.showinfo(title="Employee Removal", message="Employee has succesfully been removed.")
    except mysql.connector.Error as err:
        tk.messagebox.showerror(title="Error", message=f"An error occurred. {err}")

    employeeInfo.delete(0, "end")
    root.destroy()


def delete_employee():

    global root, employeeInfo

    root = tk.Tk()
    root.title("Employee Removal")
    root.minsize(400, 400)
    root.geometry("600x500")

    canvas = tk.Canvas(root)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    # heading frame
    headingFrame = tk.Frame(root, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text=" Employee Removal ", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Label(root, bg='#cccaca')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    label_entry = tk.Label(labelFrame, text="Employee ID : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label_entry.place(relx=0.05, rely=0.45)

    employeeInfo = tk.Entry(labelFrame)
    employeeInfo.place(relx=0.3, rely=0.45, relwidth=0.62)

    remove_button = tk.Button(root, text=" Remove Employee ", font=("Arial Black", 10), command=employee_remove)
    remove_button.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)

    cancel_button = tk.Button(root, text=" Cancel ", font=("Arial Black", 10), command=root.destroy)
    cancel_button.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)