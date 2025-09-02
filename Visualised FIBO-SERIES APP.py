

#SHIFTINNG THE CODE TO CUSTOMTKINTER FROM TKINTER
import customtkinter as ctk
from tkinter import messagebox

#appearance and theme
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

def calculate_series():
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError("Please enter a positive integer.")

        fiblist = [0, 1]
        for i in range(n - 2):
            fiblist.append(fiblist[i] + fiblist[i + 1])

        gratio = [fiblist[i] / float(fiblist[i - 1]) for i in range(2, len(fiblist))]

        fib_output = "Fibonacci Series:\n" + ", ".join(map(str, fiblist))
        ratio_output = "\n\nGolden Ratio:\n" + ", ".join(f"{x:.3f}" for x in gratio)
        result_label.configure(text=f"{fib_output}{ratio_output}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Error: {e}")

#main window of app
app = ctk.CTk()
app.title("Fibonacci & Golden Ratio")
app.geometry("600x500")
app.resizable(False, False)


title = ctk.CTkLabel(app, text="Fibonacci & Golden Ratio Calculator", font=ctk.CTkFont(size=20, weight="bold"))
title.pack(pady=20)

#Inputts:
input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=10)

entry_label = ctk.CTkLabel(input_frame, text="Enter Number of Terms:", font=ctk.CTkFont(size=14))
entry_label.grid(row=0, column=0, padx=10, pady=10)

entry = ctk.CTkEntry(input_frame, width=100)
entry.grid(row=0, column=1, padx=10, pady=10)

calc_button = ctk.CTkButton(input_frame, text="Calculate", command=calculate_series)
calc_button.grid(row=0, column=2, padx=10, pady=10)

#Results showing:
result_frame = ctk.CTkFrame(app, width=550, height=300)
result_frame.pack(pady=20, padx=20, fill="both", expand=True)

result_label = ctk.CTkLabel(result_frame, text="Results will appear here", anchor="nw", justify="left", font=ctk.CTkFont(size=13), wraplength=520)
result_label.pack(padx=15, pady=15, fill="both", expand=True)


app.mainloop()
