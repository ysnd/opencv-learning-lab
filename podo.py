import tkinter as tk
from tkinter import messagebox
import time
import threading

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.tasks = []
        self.current_task = None
        self.pomodoros = 0
        self.work_time = 25 * 60
        self.break_time = 5 * 60

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def start_timer(self):
        if not self.tasks:
            messagebox.showwarning("No Tasks", "Please add tasks first.")
            return
        self.current_task = self.tasks.pop(0)
        self.task_listbox.delete(0)
        self.run_timer(self.work_time, "Work")

    def run_timer(self, duration, mode):
        if duration > 0:
            self.root.title(f"{mode} - {duration // 60}:{duration % 60:02}")
            self.root.after(1000, self.run_timer, duration - 1, mode)
        else:
            if mode == "Work":
                self.pomodoros += 1
                messagebox.showinfo("Time's up!", "Take a break!")
                self.run_timer(self.break_time, "Break")
            else:
                messagebox.showinfo("Break's over!", "Time to work!")
                if self.tasks:
                    self.current_task = self.tasks.pop(0)
                    self.task_listbox.delete(0)
                    self.run_timer(self.work_time, "Work")
                else:
                    messagebox.showinfo("All Done!", "You've completed all tasks!")
                    self.root.title("Pomodoro Timer")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
