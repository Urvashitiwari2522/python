import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import webbrowser

# Function to open LinkedIn
def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/urvashi-tiwari2208")

# Function to open GitHub
def open_github():
    webbrowser.open("https://github.com/urvashitiwari2522")

# Function to display contact info
def show_contact():
    messagebox.showinfo("Contact Me", "Email: priyatiwari0425@gmail.com\nPhone: +91XXXXXXXXXX")

# Create main window
root = tk.Tk()
root.title("Urvashi's Portfolio")
root.geometry("500x700")
root.configure(bg="#f4f4f4")

# Title Label
title_label = tk.Label(root, text="Urvashi Tiwari", font=("Arial", 20, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=10)

# Bio
bio_label = tk.Label(root, text="BCA Student | Python & ML Enthusiast", font=("Arial", 12), bg="#f4f4f4", fg="#555")
bio_label.pack()

# Skills Section
skills_label = tk.Label(root, text="Skills", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#222")
skills_label.pack(pady=(20, 5))

skills_text = "• Python\n• Java\n• Flask\n• Linux\n• MySQL\n• AI & ML"
skills_display = tk.Label(root, text=skills_text, font=("Arial", 12), bg="#f4f4f4", fg="#444")
skills_display.pack()

# Projects Section
projects_label = tk.Label(root, text="Projects", font=("Arial", 14, "bold"), bg="#f4f4f4", fg="#222")
projects_label.pack(pady=(20, 5))

projects_text = """• Hangman Game (Python)
• QR Code Generator
• Secret Code Language
• Chatbot
• Calculator (Tkinter)
• Notebook (Tkinter)"""  # Added Notebook
projects_display = tk.Label(root, text=projects_text, font=("Arial", 12), bg="#f4f4f4", fg="#444")
projects_display.pack()

# Buttons for LinkedIn, GitHub, and Contact
linkedin_button = tk.Button(root, text="LinkedIn", font=("Arial", 12), bg="#0077b5", fg="white", command=open_linkedin)
linkedin_button.pack(pady=10)

github_button = tk.Button(root, text="GitHub", font=("Arial", 12), bg="#24292e", fg="white", command=open_github)
github_button.pack(pady=10)

contact_button = tk.Button(root, text="Contact Me", font=("Arial", 12), bg="#4CAF50", fg="white", command=show_contact)
contact_button.pack(pady=10)

# ---------- CALCULATOR PROJECT ----------
def open_calculator():
    calc = tk.Toplevel(root)
    calc.title("Calculator")
    calc.geometry("300x400")

    def on_click(btn):
        entry.insert(tk.END, btn)

    def clear():
        entry.delete(0, tk.END)

    def calculate():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    entry = tk.Entry(calc, font=("Arial", 16))
    entry.pack(fill="both", padx=10, pady=10)

    buttons = [
        "7", "8", "9", "/", "4", "5", "6", "*",
        "1", "2", "3", "-", "0", ".", "=", "+"
    ]

    btn_frame = tk.Frame(calc)
    btn_frame.pack()

    row, col = 0, 0
    for button in buttons:
        if button == "=":
            btn = tk.Button(btn_frame, text=button, font=("Arial", 14), width=10, command=calculate)
        else:
            btn = tk.Button(btn_frame, text=button, font=("Arial", 14), width=5, command=lambda b=button: on_click(b))

        btn.grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

    clear_btn = tk.Button(calc, text="C", font=("Arial", 14), width=22, command=clear)
    clear_btn.pack(pady=5)

calculator_button = tk.Button(root, text="Open Calculator", font=("Arial", 12), bg="#FF5733", fg="white", command=open_calculator)
calculator_button.pack(pady=10)

# ---------- NOTEBOOK PROJECT ----------
def open_notebook():
    notebook = tk.Toplevel(root)
    notebook.title("Notebook")
    notebook.geometry("500x500")

    text_area = scrolledtext.ScrolledText(notebook, wrap=tk.WORD, font=("Arial", 12))
    text_area.pack(expand=True, fill="both")

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", ".txt"), ("All files", ".*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))

    save_btn = tk.Button(notebook, text="Save", font=("Arial", 12), command=save_file)
    save_btn.pack()

notebook_button = tk.Button(root, text="Open Notebook", font=("Arial", 12), bg="#3498DB", fg="white", command=open_notebook)
notebook_button.pack(pady=10)

# Run the application
root.mainloop()