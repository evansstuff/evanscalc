import tkinter as tk

# create root window
root = tk.Tk()
root.resizable(width=False, height=False)
root.title("evan's calc 2026")

entry_1 = tk.Entry(root)

def add_to_entry(char):
    entry_1.insert(tk.END, char)

def calc_entry_contents():
    entry_contents = entry_1.get()
    # check if entry is empty
    if entry_contents:
        # get last character
        entry_last_char = entry_contents[-1]
        # check if last character is digit
        if entry_last_char.isdigit():
            entry_1.delete(0, tk.END)
            entry_result = eval(entry_contents)
            add_to_entry(str(entry_result))

# define buttons
button_1 = tk.Button(root, text = '1', height = 2, width = 2, command = lambda: add_to_entry("1"))
button_2 = tk.Button(root, text = '2', height = 2, width = 2, command = lambda: add_to_entry("2"))
button_3 = tk.Button(root, text = '3', height = 2, width = 2, command = lambda: add_to_entry("3"))
button_4 = tk.Button(root, text = '4', height = 2, width = 2, command = lambda: add_to_entry("4"))
button_5 = tk.Button(root, text = '5', height = 2, width = 2, command = lambda: add_to_entry("5"))
button_6 = tk.Button(root, text = '6', height = 2, width = 2, command = lambda: add_to_entry("6"))
button_7 = tk.Button(root, text = '7', height = 2, width = 2, command = lambda: add_to_entry("7"))
button_8 = tk.Button(root, text = '8', height = 2, width = 2, command = lambda: add_to_entry("8"))
button_9 = tk.Button(root, text = '9', height = 2, width = 2, command = lambda: add_to_entry("9"))
button_0 = tk.Button(root, text = '0', height = 2, width = 2, command = lambda: add_to_entry("0"))
button_add = tk.Button(root, text = '+', height = 2, width = 2, command = lambda: add_to_entry("+"))
button_sub = tk.Button(root, text = '-', height = 2, width = 2, command = lambda: add_to_entry("-"))
button_mul = tk.Button(root, text = '*', height = 2, width = 2, command = lambda: add_to_entry("*"))
button_div = tk.Button(root, text = '/', height = 2, width = 2, command = lambda: add_to_entry("/"))
button_dec = tk.Button(root, text = '.', height = 2, width = 2, command = lambda: add_to_entry("."))
button_eql = tk.Button(root, text = '=', height = 2, width = 8, command = calc_entry_contents)
button_pwr = tk.Button(root, text = '**', height = 2, width = 2, command = lambda: add_to_entry("**"))
button_clr = tk.Button(root, text = 'Clear', height = 2, width = 8, command = lambda: entry_1.delete(0, tk.END))

# show buttons
entry_1.grid(row = 0, column = 0, columnspan = 4)
button_clr.grid(row = 1, column = 0, columnspan = 2)
button_pwr.grid(row = 1, column = 2)
button_div.grid(row = 1, column = 3)
button_7.grid(row = 2, column = 0)
button_8.grid(row = 2, column = 1)
button_9.grid(row = 2, column = 2)
button_mul.grid(row = 2, column = 3)
button_4.grid(row = 3, column = 0)
button_5.grid(row = 3, column = 1)
button_6.grid(row = 3, column = 2)
button_sub.grid(row = 3, column = 3)
button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 1)
button_3.grid(row = 4, column = 2)
button_add.grid(row = 4, column = 3)
button_0.grid(row = 5, column = 0)
button_dec.grid(row = 5, column = 1)
button_eql.grid(row = 5, column = 2, columnspan = 2)

root.mainloop()
