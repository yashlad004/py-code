# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 20:57:50 2024

@author: Ladya
"""

import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Tasks list
        self.tasks = []

        # Task entry
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task button
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        # Tasks listbox
        self.task_listbox = tk.Listbox(root, height=10, width=40)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.task_listbox.bind('<<ListboxSelect>>', self.load_selected_task)

        # Update Task entry
        self.update_entry = tk.Entry(root, width=30)
        self.update_entry.grid(row=2, column=0, padx=10, pady=10)

        # Update Task button
        update_button = tk.Button(root, text="Update Task", command=self.update_task)
        update_button.grid(row=2, column=1, padx=20, pady=20)

        # Track Task button
        track_button = tk.Button(root, text="Track Task", command=self.track_task)
        track_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Exit button
        exit_button = tk.Button(root, text="Exit", command=root.destroy)
        exit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            new_task = self.update_entry.get()
            if new_task:
                old_task = self.task_listbox.get(selected_index)
                self.tasks[selected_index] = new_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, new_task)
                self.update_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a new task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def load_selected_task(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            self.update_entry.delete(0, tk.END)
            self.update_entry.insert(tk.END, selected_task)

    def track_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            messagebox.showinfo("Task Tracking", f'Tracking task: "{selected_task}"')
        else:
            messagebox.showwarning("Warning", "Please select a task to track.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
