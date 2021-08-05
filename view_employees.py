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
cursor = connection.cursor(buffered=True)


def view_employees():

    # configure tkinter window
    root = tk.Tk()
    root.title("View Employees")
    root.minsize(400, 400)
    root.geometry("600x500")

    # configure canvas
    canvas = tk.Canvas(root)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    # heading frame
    headingFrame = tk.Frame(root, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text=" Employees ", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # frame for employee data
    labelFrame = tk.Frame(root, bg="black")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheigh=0.5)
    tk.Label(labelFrame, text="{:<10}{:<20}{:^20}{:^30}{:>10}".format('ID', 'Last Name', 'First Name', 'Position', 'Department'),
             bg="black", fg="white").place(relx=0.07, rely=0.1)

    get_employees = "SELECT * FROM employees"
    y = 0.25

    try:
        cursor.execute(get_employees)
        connection.commit()

        for employee in cursor:

            tk.Label(labelFrame, text="{: <10}{: ^20}{: ^20}{: ^30}{: ^25}".format(employee[0], employee[1], employee[2], employee[3], employee[4]),
                     bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1
    except mysql.connector.Error as err:
        tk.messagebox.showerror(title="Error", message=f"An error has occurred. {err}.")

    return_button = tk.Button(root, text=" Return to Menu ", font=("Arial Black", 10), command=root.destroy)
    return_button.place(relx=0.4, rely=0.9, relwidth=0.25, relheight=0.08)

    root.mainloop()