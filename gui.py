"""
IDK what the fuck I'm doing -- Redundant Puce
"""

import tkinter as tk 

class SimpleGUI:
    def __init__(self, master):
        master.title("SimpleGUI")
        
        self.vars = [tk.StringVar(master) for _ in range(6)]
        self.history = []
        
        # Input fields 
        for i, var in enumerate(self.vars):
            tk.Label(master, text=f"Variable {i+1}:").grid(row=i, column=0)
            tk.Entry(master, textvariable=var).grid(row=i, column=1)
        
        # Button to update variables
        self.update_button = tk.Button(master, text="Update", command=self.update_values)
        self.update_button.grid(row=6, columnspan=2)
        
        # Display history
        self.history_label = tk.Label(master, text="History:")
        self.history_label.grid(row=7, column=0)
        
        self.history_display = tk.Listbox(master)
        self.history_display.grid(row=7, column=1, sticky="ew")
    
    def update_values(self):
        current_values = [var.get() for var in self.vars]
        self.history.append(current_values)
        self.refresh_history()
    
    def refresh_history(self):
        self.history_display.delete(0, tk.END)
        for entry in self.history:
            self.history_display(tk.END, ', '.join(entry))