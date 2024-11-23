import tkinter as tk

def evaluate_expression():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        # In case of error
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def append_to_expression(char):
    entry.insert(tk.END, char)

def clear_expression():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)  # Clear button
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                        command=evaluate_expression)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                        command=clear_expression)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                        command=lambda t=text: append_to_expression(t))
    
    btn.grid(row=row, column=col, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i % 4, weight=1)


root.mainloop()
