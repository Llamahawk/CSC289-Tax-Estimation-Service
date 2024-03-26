import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("500x300")
window.title("Tax Estimation Service")

frame = tk.Frame(window)
frame.pack()

label = tk.Label(window, text="North Carolina Tax Estimation Service")
label.pack(padx=20, pady=20)

user_info_frame = tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label = tk.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=[" ","Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

tax_info_frame = tk.LabelFrame(frame, text="Tax Information")
tax_info_frame.grid(row=2, column=0, padx=20, pady=20)

annual_income_label = tk.Label(tax_info_frame, text="Annual Income")
annual_income_label.grid(row=2, column=0)
filing_status_label = tk.Label(tax_info_frame, text="Filing Status")
filing_status_label.grid(row=2, column=1)

annual_income_entry = tk.Entry(tax_info_frame)
annual_income_entry.grid(row=3, column=0)
filing_status_combobox = ttk.Combobox(tax_info_frame, values=["Single", "Married joint filing", "Married seperate filing", "head of household", "Qualifying Widow"])
filing_status_combobox.grid(row=3, column=1)


submit = tk.Button(window, text="Submit")
submit.pack()

window.mainloop()