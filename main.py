# UI for the downloader program, allowing user interactivity.
# Imports
import tkinter as tk
from tkinter import *
from tkinter import filedialog, ttk, messagebox
from downloader import *

# Root window
root = Tk()

# Window title and dimension
root.title("Audio mp3 downloader")
root.geometry("600x200")

# Labels
label = Label(root, text="Welcome to the audio downloader app! \nWrite the url to the audio origin:")
label.grid(row=0, column=0, padx=10, pady=10)

file_types_lbl = Label(root, text="Select the output folder:")
file_types_lbl.grid(row=1, column=0, padx=10, pady=10)

# Functions
def select_file():
    # Ask the user to select a folder to output the downloaded file
    file_path = filedialog.askdirectory(
        title="Select the folder to output",
        initialdir="/",
    )
    selector.configure(text = file_path) # Update the text to display the selected file_path

def clicked():
    # Get the url and output folder
    url = entry_url.get()
    output_path = selector.cget("text")

    # Clear the entry box after getting the input
    entry_url.delete(0, tk.END)

    # Download and show the success to the user
    file = download(url, output_path)
    messagebox.showinfo(message=f'{file}.mp3 downloaded successfully! Path:{output_path}')

# Buttons
selector = Button(root, text="Select Folder", command=select_file)
selector.grid(row=1, column=1, padx=10, pady=10)

button = Button(root, text="Download", command=clicked)
button.grid(row=3, column=1, padx=10, pady=10)

# Entry box
entry_url = tk.Entry(root, width=50)
entry_url.focus_set()
entry_url.grid(row=0, column=1, padx=10, pady=10)

# Main Loop 
root.mainloop()