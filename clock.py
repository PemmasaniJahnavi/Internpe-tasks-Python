import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=('arial', 60), bg="black", fg="cyan")
clock_label.pack(pady=50)


def update_clock():
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)


update_clock()

root.mainloop()