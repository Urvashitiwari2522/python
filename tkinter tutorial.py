import tkinter as tk
print("Tkinter is installed:")
from tkinter import messagebox
#function to handle login button click
def login():
    username = entry_username.get()
    password = entry_password.get()
    if username =="admin" and password =="12345":
        messagebox.showinfo("Login success" , "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed","Invalid Username or Password")
#Create main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x300")
root.resizable(False, False)

#Username Label and Entry
tk.Label(root, text="Username:",
font=("Arial",12)).pack(pady=5)
entry_username = tk.Entry(root,
font=("Arial",12))
entry_username.pack(pady=5)

#Passsword Lebeel and Entry
tk.Label(root, text="Password:",
font=("Arial",12)).pack(pady=5)
entry_password = tk.Entry(root,
font=("Arial",12))
entry_password.pack(pady=5)

#Login Button
login_button = tk.Button(root,
text="Login",font=("Arial",12),
command=login)
login_button.pack(pady=10)

#Run the tkinter event loop
root.mainloop()