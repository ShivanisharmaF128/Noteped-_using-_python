import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Function to save the file
def saving_file():
    file_location = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not file_location:
        return
    with open(file_location, "w") as file_output:
        text = text_edit.get(1.0, tk.END)
        file_output.write(text)
    root.title(f"MY OWN NOTEPAD - {file_location}")

# Function to open a file
def opening_file():
    file_location = askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not file_location:
        return
    text_edit.delete(1.0, tk.END)
    with open(file_location, "r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    root.title(f"MY OWN NOTEPAD - {file_location}")    

# Creating the main window
root = tk.Tk()
root.title("MY OWN NOTEPAD")
root.geometry("900x600")
root.configure(bg="#2b2b2b")  # Dark theme

# Configuring row and column
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Creating a Text Widget with a custom font & color
text_edit = tk.Text(root, wrap="word", font=("Consolas", 14), fg="#ffffff", bg="#3c3f41", insertbackground="white")
text_edit.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

# Creating a frame for buttons
frame_button = tk.Frame(root, bg="#2b2b2b")
frame_button.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

# Styled buttons with ttk
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)

button_open = ttk.Button(frame_button, text="📂 Open File", command=opening_file)
button_open.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

button_save = ttk.Button(frame_button, text="💾 Save As", command=saving_file)
button_save.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Run the application
root.mainloop()
