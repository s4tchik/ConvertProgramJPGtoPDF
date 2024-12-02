import os
import img2pdf
import PIL
import tkinter as tk

from PIL import Image
from PIL import ImageOps
from PyPDF2 import PdfFileMerger
from tkinter import *
from tkinter import filedialog as fd, messagebox
from pikepdf import _cpphelpers

# Main window setup
root = tk.Tk()
root['bg'] = "#fff8e1"
root.title("PDF and JPG Tool for SAT")
root.geometry("800x800")
root.resizable(False, False)

# Styling for buttons and labels
button_style = {
    "bg": "#fbc02d",
    "fg": "black",
    "font": ("Arial", 12, "bold"),
    "relief": "flat",
    "activebackground": "#f57f17",
    "activeforeground": "white",
    "width": 20,
    "pady": 5,
}

label_style = {
    "bg": "#fff8e1",
    "font": ("Arial", 12),
    "justify": "left",
}

header_style = {
    "bg": "#f57f17",
    "fg": "white",
    "font": ("Arial", 20, "bold"),
    "padx": 10,
    "pady": 10,
    "anchor": "w",
}


def get_dir_name():
    global dir_name
    dir_name = fd.askdirectory(mustexist=True)
    dir_name = os.path.normpath(dir_name)
    return dir_name


def convert_jpg_to_pdf():
    dir_name = get_dir_name()
    os.chdir(dir_name)
    with open(f"New File.pdf", "wb") as f:
        imgs = []
        for file_name in os.listdir(dir_name):
            if file_name.endswith((".jpg", ".JPG")):
                path = os.path.join(dir_name, file_name)
                imgs.append(path)
        try:
            f.write(img2pdf.convert(imgs))
            messagebox.showinfo(title="Success", message='"New File.pdf" created successfully.')
        except Exception as e:
            print(e)
            messagebox.showerror(title="Error", message="No JPG files found or folder not selected.")


def compress_jpg():
    dir_name = get_dir_name()
    if dir_name == ".":
        messagebox.showerror(title="Error", message="No folder selected.")
    else:
        for file_name in os.listdir(dir_name):
            if file_name.endswith((".jpg", ".JPG")):
                path = os.path.join(dir_name, file_name)
                img = PIL.Image.open(path)
                img = img.resize(img.size, PIL.Image.ANTIALIAS)
                img = ImageOps.exif_transpose(img)
                img.save(path)
        messagebox.showinfo(title="Success", message="JPG files compressed successfully.")


def merge_pdf():
    dir_name = get_dir_name()
    if dir_name == ".":
        messagebox.showerror(title="Error", message="No folder selected.")
    else:
        os.chdir(dir_name)
        merger = PdfFileMerger()
        for file_name in os.listdir(dir_name):
            if file_name.endswith(".pdf"):
                merger.append(os.path.join(dir_name, file_name))
        merger.write(f"Merged File.pdf")
        merger.close()
        messagebox.showinfo(title="Success", message='"Merged File.pdf" created successfully.')


def jpg_to_pdf_compress():
    compress_jpg()
    convert_jpg_to_pdf()


# UI Components
Label(root, text='PDF and JPG Tools', **header_style).pack(fill='x')

# From JPG to PDF
Label(root, text='Convert JPG to PDF', **label_style).pack(pady=(10, 0))
Label(root, text='Select a folder containing JPG files.\nA PDF file "New File.pdf" will be created.', **label_style).pack(pady=(0, 10))
Button(root, text='Select Folder', command=convert_jpg_to_pdf, **button_style).pack()

# JPG to PDF with compression
Label(root, text='Convert and Compress JPG to PDF', **label_style).pack(pady=(20, 0))
Label(root, text='Select a folder containing JPG files.\nFiles will be compressed before creating the PDF.', **label_style).pack(pady=(0, 10))
Button(root, text='Select Folder', command=jpg_to_pdf_compress, **button_style).pack()

# Merge PDFs
Label(root, text='Merge PDF Files', **label_style).pack(pady=(20, 0))
Label(root, text='Select a folder containing PDF files.\nA merged PDF file "Merged File.pdf" will be created.', **label_style).pack(pady=(0, 10))
Button(root, text='Select Folder', command=merge_pdf, **button_style).pack()

# Compress JPGs
Label(root, text='Compress JPG Files', **label_style).pack(pady=(20, 0))
Label(root, text='Select a folder containing JPG files to compress.', **label_style).pack(pady=(0, 10))
Button(root, text='Select Folder', command=compress_jpg, **button_style).pack()

# Info
Label(root, text='\nNote: The program may take some time to process large files.\nIf it freezes, wait until it completes or restart if necessary.', **label_style).pack(pady=(20, 0))

if __name__ == '__main__':
    root.mainloop()
