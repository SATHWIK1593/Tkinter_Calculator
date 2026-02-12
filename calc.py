import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("800x1000")
root.resizable(False, False)

entry1 = tk.Entry(
    root,
    font=("Arial", 20),
    bg="black",
    fg="white",
    bd=0,
    justify="right"
)
entry1.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10)

def press(value):
    entry1.insert(tk.END, value)

def clear():
    entry1.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry1.get())
        entry1.delete(0, tk.END)
        entry1.insert(0, result)
    except:
        entry1.delete(0, tk.END)
        entry1.insert(0, "Error")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for btn in buttons:
    if btn == "=":
        command = calculate
    else:
        command = lambda x=btn: press(x)

    tk.Button(
        root,
        text=btn,
        font=("Bold", 18),
        bg="blue" if btn in "+-*/=" else "black",
        fg="white",
        width=5,
        height=2,
        bd=0,
        command=command
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col == 4:
        col = 0
        row += 1

tk.Button(
    root,
    text="C",
    font=("Bold", 18),
    bg="red",
    fg="white",
    width=22,
    height=2,
    bd=0,
    command=clear
).grid(row=row, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
