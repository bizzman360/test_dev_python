import tkinter as tk
window = tk.Tk()
window.title("My first application")
window.geometry("600x400")
window.configure(bg="white")
window.resizable(False, False)
from tkinter import PhotoImage

# window.mainloop()

#=========================================#

# header_label = tk.Label(window, text="Welcome Students")
# entry = tk.Entry(window)

# header_label.pack()
# entry.pack()

# window.mainloop()

#=========================================#

# header_label = tk.Label(window, text="Welcome Students")
# entry = tk.Entry(window)
# button = tk.Button(window, text="Submit")

# header_label.pack()
# entry.pack()
# button.pack()

# window.mainloop()

#=========================================#

# header_label = tk.Label(window, text="Welcome Students")
# entry = tk.Entry(window)
# button = tk.Button(window, text="Submit")

# img = tk.PhotoImage(file="PDU Logo-Color.png")
# img = img.subsample(8,8)
# img_label = tk.Label(window, image=img)

# img_label.pack()
# header_label.pack()
# entry.pack()
# button.pack()

# window.mainloop()

#=========================================#

# header_label = tk.Label(window, text="Welcome Students")
# entry = tk.Entry(window)
# entry.insert(0, "Enter your name here")

# img = tk.PhotoImage(file="PDU Logo-Color.png")
# img = img.subsample(8,8)
# img_label = tk.Label(window, image=img)

# def button_action():
#     name = entry.get()
#     print(name)
# button = tk.Button(window, text="Submit", command=button_action)

# img_label.pack()
# header_label.pack()
# entry.pack()
# button.pack()

# window.mainloop()

#=========================================#

# header_label = tk.Label(window, text="Welcome Students")
# entry = tk.Entry(window)

# img = tk.PhotoImage(file="PDU Logo-Color.png")
# img = img.subsample(8,8)
# img_label = tk.Label(window, image=img)

# header_label.config(text="Hello students",
#       fg="blue",
#       bg="yellow",
#       font=("Arial", 16)
#       )

# def button_action():
#     name = entry.get()
#     print(name)
# button = tk.Button(window, text="Submit", command=button_action)

# img_label.pack()
# header_label.pack()
# entry.pack()
# button.pack()

# window.mainloop()

#=========================================#

# header_label = tk.Label(window, text="Welcome Students", fg="blue", bg="yellow", font=("Segoe UI", 14))
# header_label.grid(row=1, column=0, columnspan=2, pady=10)
# name_label = tk.Label(window, text="Your name")
# name_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')

# entry = tk.Entry(window)
# entry.grid(row=2, column=1, padx=5, pady=5)

# img = tk.PhotoImage(file="PDU Logo-Color.png")
# img = img.subsample(8,8)
# img_label = tk.Label(window, image=img)
# img_label.grid(row=0, column=0, columnspan=2, pady=10)


# header_label.config(text="Hello students",
#       fg="blue",
#       bg="yellow",
#       font=("Arial", 16)
#       )

# def button_action():
#     name = entry.get()
#     print(name)
# button = tk.Button(window, text="Submit", command=button_action)
# button.grid(row=3, column=0, columnspan=2, pady=10)

# window.mainloop()

#=========================================#

# from tkinter import messagebox

# header_label = tk.Label(window, text="Welcome Students", fg="blue", bg="yellow", font=("Segoe UI", 14))
# header_label.grid(row=1, column=0, columnspan=2, pady=10)
# name_label = tk.Label(window, text="Your name")
# name_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')

# entry = tk.Entry(window)
# entry.grid(row=2, column=1, padx=5, pady=5)

# img = tk.PhotoImage(file="PDU Logo-Color.png")
# img = img.subsample(8,8)
# img_label = tk.Label(window, image=img)
# img_label.grid(row=0, column=0, columnspan=2, pady=10)

# header_label.config(text="Hello students",
#       fg="blue",
#       bg="yellow",
#       font=("Arial", 16)
#       )

# def button_action():
#     name = entry.get()
#     print(name)

#     messagebox.showinfo(
#         "SUCCESS!",
#         f"You have succefully entered {name}, as the input"
#     )

# button = tk.Button(window, text="Submit", command=button_action)
# button.grid(row=3, column=0, columnspan=2, pady=10)

# window.mainloop()

#=========================================#

# from tkinter import messagebox

# header_label = tk.Label(window, text="Welcome Students", fg="blue", bg="yellow", font=("Segoe UI", 14))
# header_label.grid(row=1, column=0, columnspan=2, pady=10)
# name_label = tk.Label(window, text="Your name")
# name_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')

# entry = tk.Entry(window)
# entry.grid(row=2, column=1, padx=5, pady=5)

# img = tk.PhotoImage(file="PDU Logo-Color.png")
# img = img.subsample(8,8)
# img_label = tk.Label(window, image=img)
# img_label.grid(row=0, column=0, columnspan=2, pady=10)

# header_label.config(text="Hello students",
#       fg="blue",
#       bg="yellow",
#       font=("Arial", 16)
#       )

# def button_action():
#     name = entry.get()
#     print(name)

#     messagebox.showinfo(
#         "SUCCESS!",
#         f"You have succefully entered {name}, as the input"
#     )

# def close_button_action():
#     exit_confirm = messagebox.askyesno("Exit", "Cancel")
#     if exit_confirm:
#         window.destroy()
#     else:
#         pass

# button = tk.Button(window, text="Submit", command=button_action)
# button.grid(row=3, column=0, padx=5, pady=5)
# close_button = tk.Button(window, text="Exit", command=close_button_action)
# close_button.grid(row=3, column=1, padx=5, pady=5)

# window.mainloop()

#=========================================#