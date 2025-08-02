from PyPDF2 import PdfWriter

# Create a PdfWriter object that will handle the merging
merger = PdfWriter()

# list to store pdf files names
pdfs = []

# Loop to ensure the user provides a valid positive integer for the number of PDFs.
n = 0
while n <= 0:
    try:
        n = int(input("How many pdfs you want to merge?\n"))
        if n <= 0:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")

for i in range(0,n):
    name = input(f"Enter name of {i+1} pdf: ")
    # Break the loop if the user enters a blank line
    if not name:
        break
    pdfs.append(name)

for pdf in pdfs:
    try: 
        with open(pdf, "rb") as pdf_file:
            merger.append(pdf_file)
            print(f"Successfully added '{pdf}' to the merger")
    except FileNotFoundError:
        # Execute if the file name entered by the user doesn't exist
        print(f"Error: The file '{pdf}' was not found. Skipping this file")
    except Exception as e:
        print(f"An error occurred while trying to process '{pdf}': {e}")

# Check if any PDFs were successfully added before writing the output
if len(merger.pages) > 0:
    merger.write("MERGED.pdf")
    print("Successfully merged pdfs into MERGED file")
else:
    print("No pdf files are added. The merge operation was cancelled")
    
merger.close()