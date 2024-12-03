import os
import img2pdf
import PIL
import tkinter as tk

from PIL import Image
from PIL import ImageOps
from PyPDF2 import PdfFileMerger
from tkinter import *
from tkinter import filedialog as fd, messagebox

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
    dir_name = fd.askdirectory(mustexist=True)
    return os.path.normpath(dir_name)


def is_valid_file(file_name, extensions):
    """Checks if the file has a valid extension."""
    return file_name.lower().endswith(extensions)


def convert_jpg_to_pdf():
    dir_name = get_dir_name()
    if not dir_name:
        return
    original_dir = os.getcwd()
    os.chdir(dir_name)
    try:
        imgs = [os.path.join(dir_name, f) for f in os.listdir(dir_name) if is_valid_file(f, (".jpg", ".jpeg"))]
        if imgs:
            with open("New File.pdf", "wb") as f:
                f.write(img2pdf.convert(imgs))
            messagebox.showinfo(title="Success", message='"New File.pdf" created successfully.')
        else:
            messagebox.showerror(title="Error", message="No JPG files found.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")
    finally:
        os.chdir(original_dir)


def compress_jpg():
    dir_name = get_dir_name()
    if not dir_name:
        return
    try:
        for file_name in os.listdir(dir_name):
            if is_valid_file(file_name, (".jpg", ".jpeg")):
                path = os.path.join(dir_name, file_name)
                with PIL.Image.open(path) as img:
                    img = ImageOps.exif_transpose(img)
                    img.save(path, quality=85, optimize=True)
        messagebox.showinfo(title="Success", message="JPG files compressed successfully.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")


def merge_pdf():
    dir_name = get_dir_name()
    if not dir_name:
        return
    original_dir = os.getcwd()
    os.chdir(dir_name)
    try:
        merger = PdfFileMerger()
        pdf_files = [os.path.join(dir_name, f) for f in os.listdir(dir_name) if is_valid_file(f, ".pdf")]
        if pdf_files:
            for pdf in pdf_files:
                merger.append(pdf)
            merger.write("Merged File.pdf")
            messagebox.showinfo(title="Success", message='"Merged File.pdf" created successfully.')
        else:
            messagebox.showerror(title="Error", message="No PDF files found.")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")
    finally:
        merger.close()
        os.chdir(original_dir)


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
