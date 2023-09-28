import tkinter as tk
from tkinter import scrolledtext
import subprocess
import interpreterv2 as ann


def run_code():
    code = code_input.get(1.0, tk.END)
    data = ann.convert_to_code(code)
    result = ann.do_it(data, True)

    code_output.config(state="normal")
    code_output.delete(1.0, tk.END)
    code_output.insert(tk.END, str(result))
    code_output.config(state="disabled")

def save_code():
    code = code_input.get(1.0, tk.END)
    try:
        with open("temp_script.ann", "w") as temp_file:
            temp_file.write(code)
    except Exception as e:
        code_input.config(state="normal")
        code_input.delete(1.0, tk.END)
        code_input.insert(tk.END, str(e))
        code_input.config(state="disabled")


root = tk.Tk()
root.title("ANN IDE")

# INPUT
code_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
code_input.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# BUTTONS
run_button = tk.Button(root, text="run code", command=run_code)
run_button.pack(side=tk.LEFT, padx=10, pady=10)

run_button = tk.Button(root, text="save code", command=save_code)
run_button.pack(side=tk.LEFT, padx=10, pady=10)

# OUTPUT
code_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10)
code_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
