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

def view_patients():

    # configure tkinter window
    root = tk.Tk()
    root.title("View Patients")
    root.minsize(400,400)
    root.geometry("600x500")

    # configure canvas
    canvas = tk.Canvas(root)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    # heading frame
    headingFrame = tk.Frame(root, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text=" Patients ", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # frame for patient data
    labelFrame = tk.Frame(root, bg="black")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    tk.Label(labelFrame, text="{:^5}{:^20}{:^15}{:^20}{:^15}{}".format('ID', 'Name', 'Department', 'Room', 'Doctor', 'Check-in Date'),
          bg="black", fg="white").place(relx=0.07, rely=0.1)
    tk.Label(labelFrame, text="----------------------------------------------------------------------------------------", bg="black", fg="white").place(relx=0.05, rely=0.2)

    # SQL select command for patients table
    get_patients = "SELECT * FROM patients"
    y = 0.25

    # run SQL query and display results 
    try:
        cursor.execute(get_patients)
        connection.commit()

        for patient in cursor:
            tk.Label(labelFrame, text="{:^2}{:^20}{:^25}{:^18}{:^25}{}".format(patient[0], (patient[2] + ", " + patient[1]), patient[3], patient[4], patient[5], patient[6]),
                  bg='black', fg="white").place(relx=0.07, rely=y)
            y += 0.1
    except mysql.connector.Error as err:
        tk.messagebox.showerror(title="Error", message=f"An error has occurred. {err}.")

    return_button = tk.Button(root, text=" Return to Menu ", font=("Arial Black", 10), command=root.destroy)
    return_button.place(relx=0.4, rely=0.9, relwidth=0.25, relheight=0.08)

    root.mainloop()
