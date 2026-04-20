import customtkinter as ctk
from tkinter import ttk, messagebox
import random

# Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

processes = []

# Create Process
def create_process():
    pid = 1 if not processes else processes[-1]["pid"] + 1
    processes.append({"pid": pid, "state": "Ready"})
    update_table()

# Update Table
def update_table():
    for row in table.get_children():
        table.delete(row)

    for p in processes:
        tag = p["state"]
        table.insert("", "end", values=(p["pid"], p["state"]), tags=(tag,))

    count_label.configure(text=f"Total Processes: {len(processes)}")

# Change State
def change_state():
    try:
        pid = int(pid_entry.get())
        new_state = state_var.get()

        for p in processes:
            if p["pid"] == pid:
                p["state"] = new_state
                update_table()
                return

        messagebox.showerror("Error", "Process not found!")
    except:
        messagebox.showerror("Error", "Invalid PID!")

# Delete Process
def delete_process():
    try:
        pid = int(pid_entry.get())

        for i in range(len(processes)):
            if processes[i]["pid"] == pid:
                processes.pop(i)
                update_table()
                return

        messagebox.showerror("Error", "Process not found!")
    except:
        messagebox.showerror("Error", "Invalid PID!")

# Simulation (state changes automatically)
def run_simulation():
    if not processes:
        return

    for p in processes:
        p["state"] = random.choice(["Ready", "Running", "Waiting"])

    update_table()

# GUI
app = ctk.CTk()
app.title("Process Manager")
app.geometry("700x550")

title = ctk.CTkLabel(app, text="Process Management System",
                     font=("Arial", 20, "bold"))
title.pack(pady=10)

count_label = ctk.CTkLabel(app, text="Total Processes: 0",
                           font=("Arial", 14))
count_label.pack()

frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=10, fill="x")

create_btn = ctk.CTkButton(frame, text="Create Process", command=create_process)
create_btn.grid(row=0, column=0, padx=10, pady=10)

pid_entry = ctk.CTkEntry(frame, placeholder_text="Enter PID")
pid_entry.grid(row=0, column=1, padx=10)

state_var = ctk.StringVar(value="Ready")
state_menu = ctk.CTkOptionMenu(frame, variable=state_var,
                               values=["Ready", "Running", "Waiting"])
state_menu.grid(row=0, column=2, padx=10)

change_btn = ctk.CTkButton(frame, text="Change State", command=change_state)
change_btn.grid(row=1, column=0, padx=10, pady=10)

delete_btn = ctk.CTkButton(frame, text="Delete Process", command=delete_process)
delete_btn.grid(row=1, column=1, padx=10)

simulate_btn = ctk.CTkButton(frame, text="Run Simulation", command=run_simulation)
simulate_btn.grid(row=1, column=2, padx=10)

# TABLE STYLE
style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                font=("Arial", 14),
                rowheight=32)

style.configure("Treeview.Heading",
                font=("Arial", 16, "bold"))

# Table
table = ttk.Treeview(app, columns=("PID", "State"), show="headings")

table.heading("PID", text="PID")
table.heading("State", text="State")

table.column("PID", anchor="center", width=120)
table.column("State", anchor="center", width=300)

# Color tags
table.tag_configure("Ready", background="#1f6aa5", foreground="white")
table.tag_configure("Running", background="#2ecc71", foreground="black")
table.tag_configure("Waiting", background="#f39c12", foreground="black")

table.pack(pady=20, fill="both", expand=True)

app.mainloop()