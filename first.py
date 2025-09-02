#this is now discarded.. switched to custom tkinter in the other file

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def calculate_series():
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError("Please enter a positive integer.")

        # Fibonacci calculation
        fiblist = [0, 1]
        for i in range(n - 2):
            fiblist.append(fiblist[i] + fiblist[i + 1])

        gratio = [fiblist[i] / float(fiblist[i - 1]) for i in range(2, len(fiblist))]

        fib_output = "Fibonacci Series:\n" + ", ".join(map(str, fiblist))
        ratio_output = "\n\nGolden Ratio:\n" + ", ".join(f"{x:.3f}" for x in gratio)
        result_label.config(text=f"{fib_output}{ratio_output}")

    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")



root = tk.Tk()
root.title("Fibonacci & Golden Ratio")
root.geometry("560x450")
root.configure(bg="#f2f2f2")
root.resizable(False, False)


title_label = tk.Label(
    root,
    text="Fibonacci Series & Golden Ratio Calculator",
    font=("Helvetica", 18, "bold"),
    bg="#f2f2f2",
    fg="#333"
)
title_label.pack(pady=20)


input_frame = tk.Frame(root, bg="#f2f2f2")
input_frame.pack(pady=10)

entry_label = tk.Label(
    input_frame,
    text="Enter Number of Terms:",
    font=("Helvetica", 12),
    bg="#f2f2f2"
)
entry_label.grid(row=0, column=0, padx=5)

entry = ttk.Entry(input_frame, width=10)
entry.grid(row=0, column=1, padx=5)

calc_button = ttk.Button(input_frame, text="Calculate", command=calculate_series)
calc_button.grid(row=0, column=2, padx=10)


separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", pady=15)


result_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
result_frame.pack(padx=20, pady=10, fill="both", expand=True)

result_label = tk.Label(
    result_frame,
    text="Results will appear here",
    font=("Courier New", 12),
    bg="white",
    fg="#333",
    justify="left",
    anchor="nw"
)
result_label.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()
