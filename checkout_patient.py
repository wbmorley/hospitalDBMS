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

def patient_remove():

    patient_ID = patientInfo.get()

    patient_removeSQL = ("DELETE FROM patients WHERE patientid = " + patient_ID)

    try:
        cursor.execute(patient_removeSQL)
        connection.commit()
        tk.messagebox.showinfo(title="Patient Check-out", message="Patient has succesfully been checked-out.")
    except mysql.connection.Error as err:
        tk.messagebox.showerror(title="Error", message=f"An error occurred. {err}")

    patientInfo.delete(0, "end")
    root.destroy()


def delete_patient():

    global root, patientInfo

    root = tk.Tk()
    root.title("Check-out Patient")
    root.minsize(400, 400)
    root.geometry("600x500")

    canvas = tk.Canvas(root)
    canvas.config(bg="#577a91")
    canvas.pack(expand=True, fill="both")

    # heading frame
    headingFrame = tk.Frame(root, bg="black", bd=5)
    headingFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    headingLabel = tk.Label(headingFrame, text=" Patient Check-out ", bg="black", fg="white",
                            font=('Arial Black', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = tk.Label(root, bg='#cccaca')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    label_entry = tk.Label(labelFrame, text="Patient ID : ", bg="#cccaca", fg="black", font=("Arial Black", 9))
    label_entry.place(relx=0.05, rely=0.5)

    patientInfo = tk.Entry(labelFrame)
    patientInfo.place(relx=0.3, rely=0.5, relwidth=0.62)

    checkout_button = tk.Button(root, text=" Check-out Patient ", font=("Arial Black", 10), command=patient_remove)
    checkout_button.place(relx=0.15, rely=0.85, relwidth=0.3, relheight=0.1)

    cancel_button = tk.Button(root, text=" Cancel ", font=("Arial Black", 10), command=root.destroy)
    cancel_button.place(relx=0.55, rely=0.85, relwidth=0.3, relheight=0.1)