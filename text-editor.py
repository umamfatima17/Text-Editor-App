
import tkinter as tk
from tkinter import filedialog, messagebox

# Main window
root = tk.Tk()
root.title("My Text Editor")
root.geometry("800x600")

# Text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 18)
)

text.pack(expand=True, fill=tk.BOTH)


# Function to create a new document
def new_file():
    text.delete("1.0", tk.END)


# Function to open a text file
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            text.delete("1.0", tk.END)
            text.insert("1.0", content)

        except OSError as error:
            messagebox.showerror("Error", f"Could not open file:\n{error}")


# Function to save a text file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text.get("1.0", "end-1c"))

            messagebox.showinfo("Success", "File saved successfully!")

        except OSError as error:
            messagebox.showerror("Error", f"Could not save file:\n{error}")


# Create menu bar
main_menu = tk.Menu(root)
root.config(menu=main_menu)

file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Run the application
root.mainloop()
