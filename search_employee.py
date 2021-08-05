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

def selection_to_SQL(arg):
    switcher = {
        "Employee ID": "employeeid",
        "First Name": "first_name",
        "Last Name": "last_name",
        "Position": "position",
        "Department": "department"
    }
    return switcher[arg]


def employee_SQLsearch():

    searchSelection = clicked.get()
    searchInput = empInfo.get()
    SQLvar = selection_to_SQL(searchSelection)


    SQL = "SELECT * FROM employees WHERE " + SQLvar + " = '" + searchInput +"'"

    root2 = tk.Tk()
    root2.title("View Employees")
    root2.minsize(400, 400)
    root2.geometry("600x500")

    # configure canvas
    canvas = tk.Canvas(root2)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    # heading frame
    headingFrame = tk.Frame(root2, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text=" Employees ", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # frame for employee data
    labelFrame = tk.Frame(root2, bg="#cccaca")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheigh=0.5)
    tk.Label(labelFrame,
             text="{:^10}{:^15}{:^25}{:^25}{:^10}".format('ID', 'Last Name', 'First Name', 'Position', 'Department'),
             bg="black", fg="white").place(relx=0.07, rely=0.1)

    y = 0.25

    try:
        cursor.execute(SQL)
        connection.commit()
        for employee in cursor:
            tk.Label(labelFrame,
                     text="{:^7}{:^25}{:^25}{:^35}{}".format(employee[0], employee[1], employee[2], employee[3],
                                                             employee[4]),
                     bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1
    except mysql.connector.Error as err:
        tk.messagebox.showerror(title="Error", message=f"An error has occurred. {err}.")

    return_button = tk.Button(root2, text=" Return to Menu ", font=("Arial Black", 10), command=root2.destroy)
    return_button.place(relx=0.4, rely=0.9, relwidth=0.25, relheight=0.08)

    root2.mainloop()



def employee_search():

    global empInfo, label, clicked, root

    root = tk.Tk()
    root.title("Employee Search")
    root.minsize(400, 400)
    root.geometry("600x500")

    canvas = tk.Canvas(root)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    headingFrame = tk.Frame(root, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text=" Employee Search ", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Label(root, bg="#cccaca")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.45)

    options = ["Employee ID", "Last Name", "First Name", "Position", "Department"]

    clicked = tk.StringVar(root)
    clicked.set("Select")

    menu = tk.OptionMenu(labelFrame, clicked, *options)
    tk.Label(labelFrame, text=' Search Criteria : ', bg="#cccaca", fg="black", font=("Arial Black", 9)).place(relx=0.05, rely=0.30, relheight=0.1)
    menu.place(relx=0.3, rely=0.30, relwidth=0.62, relheight=0.1)

    label_entry = tk.Label(labelFrame, text=" Search Field : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label_entry.place(relx=0.05, rely=0.55)

    empInfo = tk.Entry(labelFrame)
    empInfo.place(relx=0.3, rely=0.55, relwidth=0.62)

    search_button = tk.Button(root, text=" Search Employees ", font=("Arial Black", 10), command=employee_SQLsearch)
    search_button.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)

    cancel_button = tk.Button(root, text=" Cancel ", font=("Arial Black", 10), command=root.destroy)
    cancel_button.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)

    root.mainloop()