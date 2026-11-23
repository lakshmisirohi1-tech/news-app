import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()

# Window title
root.title("News App")

# Window size
root.geometry("900x600")

# Background color
root.configure(bg="#101820")

# Heading
heading = tk.Label(
    root,
    text="NEWS APP",
    font=("Arial", 26, "bold"),
    bg="#101820",
    fg="white"
)

heading.pack(pady=30)

# Welcome message
message = tk.Label(
    root,
    text="Stay Updated. Stay Informed.",
    font=("Arial", 14),
    bg="#101820",
    fg="#00D9FF"
)

message.pack()

# Run application
root.mainloop()
