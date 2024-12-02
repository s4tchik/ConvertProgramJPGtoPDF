# PDF and JPG Tool for SAT

A simple GUI tool that allows you to convert JPG images to PDF, compress JPG files, and merge multiple PDF files into one. This tool uses Python with several libraries, including `Pillow`, `PyPDF2`, `img2pdf`, and `tkinter` to provide an intuitive user interface.

## Features

- **Convert JPG to PDF**: Converts JPG files in a folder to a single PDF.
- **Convert and Compress JPG to PDF**: Compress JPG files before converting them to PDF.
- **Merge PDF Files**: Merges multiple PDF files into one.
- **Compress JPG Files**: Compresses JPG files to reduce their file size.

## Requirements

- Python 3.x
- Libraries:
  - `Pillow` (for image manipulation)
  - `PyPDF2` (for merging PDFs)
  - `img2pdf` (for converting images to PDF)
  - `tkinter` (for GUI)
  - `pikepdf` (optional, for additional PDF manipulation)

You can install the required libraries using `pip`:

```bash
pip install Pillow PyPDF2 img2pdf pikepdf
```

## Usage

1. **Run the Application**:
   - To start the tool, simply run the script `main.py`. This will launch a graphical user interface (GUI) where you can interact with the features.

2. **Using the Tool**:
   - **Convert JPG to PDF**: Click "Select Folder" and choose a folder containing JPG files. The program will create a PDF file named `New File.pdf`.
   - **Convert and Compress JPG to PDF**: Select a folder with JPG files. The files will first be compressed and then converted into a PDF (`New File.pdf`).
   - **Merge PDF Files**: Choose a folder with PDF files. The tool will merge them into a single PDF named `Merged File.pdf`.
   - **Compress JPG Files**: Select a folder with JPG files to compress them and reduce their file size.

3. **Note**: Depending on the number and size of files, the program may take some time to process. If it freezes, wait for it to complete, or restart the program if necessary.

## File Structure

```plaintext
├── main.py              # The main Python script for the GUI
├── README.md            # Documentation for the project
└── requirements.txt     # (Optional) List of dependencies
```


## License

This project is licensed s4tchik.

## Acknowledgments

- The libraries `Pillow`, `PyPDF2`, `img2pdf`, and `tkinter` made the development of this tool easy and efficient.
