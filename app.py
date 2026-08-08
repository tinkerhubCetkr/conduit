import tkinter as tk
from tkinter import ttk

import core.config
html_file_path = core.config.SOURCE_DIR;

def handle_click():
    print(f"Submitted text: {entry.get()}")

# Initialize main window
root = tk.Tk()
root.title("conduit")
root.geometry("1000x1000")

# Create the Notebook (Tab manager)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

#TAB 1: Input Section
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Div By Class")

# Input layout
frame_input = ttk.Frame(tab1)
frame_input.pack(padx=20, pady=30, fill="x")

html_file_path_label = ttk.Label(frame_input, text=html_file_path)
html_file_path_label.pack(side="left",padx=20, pady=30)

entry = ttk.Entry(frame_input)
entry.pack(side="left", fill="x", expand=True)

button = ttk.Button(frame_input, text="Submit", command=handle_click)
button.pack(side="left", padx=(0, 10))

#TAB 2: Second Section 
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Analytics / Logs")

label2 = ttk.Label(tab2, text="dgfgdfgfdgfdge.")
label2.pack(padx=20, pady=30)

#TAB 3: Third Section
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Settings")

label3 = ttk.Label(tab3, text="dfgdfgdfgd.")
label3.pack(padx=20, pady=30)

root.mainloop()