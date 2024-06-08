import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x450")
        
        self.tasks = []
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        
        self.listbox = tk.Listbox(self.frame, width=50, height=15, font=("Arial", 12), selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=20)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)
        
        self.add_task_button = tk.Button(self.button_frame, text="Add Task", width=10, command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=10)
        
        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", width=10, command=self.delete_task)
        self.delete_task_button.pack(side=tk.LEFT, padx=10)
        
        self.clear_tasks_button = tk.Button(self.button_frame, text="Clear All", width=10, command=self.clear_tasks)
        self.clear_tasks_button.pack(side=tk.LEFT, padx=10)
    
    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task.")
    
    def clear_tasks(self):
        if messagebox.askyesno("Confirm", "Do you really want to delete all tasks?"):
            self.tasks = []
            self.update_listbox()
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
