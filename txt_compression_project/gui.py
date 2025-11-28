import tkinter as tk
from compress import compress,decompress
from tkinter import filedialog

def open_file():
    file_name = filedialog.askopenfilename(initialdir='/', title="Select a file to compress") 
    return file_name

def compression(i,o):
    compress(i,o)

window = tk.Tk()
window.title("Compression engine")
window.geometry("600x400")


compress_button = tk.Button(window, text='Compress', command=lambda:compression(open_file(), "compressed_output1.txt"))

compress_button.grid(row=2, column=1)


window.mainloop()