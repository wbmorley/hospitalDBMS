from datetime import datetime
from tkinter import messagebox
import tkinter as tk
import mysql.connector

# function to configure database connection and add patient to hospital database
def patient_insert():

    # entered patient data
    patient_last = patientInfo1.get()
    patient_first = patientInfo2.get()
    patient_depart = patientInfo3.get()
    patient_room = patientInfo4.get()
    patient_doctor = int(patientInfo5.get()[1])
    patient_intime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # connect to SQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="hospitalDBMS"
    )
    cursor = connection.cursor()

    patient_info = (patient_last, patient_first, patient_depart, patient_room, patient_doctor, patient_intime)


    # SQL insert statement for patients
    patient_insert = ("INSERT INTO patients"
                      "(last_name, first_name, department, room, doctorid, checkin_date)"
                      "VALUES (%s, %s, %s, %s, %s, %s)")

    # insert patient data
    try:
        cursor.execute(patient_insert, patient_info)
        connection.commit()
        tk.messagebox.showinfo(title="Checked-in", message="Patient has been checked in successfully.")
    except mysql.connector.Error as err:
        tk.messagebox.showerror(title="Error", message= f"An error has occurred. {err}.")

    root.destroy()

# function to configure tkinter window & canvas, prompt user input for patient information
def add_patient():

    global patientInfo1, patientInfo2, patientInfo3, patientInfo4, patientInfo5, root

    # configure tkinter window
    root = tk.Tk()
    root.title("Patient Check-In")
    root.minsize(400, 400)
    root.geometry("600x500")

    # connection for doctor query
    connection_doc = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="hospitalDBMS"
    )
    cursor_doc = connection_doc.cursor(buffered=True)

    # configure canvas
    canvas = tk.Canvas(root)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    # heading frame and label
    headingFrame = tk.Frame(root, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text="Check-In Patient", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # label frame for entries
    labelFrame = tk.Frame(root, bg="#cccaca")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # patient last name entry
    label1 = tk.Label(labelFrame, text="Last Name : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label1.place(relx=0.0, rely=0.15, relwidth=0.30, relheight=0.05)
    patientInfo1 = tk.Entry(labelFrame)
    patientInfo1.place(relx=0.27, rely=0.15, relwidth=0.6, relheight=0.05)

    # patient first name entry
    label2 = tk.Label(labelFrame, text="First Name : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label2.place(relx=0.0, rely=0.35, relwidth=0.30, relheight=0.05)
    patientInfo2 = tk.Entry(labelFrame)
    patientInfo2.place(relx=0.27, rely=0.35, relwidth=0.6, relheight=0.05)

    # patient department entry (drop down menu)
    label3 = tk.Label(labelFrame, text="Department : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label3.place(relx=0.0, rely=0.55, relwidth=0.30, relheight=0.05)
    options_depart = ["ER", "ICU", "Neurology", "Oncology", "Cardiology"]
    patientInfo3 = tk.StringVar(root)
    patientInfo3.set("Select")
    menu = tk.OptionMenu(labelFrame, patientInfo3, *options_depart)
    menu.place(relx=0.28, rely=0.54, relwidth=0.32, relheight=0.08)

    # patient room entry
    label4 = tk.Label(labelFrame, text="Room : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label4.place(relx=0.63, rely=0.55, relwidth=0.12, relheight=0.05)
    patientInfo4 = tk.Entry(labelFrame)
    patientInfo4.place(relx=0.77, rely=0.55, relwidth=0.10, relheight=0.05)

    # patient doctor entry (drop down menu)
    label5 = tk.Label(labelFrame, text="Primary Doctor : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label5.place(relx=0.0, rely=0.75, relwidth=0.30, relheight=0.05)

    # query for previously added doctors to select from in drop down menu
    doctor_SQL = "SELECT employeeid, CONCAT(last_name, ', ', first_name) FROM employees WHERE position = 'Doctor'"
    cursor_doc.execute(doctor_SQL)
    connection_doc.commit()

    options_doc = [doctor for doctor in cursor_doc]
    patientInfo5 = tk.StringVar(root)
    patientInfo5.set("Select")
    menu2 = tk.OptionMenu(labelFrame, patientInfo5, *options_doc)
    menu2.place(relx=0.28, rely=0.75, relwidth=0.6, relheight=0.1)


    checkin_button = tk.Button(root, text=" Check-In Patient ", font=("Arial Black", 10), command=patient_insert)
    checkin_button.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)

    cancel_button = tk.Button(root, text=" Cancel ", font=("Arial Black", 10), command=root.destroy)
    cancel_button.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)




