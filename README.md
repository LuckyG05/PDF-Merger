# PDF-Merger
A practical **Python script to effortlessly merge multiple PDF documents** into one cohesive file. Designed for ease of use, it provides a command-line utility for quick PDF concatenation.

---

## Project Overview

This is a powerful yet easy-to-use command-line tool built in Python that lets you merge multiple PDF files into a single document. Instead of relying on complex software, this script provides a lightweight solution for organizing your files. It's designed to be robust and user-friendly, with built-in error handling to prevent crashes from invalid inputs or missing files. Whether you need to combine project reports, consolidate invoices, or compile multiple chapters, this tool simplifies the process directly from your terminal.

---

## Features

* **User-Friendly Interface:** The script prompts you for the number of files and their names.
* **Error Handling:** The program won't crash if you enter an invalid number, a file that doesn't exist, or make other common mistakes.
* **Safe File Handling:** Uses `PyPDF2` to securely read and merge PDFs.
* **Clear Output:** Notifies you which files were successfully added and if the final merged PDF was created.

---

## Requirements

You only need **Python 3.x** and the **PyPDF2** library. You can install the library using `pip`:
```bash
pip install PyPDF2
```

---

## How to Use
1. Clone the Repository:
Get a copy of the project on your local machine using this command:
```bash
git clone https://github.com/LuckyG05/PDF-Merger.git
```

2. Navigate to the Project Directory:
Move into the project folder using your terminal:
```bash
cd PDF-Merger
```

3. Place Your PDF Files:
Put all the PDF files you want to merge into this same directory.

4. Run the Script:
Execute the script using the following command:
```bash
python main.py
```

5. The script will then guide you through the merging process by asking you for the number of PDFs and their filenames.

---

## Contributing
Feel free to fork this repository and submit pull requests to improve the script. All contributions are welcome!

---

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contact
If you have any questions or feedback, feel free to reach out:
* **GitHub:** [LuckyG05](https://github.com/LuckyG05)

---

