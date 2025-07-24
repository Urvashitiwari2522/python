import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import webbrowser

# Colors & Theme
BG_COLOR = "#1e1e2d"
FG_COLOR = "#ffffff"
BTN_COLOR = "#4CAF50"
BTN_HOVER = "#388E3C"
FONT = ("Arial", 12)

# Main Window
root = tk.Tk()
root.title("Urvashi's Portfolio")
root.geometry("600x750")
root.configure(bg=BG_COLOR)

# Title Frame
title_frame = tk.Frame(root, bg="#282c3c", height=80)
title_frame.pack(fill="x")

title_label = tk.Label(title_frame, text="Urvashi Tiwari", font=("Arial", 24, "bold"), fg="white", bg="#282c3c")
title_label.pack(pady=20)

subtitle_label = tk.Label(root, text="BCA Student | Python & ML Enthusiast", font=("Arial", 14), fg="#b0b0b0", bg=BG_COLOR)
subtitle_label.pack(pady=5)

# Skills Section
skills_frame = tk.Frame(root, bg=BG_COLOR)
skills_frame.pack(pady=10)

skills_label = tk.Label(skills_frame, text="Skills", font=("Arial", 16, "bold"), fg=FG_COLOR, bg=BG_COLOR)
skills_label.pack()

skills_text = "✅ Python  ✅ Java  ✅ Flask  ✅ Linux  ✅ MySQL  ✅ AI & ML"
skills_display = tk.Label(skills_frame, text=skills_text, font=FONT, fg="#cfcfcf", bg=BG_COLOR)
skills_display.pack()

# Projects Section
projects_label = tk.Label(root, text="Projects", font=("Arial", 16, "bold"), fg=FG_COLOR, bg=BG_COLOR)
projects_label.pack(pady=10)

projects_text = """• Hangman Game (Python)
• QR Code Generator
• Secret Code Language
• Chatbot
• Calculator (Tkinter)
• Notebook (Tkinter)"""
projects_display = tk.Label(root, text=projects_text, font=FONT, fg="#b0b0b0", bg=BG_COLOR)
projects_display.pack()

# Buttons Frame
buttons_frame = tk.Frame(root, bg=BG_COLOR)
buttons_frame.pack(pady=20)

# Function to create a button with hover effect
def create_button(frame, text, command, bg=BTN_COLOR, fg="white"):
    btn = tk.Button(frame, text=text, font=FONT, bg=bg, fg=fg, width=20, height=2, command=command, relief="flat")
    btn.pack(pady=5)
    btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
    btn.bind("<Leave>", lambda e: btn.config(bg=BTN_COLOR))
    return btn

# Open LinkedIn & GitHub
def open_linkedin():
    webbrowser.open("https://www.linkedin.com/in/urvashi-tiwari2208")

def open_github():
    webbrowser.open("https://github.com/urvashitiwari2522")

def show_contact():
    messagebox.showinfo("Contact Me", "Email: priyatiwari0425@gmail.com\nPhone: +91XXXXXXXXXX")

# Add Buttons
create_button(buttons_frame, "LinkedIn Profile", open_linkedin, "#0077b5")
create_button(buttons_frame, "GitHub Profile", open_github, "#24292e")
create_button(buttons_frame, "Contact Me", show_contact, "#FF9800")

# ---------- CALCULATOR ----------
def open_calculator():
    calc = tk.Toplevel(root)
    calc.title("Calculator")
    calc.geometry("300x400")
    calc.configure(bg="#222")

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

    entry = tk.Entry(calc, font=("Arial", 18), justify="right", bg="#333", fg="white")
    entry.pack(fill="both", padx=10, pady=10)

    buttons = [
        "7", "8", "9", "/", "4", "5", "6", "*",
        "1", "2", "3", "-", "0", ".", "=", "+"
    ]

    btn_frame = tk.Frame(calc, bg="#222")
    btn_frame.pack()

    row, col = 0, 0
    for button in buttons:
        if button == "=":
            btn = tk.Button(btn_frame, text=button, font=("Arial", 14), width=10, bg="#4CAF50", fg="white", command=calculate)
        else:
            btn = tk.Button(btn_frame, text=button, font=("Arial", 14), width=5, bg="#444", fg="white", command=lambda b=button: on_click(b))

        btn.grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

    clear_btn = tk.Button(calc, text="C", font=("Arial", 14), width=22, bg="#d9534f", fg="white", command=clear)
    clear_btn.pack(pady=5)

create_button(buttons_frame, "Open Calculator", open_calculator, "#FF5733")

# ---------- NOTEBOOK ----------
def open_notebook():
    notebook = tk.Toplevel(root)
    notebook.title("Notebook")
    notebook.geometry("500x500")
    notebook.configure(bg="#282c3c")

    text_area = scrolledtext.ScrolledText(notebook, wrap=tk.WORD, font=("Arial", 12), bg="#333", fg="white")
    text_area.pack(expand=True, fill="both")

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", ".txt"), ("All files", ".*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))

    save_btn = tk.Button(notebook, text="Save", font=("Arial", 12), bg="#3498DB", fg="white", command=save_file)
    save_btn.pack()

create_button(buttons_frame, "Open Notebook", open_notebook, "#3498DB")

# Run the application
root.mainloop()