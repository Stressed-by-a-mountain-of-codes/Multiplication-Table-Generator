import tkinter as tk
from tkinter import messagebox
import pyttsx3
import threading
import time

engine = pyttsx3.init()

def speak_lines(lines):
    for line in lines:
        engine.say(line)
    engine.runAndWait()

def generate_table():
    num = entry.get()
    if not num.lstrip('-').isdigit():
        messagebox.showerror("Invalid Input", "Enter a valid integer.")
        return

    n = int(num)
    lines = [f"{n} × {i} = {n * i}" for i in range(1, 11)]
    result_label.config(text="\n".join(lines), fg="darkgreen")

    threading.Thread(target=speak_lines, args=(lines,), daemon=True).start()
    root.after(5000, reset)

def reset():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Multiplication Table Speaker")
root.geometry("350x350")
root.resizable(False, False)

tk.Label(root, text="Enter a number:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack()
entry.bind("<Return>", lambda e: generate_table())

tk.Button(root, text="Generate & Speak", font=("Arial", 12), command=generate_table).pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier New", 11), justify="left")
result_label.pack(pady=10)

entry.focus()
root.mainloop()
