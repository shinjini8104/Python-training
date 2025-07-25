import tkinter

def submit_data():
    name = name_val.get()
    phone = phone_val.get()
    gender = gender_val.get()
    city = city_val.get()

    if not name or not phone or not gender or not city:
        res.config(text="Please fill all fields", fg="red")
        return

    with open("registrations.txt", "a") as file:
        file.write(f"Name: {name}, Phone: {phone}, Gender: {gender}, City: {city}\n")

    res.config(text="Registration Successful!", fg="green")


    name_val.delete(0, 'end')
    phone_val.delete(0, 'end')
    gender_val.delete(0, 'end')
    city_val.delete(0, 'end')


root = tkinter.Tk()
root.geometry("500x500")
root.title("Registration Form")
root.configure(bg="#F0F8FF")

head = tkinter.Label(root, text="Registration Form", font=("Arial", 20, "bold"), bg="#ADD8E6")
head.pack(pady=30)

fr = tkinter.Frame(root, bg="#E0FFFF")
fr.pack(pady=5)


tkinter.Label(fr, text="Name", font=("Arial", 12), bg="light yellow").grid(row=0, column=0, padx=5, pady=5)
name_val = tkinter.Entry(fr)
name_val.grid(row=0, column=1, padx=5, pady=5)


tkinter.Label(fr, text="Phone", font=("Arial", 12), bg="light yellow").grid(row=1, column=0, padx=5, pady=5)
phone_val = tkinter.Entry(fr)
phone_val.grid(row=1, column=1, padx=5, pady=5)


tkinter.Label(fr, text="Gender", font=("Arial", 12), bg="light yellow").grid(row=2, column=0, padx=5, pady=5)
gender_val = tkinter.Entry(fr)
gender_val.grid(row=2, column=1, padx=5, pady=5)


tkinter.Label(fr, text="City", font=("Arial", 12), bg="light yellow").grid(row=3, column=0, padx=5, pady=5)
city_val = tkinter.Entry(fr)
city_val.grid(row=3, column=1, padx=5, pady=5)


tkinter.Button(fr, text="Submit", font=("Arial", 12, "bold"), command=submit_data).grid(row=4, column=0, columnspan=2, pady=15)


res = tkinter.Label(root, text="", font=("Arial", 10, "bold"), bg="#F0F8FF")
res.pack(pady=10)

root.mainloop()
