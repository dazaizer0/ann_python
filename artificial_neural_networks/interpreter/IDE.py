import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import subprocess
import interpreterv2 as ann
import webbrowser


def run_code():
    code = code_input.get(1.0, tk.END)
    data = ann.convert_to_code(code)
    result = ann.do_it(data, True)

    code_output.config(state="normal")
    code_output.delete(1.0, tk.END)
    code_output.insert(tk.END, str(result))
    code_output.config(state="disabled")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            text = code_input.get(1.0, tk.END)
            file.write(text)

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            code_input.delete(1.0, tk.END)
            code_input.insert(tk.END, text)

def open_documentation():
    url = "https://github.com/dazaizer0/Neogus-ANN/releases"
    webbrowser.open(url)


root = tk.Tk()
root.title("ANN IDE")
root.configure(bg="grey4")

# INPUT
code_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, bg="grey8", fg="plum2")
code_input.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# BUTTONS
run_button = tk.Button(root, text="run code", command=run_code, bg="grey8", fg="plum2")
run_button.pack(side=tk.LEFT, padx=10, pady=10)

save_button = tk.Button(root, text="save code", command=save_file, bg="grey8", fg="plum2")
save_button.pack(side=tk.LEFT, padx=10, pady=10)

load_button = tk.Button(root, text="load code", command=load_file, bg="grey8", fg="plum2")
load_button.pack(side=tk.LEFT, padx=10, pady=10)

docu_button = tk.Button(root, text="open_documentation", command=open_documentation, bg="grey8", fg="plum2")
docu_button.pack(side=tk.LEFT, padx=10, pady=10)

# OUTPUT
code_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10, bg="grey8", fg="magenta2")
code_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
